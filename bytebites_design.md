# ByteBites System Design

The verified UML-style class diagram. Four classes, related by **composition**
(has-a / contains), never inheritance (is-a).

## Classes

### Customer
- name: str
- purchase_history: list[Order]
- Methods: add_order(order)

### FoodItem
- name: str
- price: float
- category: str
- popularity_rating: float

### Menu
- items: list[FoodItem]
- Methods: add_item(item), filter_by_category(category), sort_by_popularity()

### Order
- items: list[FoodItem]
- Methods: add_item(item), calculate_total()

## Relationships

- `Menu` **contains** `FoodItem` objects (composition).
- `Order` **contains** `FoodItem` objects (composition).
- `Customer` **has** a `purchase_history` of `Order` objects (composition).

## Diagram (textual UML)

```
Customer ───has──▶ Order ───contains──▶ FoodItem ◀──contains─── Menu
  - name              - items              - name          - items
  - purchase_history  + add_item()         - price         + add_item()
  + add_order()       + calculate_total()  - category      + filter_by_category()
                                           - popularity    + sort_by_popularity()
```

## Design notes (things the AI suggested that were rejected)

- A `MenuManager` class was proposed — removed. `Menu` already owns the catalog;
  `MenuManager` had no responsibility the spec describes.
- An early draft had `FoodItem` inheriting from `Menu`. That's an is-a error:
  a FoodItem is not a kind of Menu — a Menu *contains* FoodItems. Changed to
  composition.
- A `discount_history` attribute on `Customer` was suggested — removed as out of
  scope (the spec mentions no discounts).
