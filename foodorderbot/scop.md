### Deciding the Scope

1. It should be able to greet the user dynamically.
2. It should be to understand the menu items and their quantity reuested.
3. Chatbot should be able to place an order on the user's behalf.
4. Give the user the status of the order when asked.


#### Listing Intents

Default welcome intent: when the user messages the chatbot
• Place order intent: when the user asks the bot to order food
• Item description intent: when the user tells what item and quantity 
they want
• Order status: when the user wants to know his order status
• Order_ID: the bot needs to understand the user’s order ID for 
tracking.
• User thanks: when the user thanks the bot

#### Listing Entities

• food_items: what food does the user want to order?
• quantities: what is the quantity of the food item the user is willing to order?
• order_id: order_id of the place order for user