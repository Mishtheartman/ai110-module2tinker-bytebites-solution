"""
pytest suite for the ByteBites models.

Run with:  python -m pytest
"""

from models import Customer, FoodItem, Menu, Order


def _sample_menu() -> Menu:
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 8.50, "Mains", 4.7))
    menu.add_item(FoodItem("Large Soda", 2.00, "Drinks", 3.9))
    menu.add_item(FoodItem("Iced Coffee", 3.50, "Drinks", 4.8))
    menu.add_item(FoodItem("Brownie", 2.75, "Desserts", 4.2))
    return menu


def test_calculate_total_with_multiple_items():
    order = Order()
    order.add_item(FoodItem("Spicy Burger", 8.50, "Mains", 4.7))
    order.add_item(FoodItem("Large Soda", 2.00, "Drinks", 3.9))
    assert order.calculate_total() == 10.50


def test_order_total_is_zero_when_empty():
    order = Order()
    assert order.calculate_total() == 0.0


def test_filter_by_category():
    menu = _sample_menu()
    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 2
    assert all(item.category == "Drinks" for item in drinks)


def test_filter_by_category_is_case_insensitive():
    menu = _sample_menu()
    assert len(menu.filter_by_category("drinks")) == 2


def test_filter_by_missing_category_returns_empty():
    menu = _sample_menu()
    assert menu.filter_by_category("Sushi") == []


def test_sort_by_popularity_orders_descending():
    menu = _sample_menu()
    ordered = menu.sort_by_popularity()
    ratings = [item.popularity_rating for item in ordered]
    assert ratings == sorted(ratings, reverse=True)
    assert ordered[0].name == "Iced Coffee"  # highest rating (4.8)


def test_customer_records_order_history():
    customer = Customer("Alex")
    assert customer.purchase_history == []
    order = Order()
    order.add_item(FoodItem("Brownie", 2.75, "Desserts", 4.2))
    customer.add_order(order)
    assert len(customer.purchase_history) == 1


def test_customers_do_not_share_history():
    # Guards against a mutable-default-argument bug.
    a = Customer("A")
    b = Customer("B")
    a.add_order(Order())
    assert len(a.purchase_history) == 1
    assert len(b.purchase_history) == 0
