"""
ByteBites — backend models.

Four classes model the campus food-ordering domain described in
`bytebites_spec.md`:

  - Customer   : a real user, tracked by name and past orders.
  - FoodItem   : a single sellable item (name, price, category, popularity).
  - Menu       : the full catalog of FoodItems, with filter/sort helpers.
  - Order      : one transaction — the FoodItems a customer is buying now.

Relationships are composition, not inheritance: a Menu *contains* FoodItems,
an Order *contains* FoodItems, and a Customer *has* a history of Orders. No
class inherits from another. Scope is intentionally limited to the spec — no
authentication, database, or discount logic.
"""

from typing import List, Optional


class Customer:
    """A ByteBites user, identified by name and a history of past orders."""

    def __init__(self, name: str, purchase_history: Optional[List["Order"]] = None) -> None:
        self.name = name
        # Default to a fresh list rather than a shared mutable default argument.
        self.purchase_history: List["Order"] = (
            purchase_history if purchase_history is not None else []
        )

    def add_order(self, order: "Order") -> None:
        """Record a completed order in this customer's purchase history."""
        self.purchase_history.append(order)

    def __repr__(self) -> str:
        return f"Customer(name={self.name!r}, orders={len(self.purchase_history)})"


class FoodItem:
    """A single item on the menu."""

    def __init__(
        self,
        name: str,
        price: float,
        category: str,
        popularity_rating: float,
    ) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self) -> str:
        return (
            f"FoodItem(name={self.name!r}, price={self.price}, "
            f"category={self.category!r}, popularity={self.popularity_rating})"
        )


class Menu:
    """The full catalog of FoodItems the restaurant offers."""

    def __init__(self) -> None:
        self.items: List[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a FoodItem to the catalog."""
        self.items.append(item)

    def filter_by_category(self, category: str) -> List[FoodItem]:
        """Return only the items whose category matches (case-insensitive)."""
        target = category.strip().lower()
        return [item for item in self.items if item.category.strip().lower() == target]

    def sort_by_popularity(self) -> List[FoodItem]:
        """Return the items sorted by popularity_rating, most popular first.

        Returns a new list; the menu's own ordering is left unchanged.
        """
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Order:
    """A single transaction: the FoodItems a customer is buying right now."""

    def __init__(self) -> None:
        self.items: List[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a FoodItem to this order."""
        self.items.append(item)

    def calculate_total(self) -> float:
        """Return the sum of the prices of every item in the order (0.0 if empty)."""
        return sum(item.price for item in self.items)

    def __repr__(self) -> str:
        return f"Order(items={len(self.items)}, total={self.calculate_total()})"


if __name__ == "__main__":
    # A quick manual scenario exercising every class and method.
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 8.50, "Mains", 4.7))
    menu.add_item(FoodItem("Large Soda", 2.00, "Drinks", 3.9))
    menu.add_item(FoodItem("Iced Coffee", 3.50, "Drinks", 4.8))
    menu.add_item(FoodItem("Brownie", 2.75, "Desserts", 4.2))

    print("Drinks on the menu:")
    for item in menu.filter_by_category("Drinks"):
        print(f"  - {item.name} (${item.price:.2f})")

    print("\nMenu by popularity:")
    for item in menu.sort_by_popularity():
        print(f"  - {item.name} ({item.popularity_rating})")

    order = Order()
    order.add_item(menu.items[0])  # Spicy Burger
    order.add_item(menu.items[2])  # Iced Coffee
    print(f"\nOrder total: ${order.calculate_total():.2f}")

    alex = Customer("Alex")
    alex.add_order(order)
    print(f"{alex.name} now has {len(alex.purchase_history)} order(s) on file.")
