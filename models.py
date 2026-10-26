"""ByteBites: backend logic for a campus food ordering app.

- FoodItem: a menu product (name, price, category, popularity, availability).
- Menu: manages the collection of FoodItems (add, remove, filter, sort, display).
- Customer: a customer's ID, name, and history of completed orders.
- Order: one customer's transaction; only takes available items and always
  calculates its total from the selected items.

Scope: plain Python classes. No authentication, database layer, or
features beyond the spec.
"""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4


class FoodItem:
    """An individual food or drink product (e.g. Spicy Burger, Large Soda)."""

    def __init__(
        self,
        name: str,
        price: float,
        category: str,
        popularity_rating: float = 0.0,
        is_available: bool = True,
    ) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating
        self.is_available = is_available


class Menu:
    """Manages the collection of food items. Kept separate from order processing."""

    def __init__(self) -> None:
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the menu."""
        self.items.append(item)

    def remove_item(self, item: FoodItem) -> None:
        """Remove a food item from the menu (does nothing if it isn't there)."""
        if item in self.items:
            self.items.remove(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return items in the given category."""
        return [item for item in self.items if item.category == category]

    def sort_items(self, by: str = "price", descending: bool = False) -> list[FoodItem]:
        """Return items sorted by "price", "name", or "popularity_rating".

        Returns a new list; the menu's own order is not changed. Items with
        equal values keep their menu order.
        """
        if by not in ("price", "name", "popularity_rating"):
            raise ValueError(f"Cannot sort by {by!r}")
        return sorted(self.items, key=lambda item: getattr(item, by), reverse=descending)

    def display_items(self) -> None:
        """Display the available food items."""
        for item in self.items:
            if item.is_available:
                print(f"{item.name} ({item.category}) - ${item.price:.2f}")


class Customer:
    """Stores customer info; purchase history is built from completed orders."""

    def __init__(self, name: str) -> None:
        self.customer_id: str = str(uuid4())  # unique ID, never reused
        self.name = name
        self.purchase_history: list[Order] = []

    def is_registered(self) -> bool:
        """Check whether the customer is a registered user (no auth logic)."""
        return bool(self.customer_id)

    def add_completed_order(self, order: Order) -> None:
        """Record a completed order in the purchase history.

        Only orders placed by this customer are recorded, and each order
        is recorded once.
        """
        if order.customer is self and order not in self.purchase_history:
            self.purchase_history.append(order)


class Order:
    """A customer's transaction; the total is calculated from selected items."""

    def __init__(self, customer: Customer) -> None:
        self.order_id: str = str(uuid4())  # unique ID, never reused
        self.customer = customer
        self.selected_items: list[FoodItem] = []
        self.order_date: datetime = datetime.now()

    @property
    def total_cost(self) -> float:
        """Always derived from selected_items, never set manually."""
        return self.calculate_total()

    def add_item(self, item: FoodItem) -> bool:
        """Add an item if it is available; return whether it was added."""
        if not item.is_available:
            return False
        self.selected_items.append(item)
        return True

    def calculate_total(self) -> float:
        """Sum the prices of the current selected items."""
        return round(sum(item.price for item in self.selected_items), 2)

    def complete_order(self) -> bool:
        """Record the order in the customer's purchase history.

        Returns False (and records nothing) if the order is empty.
        """
        if not self.selected_items:
            return False
        self.customer.add_completed_order(self)
        return True


if __name__ == "__main__":
    # Quick demo so running this file shows the classes working.
    burger = FoodItem("Spicy Burger", 8.50, "Burgers", 4.5)
    soda = FoodItem("Large Soda", 2.10, "Drinks", 4.0)
    tea = FoodItem("Iced Tea", 1.20, "Drinks", 3.8)
    cake = FoodItem("Cheesecake", 4.00, "Desserts", 4.8, is_available=False)

    menu = Menu()
    for food in (burger, soda, tea, cake):
        menu.add_item(food)

    print("Menu (available items):")
    menu.display_items()
    print("Drinks:", [food.name for food in menu.filter_by_category("Drinks")])
    print("Cheapest first:", [food.name for food in menu.sort_items("price")])
    print("Most popular first:",
          [food.name for food in menu.sort_items("popularity_rating", descending=True)])

    customer = Customer("Ana")
    print(f"\nCustomer {customer.name} registered: {customer.is_registered()}")

    order = Order(customer)
    for food in (burger, soda, tea, cake):
        print(f"Add {food.name}: {order.add_item(food)}")
    print(f"Order total: ${order.total_cost:.2f}")

    print("Empty order completed:", Order(customer).complete_order())
    print("Order completed:", order.complete_order())
    print("Orders in purchase history:", len(customer.purchase_history))
