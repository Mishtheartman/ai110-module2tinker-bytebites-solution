# ByteBites — First AI Draft (standard chat, BEFORE the custom agent)

This is the *unrefined* first diagram from a standard chat session, kept only so it can be
compared against the verified `bytebites_design.md`. **It contains deliberate mistakes** — the
kind an unconstrained AI assistant tends to produce. Do not build from this file.

## Classes (as first generated — NOT correct)

### Customer
- name: str
- purchase_history: list
- discount_history: list        ← out of scope; the spec never mentions discounts

### FoodItem(Menu)                ← WRONG: inheritance. A FoodItem is not a kind of Menu.
- name, price, category, popularity_rating

### Menu
- items: list

### MenuManager                   ← unnecessary extra class; Menu already owns the catalog
- Methods: add_item(), filter_by_category(), sort_by_popularity()

### Order
- items: list
- Methods: calculate_total()

## What was wrong (and fixed in `bytebites_design.md`)

1. `FoodItem(Menu)` — inheritance where composition belongs. A `Menu` *contains* `FoodItem`s.
2. `MenuManager` — scope creep; folded its methods back into `Menu`.
3. `discount_history` on `Customer` — not in the spec; removed.

Refining the prompt with the custom agent (see `CLAUDE.md`) — which forbids extra classes and
inheritance — produced the corrected four-class, composition-only design.
