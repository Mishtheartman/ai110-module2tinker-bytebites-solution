# ByteBites Spec

## Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to manage our customers,
tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we
must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and
lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction
object should store the selected items and compute the total cost.

## Candidate Classes

Four nouns carry the data this system needs to model:

1. **Customer** — a real user; tracks `name` and `purchase_history` (past orders).
2. **FoodItem** — one sellable item; tracks `name`, `price`, `category`, `popularity_rating`.
3. **Menu** — the full catalog; holds all `FoodItem`s and can filter by category / sort by popularity.
4. **Order** — a single transaction; holds the selected `FoodItem`s and computes the total cost.
