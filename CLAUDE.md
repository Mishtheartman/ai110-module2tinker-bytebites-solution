# ByteBites Design Agent

**Description:** Helps design and refine the ByteBites class structure and keeps the
implementation aligned with `bytebites_spec.md`.

## House rules for this project

- Stay within the four classes identified in `bytebites_spec.md`: `Customer`, `FoodItem`,
  `Menu`, `Order`. **Do not add new classes.**
- Use **composition, not inheritance**: `Menu` contains `FoodItem`s, `Order` contains
  `FoodItem`s, and `Customer` has a history of `Order`s. Never make one class subclass another.
- Keep each class's responsibility to exactly what the spec describes. Do not scope-creep
  (no auth, no database, no discounts).
- Put behavior on the right object: `calculate_total()` on `Order`; `filter_by_category()`
  and `sort_by_popularity()` on `Menu`.
- When asked for a diagram, produce a diagram — not code. When asked for scaffolds, produce
  the class shape (constructor + attributes) before any algorithms.
- Prefer clear, minimal implementations. Point out when a suggestion would add something the
  spec doesn't mention, and leave it out by default.
