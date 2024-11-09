import streamlit as st
import pandas as pd

# Define items for the rental
items = [
    {"item": "Dishwashing Soap", "price": 3.00},
    {"item": "Toilet Paper (4-pack)", "price": 2.50},
    {"item": "Paper Towels (2-pack)", "price": 3.50},
    {"item": "Hand Soap", "price": 1.50},
    {"item": "Shampoo", "price": 4.00},
    {"item": "Conditioner", "price": 4.00},
    {"item": "Body Wash", "price": 3.00},
    {"item": "Trash Bags (20-pack)", "price": 6.00},
    {"item": "Laundry Detergent", "price": 10.00},
    {"item": "Fabric Softener", "price": 5.00},
    {"item": "Dish Sponge", "price": 1.20},
    {"item": "Toilet Cleaner", "price": 2.75},
    {"item": "Disinfectant Wipes", "price": 4.50},
    {"item": "Cleaning Spray", "price": 3.25},
    {"item": "Mop and Bucket Set", "price": 20.00},
    {"item": "Dustpan and Brush", "price": 3.00},
    {"item": "Kitchen Towels (4-pack)", "price": 5.00},
    {"item": "Bathroom Towels (4-pack)", "price": 15.00},
    {"item": "Bed Sheets (Twin)", "price": 20.00},
    {"item": "Bed Sheets (Queen)", "price": 25.00},
    {"item": "Bed Sheets (King)", "price": 30.00},
    {"item": "Pillowcases (4-pack)", "price": 10.00},
    {"item": "Blanket", "price": 18.00},
    {"item": "Pillows (2-pack)", "price": 15.00},
    {"item": "Mattress Protector (Queen)", "price": 25.00},
    {"item": "Shower Curtain", "price": 7.50},
    {"item": "Bath Mat", "price": 5.00},
    {"item": "Toothbrushes (5-pack)", "price": 3.00},
    {"item": "Toothpaste (3-pack)", "price": 4.00},
    {"item": "Shower Gel (5-pack)", "price": 8.00},
    {"item": "First Aid Kit", "price": 12.00},
    {"item": "Flashlight", "price": 5.00},
    {"item": "Batteries (AA, 10-pack)", "price": 6.00},
    {"item": "Coffee Maker Filters (50-pack)", "price": 2.00},
    {"item": "Coffee", "price": 7.00},
    {"item": "Tea Bags (50-pack)", "price": 4.00},
    {"item": "Salt", "price": 1.00},
    {"item": "Pepper", "price": 1.00},
    {"item": "Olive Oil", "price": 6.00},
    {"item": "Pantry Snacks", "price": 10.00},
    {"item": "Water Bottles (24-pack)", "price": 8.00},
    {"item": "Wine Glasses (4-pack)", "price": 12.00},
    {"item": "Wine Opener", "price": 3.00},
    {"item": "Plates (set of 4)", "price": 10.00},
    {"item": "Cups (set of 4)", "price": 8.00},
    {"item": "Utensils Set (4-pack)", "price": 12.00},
    {"item": "Cutting Board", "price": 5.00},
    {"item": "Can Opener", "price": 2.50},
    {"item": "Garlic Press", "price": 3.00},
    {"item": "Cooking Pots Set", "price": 25.00},
]

# Convert items to DataFrame for easier handling
items_df = pd.DataFrame(items)

# App title
st.title("Vacation Rental Supply Ordering App")

# Instructions
st.write("Select the items you need to order in bulk for your vacation rental and specify the quantities.")

# Define an empty list to store selected items
selected_items = []

# Display each item with a checkbox and quantity selector
for i, item in items_df.iterrows():
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        selected = st.checkbox(f"{item['item']} (${item['price']:.2f} each)", key=f"item_{i}")
    with col2:
        if selected:
            quantity = st.number_input("Quantity", min_value=0, value=1, step=1, key=f"quantity_{i}")
            total_price = item["price"] * quantity
            selected_items.append({"item": item["item"], "price": item["price"], "quantity": quantity, "total_price": total_price})

# Calculate total order price
if selected_items:
    selected_df = pd.DataFrame(selected_items)
    total_order_price = selected_df["total_price"].sum()
    st.write("### Selected Items")
    st.table(selected_df[["item", "price", "quantity", "total_price"]])
    st.write(f"**Total Order Price:** ${total_order_price:.2f}")
else:
    st.write("No items selected.")

# Confirm order button
if st.button("Confirm Order"):
    if selected_items:
        st.success("Order confirmed! A summary of your order has been displayed above.")
    else:
        st.warning("Please select at least one item to order.")
