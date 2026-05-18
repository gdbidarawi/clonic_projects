from datetime import datetime, date

class MedicalMaterial:
    def __init__(self, item_id: str, name: str, batch_number: str, quantity: int, expiration_date_str: str):
        """
        Represents a medical material or medicine in the hospital inventory.
        expiration_date_str format: 'YYYY-MM-DD'
        """
        self.item_id = item_id
        self.name = name
        self.batch_number = batch_number
        self.quantity = quantity
        # Convert string date to a datetime.date object for accurate comparisons
        self.expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d").date()

    def is_outdated(self) -> bool:
        """Checks if the item has already reached or passed its expiration date."""
        return self.expiration_date <= date.today()

    def days_until_expiration(self) -> int:
        """Returns the number of days left before expiration. Negative means already expired."""
        delta = self.expiration_date - date.today()
        return delta.days

    def __str__(self):
        status = "OUTDATED" if self.is_outdated() else f"{self.days_until_expiration()} days left"
        return f"[{self.item_id}] {self.name} (Batch: {self.batch_number}) | Qty: {self.quantity} | Exp: {self.expiration_date} ({status})"


class HospitalInventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_material(self, material: MedicalMaterial):
        """Adds an item to the tracking system."""
        self.inventory[material.item_id] = material

    def get_outdated_materials(self):
        """Filters and returns all materials that are expired."""
        outdated_items = [item for item in self.inventory.values() if item.is_outdated()]
        return outdated_items

    def get_near_expiry_materials(self, threshold_days: int = 30):
        """Filters items that are not expired yet, but will expire within the given threshold days."""
        near_expiry = []
        for item in self.inventory.values():
            days_left = item.days_until_expiration()
            if 0 < days_left <= threshold_days:
                near_expiry.append(item)
        return near_expiry

# TESTING THE SYSTEM
if __name__ == "__main__":
    manager = HospitalInventoryManager()

    # Adding mock hospital supplies with mixed dates
    # Note: Dates are set relative to mid-2026
    manager.add_material(MedicalMaterial("M001", "Amoxicillin 500mg", "B-77A1", 120, "2025-12-10"))  # Expired
    manager.add_material(MedicalMaterial("M002", "Surgical Gloves (Size M)", "B-99X2", 500, "2028-08-15")) # Safe
    manager.add_material(MedicalMaterial("M003", "Sterile Gauze Pads", "B-11C9", 250, "2026-06-05"))     # Near Expiry (~18 days away)
    manager.add_material(MedicalMaterial("M004", "Propofol Injection", "B-4CD2", 45, "2026-02-14"))      # Expired

    print(f"--- Current Date Evaluation: {date.today()} ---\n")

    # Fetching completely expired/outdated materials
    print(" OUTDATED / EXPIRED MATERIALS NEEDING IMMEDIATE DISPOSAL:")
    outdated_list = manager.get_outdated_materials()
    if outdated_list:
        for item in outdated_list:
            print(f"   {item}")
    else:
        print("  No outdated materials found.")

    print("\n" + "="*60 + "\n")

    #  Fetching items nearing expiration (within 30 days) to prevent waste
    print(" ALERT: MATERIALS NEARING EXPIRATION (WITHIN 30 DAYS):")
    near_expiry_list = manager.get_near_expiry_materials(threshold_days=30)
    if near_expiry_list:
        for item in near_expiry_list:
            print(f"   {item}")
    else:
        print("  No items are nearing expiration within the threshold.")