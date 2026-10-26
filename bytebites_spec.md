# "Candidate Classes
## Client Feature Request
We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

## 1. Customer
Stores customer information, including their name and past purchase history. It can also help verify whether a customer is a registered user.

**Attributes:**
- `customer_id` - Unique identifier for each customer.
- `name` - Customer's name.
- `purchase_history` - List of the customer's past orders.

## 2. FoodItem
Represents an individual food or drink product, such as a Spicy Burger or Large Soda.

**Attributes:**
- `name` - Name of the food item.
- `price` - Cost of the item.
- `category` - Category, such as Drinks, Burgers, or Desserts.
- `popularity_rating` - Rating that represents the item's popularity.
- `is_available` - Indicates whether the item is available for purchase.

## 3. Menu
Manages the collection of food items available in the ByteBites app.

**Attributes:**
- `items` - List of all available food items.

**Methods:**
- `add_item()` - Adds a food item to the menu.
- `remove_item()` - Removes a food item from the menu.
- `filter_by_category()` - Filters items by category.
- `display_items()` - Displays the available food items.

## 4. Order
Represents a customer's transaction and calculates the total cost of the selected items.

**Attributes:**
- `order_id` - Unique identifier for each order.
- `customer` - Customer who placed the order.
- `selected_items` - List of food items in the order.
- `total_cost` - Total price of the selected items.
- `order_date` - Date and time the order was placed.

**Methods:**
- `add_item()` - Adds a food item to the order.
- `calculate_total()` - Calculates the total cost of the order.

---

## Suggested Class Relationships

- A `Customer` can have multiple `Order` objects.
- A `Menu` contains multiple `FoodItem` objects.
- An `Order` contains one or more `FoodItem` objects.
- An `Order` calculates its total using the prices of its selected items.

## Design Suggestions

- Give every customer and order a unique ID.
- Keep menu management separate from order processing.
- Check that food items are available before adding them to an order.
- Calculate the order total from the current selected items rather than relying on a manually entered total.
- Store purchase history through completed orders to avoid duplicating customer data.
