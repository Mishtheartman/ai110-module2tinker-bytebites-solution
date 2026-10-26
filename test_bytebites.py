"""Tests for the ByteBites classes in models.py."""

from models import Customer, FoodItem, Menu, Order


def make_menu():
    """Build a small menu with items in several categories."""
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 8.50, "Burgers", 4.5))
    menu.add_item(FoodItem("Large Soda", 2.10, "Drinks", 4.0))
    menu.add_item(FoodItem("Iced Tea", 1.20, "Drinks", 3.8))
    menu.add_item(FoodItem("Cheesecake", 4.00, "Desserts", 4.8, is_available=False))
    return menu


def test_filter_returns_only_matching_category():
    menu = make_menu()
    drinks = menu.filter_by_category("Drinks")
    assert [item.name for item in drinks] == ["Large Soda", "Iced Tea"]
    assert all(item.category == "Drinks" for item in drinks)


def test_filter_keeps_menu_order():
    menu = make_menu()
    drinks = menu.filter_by_category("Drinks")
    assert drinks[0].name == "Large Soda"
    assert drinks[1].name == "Iced Tea"


def test_filter_unknown_category_returns_empty_list():
    menu = make_menu()
    assert menu.filter_by_category("Salads") == []


def test_filter_on_empty_menu_returns_empty_list():
    assert Menu().filter_by_category("Drinks") == []


def test_filter_is_case_sensitive():
    menu = make_menu()
    assert menu.filter_by_category("drinks") == []


def test_filter_includes_unavailable_items():
    menu = make_menu()
    desserts = menu.filter_by_category("Desserts")
    assert [item.name for item in desserts] == ["Cheesecake"]


def test_filter_does_not_change_menu():
    menu = make_menu()
    menu.filter_by_category("Drinks")
    assert len(menu.items) == 4


def test_removed_item_is_not_in_filter():
    menu = make_menu()
    soda = menu.filter_by_category("Drinks")[0]
    menu.remove_item(soda)
    assert [item.name for item in menu.filter_by_category("Drinks")] == ["Iced Tea"]
"""Behavior tests for ByteBites models.

Each test checks one behavior from the outside (inputs -> outputs),
not how the code is written. Until the classes are implemented, these
fail with NotImplementedError; that is expected.
"""

import pytest

from models import Customer, FoodItem, Menu, Order


# ---------- Fixtures ----------

@pytest.fixture
def burger():
    return FoodItem("Spicy Burger", 10.00, "Burgers")


@pytest.fixture
def soda():
    return FoodItem("Large Soda", 5.00, "Drinks")


@pytest.fixture
def sold_out_fries():
    return FoodItem("Fries", 3.00, "Sides", is_available=False)


@pytest.fixture
def customer():
    return Customer("Alex")


@pytest.fixture
def order(customer):
    return Order(customer)


@pytest.fixture
def menu(burger, soda):
    m = Menu()
    m.add_item(burger)
    m.add_item(soda)
    return m


# ---------- Order: happy path ----------

def test_calculate_total_with_multiple_items(order, burger, soda):
    order.add_item(burger)
    order.add_item(soda)
    assert order.calculate_total() == pytest.approx(15.00)


def test_add_available_item_to_order(order, burger):
    assert order.add_item(burger) is True
    assert burger in order.selected_items


def test_total_cost_updates_after_adding_item(order, burger, soda):
    order.add_item(burger)
    assert order.total_cost == pytest.approx(10.00)
    order.add_item(soda)
    assert order.total_cost == pytest.approx(15.00)


# ---------- Order: edge cases ----------

def test_order_total_is_zero_when_empty(order):
    assert order.calculate_total() == 0


def test_unavailable_item_is_rejected(order, sold_out_fries):
    assert order.add_item(sold_out_fries) is False
    assert sold_out_fries not in order.selected_items


def test_total_ignores_rejected_items(order, burger, sold_out_fries):
    order.add_item(burger)
    order.add_item(sold_out_fries)
    assert order.calculate_total() == pytest.approx(10.00)


def test_same_item_added_twice_counts_twice(order, soda):
    order.add_item(soda)
    order.add_item(soda)
    assert order.calculate_total() == pytest.approx(10.00)


def test_orders_have_unique_ids(customer):
    assert Order(customer).order_id != Order(customer).order_id


# ---------- Menu: happy path ----------

def test_add_item_appears_in_menu(burger):
    menu = Menu()
    menu.add_item(burger)
    assert burger in menu.items


def test_filter_by_category_returns_only_matching_items(menu, burger, soda):
    drinks = menu.filter_by_category("Drinks")
    assert drinks == [soda]
    assert burger not in drinks


def test_remove_item_no_longer_in_menu(menu, burger):
    menu.remove_item(burger)
    assert burger not in menu.items


# ---------- Menu: edge cases ----------

def test_filter_with_no_matches_returns_empty_list(menu):
    assert menu.filter_by_category("Desserts") == []


def test_filter_on_empty_menu_returns_empty_list():
    assert Menu().filter_by_category("Drinks") == []


# ---------- Customer ----------

def test_new_customer_has_empty_history(customer):
    assert customer.purchase_history == []


def test_completed_order_added_to_history(customer, order):
    customer.add_completed_order(order)
    assert order in customer.purchase_history


def test_unfinished_order_not_in_history(customer, order):
    assert order not in customer.purchase_history


def test_history_holds_multiple_orders_in_completion_order(customer):
    first, second = Order(customer), Order(customer)
    customer.add_completed_order(first)
    customer.add_completed_order(second)
    assert customer.purchase_history == [first, second]


def test_customers_have_unique_ids():
    assert Customer("Sam").customer_id != Customer("Sam").customer_id


# ---------- FoodItem ----------

def test_new_food_item_is_available_by_default(burger):
    assert burger.is_available is True