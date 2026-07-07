# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described
in the spec.

## Behavioral Instructions
<!-- Example behavioral instructions used to constrain the AI assistant for this project. -->
- Stay within the four classes in `bytebites_spec.md`: `Customer`, `FoodItem`, `Menu`, `Order`.
  Do not invent new classes (no `MenuManager`, `Cart`, `Payment`, etc.).
- Use **composition, not inheritance**. `Menu` and `Order` each hold a list of `FoodItem`
  objects; `Customer` holds a list of `Order` objects. No class should subclass another.
- Only add attributes and methods that the spec calls for. If the spec doesn't mention it
  (discounts, ratings history, auth), leave it out.
- Assign responsibilities to the right class: `calculate_total()` belongs to `Order`;
  `filter_by_category()` and `sort_by_popularity()` belong to `Menu`.
- Prefer small, readable methods over clever one-liners. Return new lists from sort/filter
  rather than mutating `self.items` in place.
