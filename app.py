import streamlit as st
import pandas as pd

# Define an expanded list of items for the vacation rental
items = [
    {"category": "Cleaning Supplies", "item": "Dishwashing Soap", "price": 3.00, "description": "Liquid soap for dishes"},
    {"category": "Cleaning Supplies", "item": "Toilet Paper (4-pack)", "price": 2.50, "description": "4 rolls of toilet paper"},
    {"category": "Cleaning Supplies", "item": "Paper Towels (2-pack)", "price": 3.50, "description": "2 rolls of paper towels"},
    {"category": "Cleaning Supplies", "item": "Trash Bags (20-pack)", "price": 6.00, "description": "20 heavy-duty trash bags"},
    {"category": "Cleaning Supplies", "item": "Multi-Surface Cleaner", "price": 4.50, "description": "Multi-surface cleaner spray"},
    {"category": "Cleaning Supplies", "item": "Glass Cleaner", "price": 3.00, "description": "Cleaner for windows and mirrors"},
    {"category": "Cleaning Supplies", "item": "Scrub Sponges (5-pack)", "price": 2.00, "description": "5-pack of scrub sponges"},
    {"category": "Cleaning Supplies", "item": "Broom and Dustpan Set", "price": 12.00, "description": "Broom with dustpan"},
    {"category": "Cleaning Supplies", "item": "Mop and Bucket Set", "price": 15.00, "description": "Mop with bucket"},
    
    {"category": "Bathroom Essentials", "item": "Hand Soap", "price": 1.50, "description": "Gentle hand soap"},
    {"category": "Bathroom Essentials", "item": "Shampoo", "price": 4.00, "description": "Travel-sized shampoo bottles"},
    {"category": "Bathroom Essentials", "item": "Conditioner", "price": 4.00, "description": "Travel-sized conditioner bottles"},
    {"category": "Bathroom Essentials", "item": "Body Wash", "price": 3.00, "description": "Travel-sized body wash"},
    {"category": "Bathroom Essentials", "item": "Bath Towels (2-pack)", "price": 10.00, "description": "2 soft bath towels"},
    {"category": "Bathroom Essentials", "item": "Hand Towels (4-pack)", "price": 8.00, "description": "4-pack of hand towels"},
    {"category": "Bathroom Essentials", "item": "Toothbrush Holders", "price": 5.00, "description": "Set of toothbrush holders"},
    {"category": "Bathroom Essentials", "item": "Toilet Brush Set", "price": 6.00, "description": "Brush with holder for toilet cleaning"},
    
    {"category": "Laundry Supplies", "item": "Laundry Detergent", "price": 10.00, "description": "1-gallon bottle of detergent"},
    {"category": "Laundry Supplies", "item": "Fabric Softener", "price": 8.00, "description": "1-gallon bottle of fabric softener"},
    {"category": "Laundry Supplies", "item": "Dryer Sheets (100-pack)", "price": 5.00, "description": "100-pack of dryer sheets"},
    {"category": "Laundry Supplies", "item": "Stain Remover Spray", "price": 3.00, "description": "Spray for removing stains"},
    
    {"category": "Kitchen Essentials", "item": "Dish Sponge", "price": 1.20, "description": "Non-scratch dish sponge"},
    {"category": "Kitchen Essentials", "item": "Dish Soap", "price": 2.00, "description": "Liquid soap for dishes"},
    {"category": "Kitchen Essentials", "item": "Trash Bags (Large)", "price": 4.50, "description": "Large trash bags for kitchen use"},
    {"category": "Kitchen Essentials", "item": "Coffee Filters", "price": 2.50, "description": "Pack of 100 coffee filters"},
    {"category": "Kitchen Essentials", "item": "Aluminum Foil", "price": 3.00, "description": "Roll of aluminum foil"},
    {"category": "Kitchen Essentials", "item": "Plastic Wrap", "price": 2.50, "description": "Roll of plastic wrap"},
    {"category": "Kitchen Essentials", "item": "Cooking Oil", "price": 4.00, "description": "Bottle of cooking oil"},
    
    {"category": "Pantry Items", "item": "Salt", "price": 1.00, "description": "1 lb of table salt"},
    {"category": "Pantry Items", "item": "Pepper", "price": 1.00, "description": "1 lb of ground pepper"},
    {"category": "Pantry Items", "item": "Coffee", "price": 7.00, "description": "1 lb of ground coffee"},
    {"category": "Pantry Items", "item": "Tea Bags (20-pack)", "price": 2.00, "description": "20 tea bags"},
    {"category": "Pantry Items", "item": "Sugar", "price": 2.00, "description": "1 lb of granulated sugar"},
    {"category": "Pantry Items", "item": "Olive Oil", "price": 6.00, "description": "Bottle of olive oil"},
    
    {"category": "Linens", "item": "Bed Sheets (Queen)", "price": 25.00, "description": "Set of queen bed sheets"},
    {"category": "Linens", "item": "Pillowcases (4-pack)", "price": 10.00, "description": "4 standard pillowcases"},
    {"category": "Linens", "item": "Blanket (Queen)", "price": 30.00, "description": "Queen-sized blanket"},
    {"category": "Linens", "item": "Mattress Protector (Queen)", "price": 20.00, "description": "Waterproof mattress protector"},
    {"category": "Linens", "item": "Pillows (2-pack)", "price": 15.00, "description": "2 standard-sized pillows"},
    
    {"category": "Miscellaneous", "item": "Batteries (AA 12-pack)", "price": 6.00, "description": "12-pack of AA batteries"},
    {"category": "Miscellaneous", "item": "Flashlight", "price": 5.00, "description": "Handheld flashlight"},
    {"category": "Miscellaneous", "item": "First Aid Kit", "price": 12.00, "description": "Basic first aid kit"},
    {"category": "Miscellaneous", "item": "Umbrella", "price": 7.00, "description": "Compact umbrella for guests"},
    {"category": "Miscellaneous", "item": "Sewing Kit", "price": 3.00, "description": "Mini sewing kit"},
]

# Convert items to DataFrame for easier handling
items_df = pd.DataFrame(items)

# App title
st.title("Vacation Rental Bulk Ordering System")

# Instructions
st.write("Select items in bulk for your vacation rental business and set up recurring orders.")

# Set up order frequency options
order_frequency = st.selectbox("Order Frequency", ["One-Time", "Weekly", "Monthly", "Quarterly"])

# Bulk discounts
st.sidebar.title("Discounts")
st.sidebar.write("10% discount on orders of 50+ units of a single item")
st.sidebar.write("15% discount on orders of 100+ units of a single item")

# Display each item with checkboxes and quantity selectors
selected_items = []
for category in items_df["category"].unique():
    st.header(category)
    category_items = items_df[items_df["category"] == category]
    for i, item in category_items.iterrows():
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            selected = st.checkbox(f"{item['item']} (${item['price']:.2f} each) - {item['description']}", key=f"item_{i}")
        with col2:
            if selected:
                quantity = st.number_input("Quantity", min_value=0, value=1, step=1, key=f"quantity_{i}")
                
                # Bulk discount logic
                price_per_unit = item["price"]
                if quantity >= 100:
                    price_per_unit *= 0.85  # 15% discount
                elif quantity >= 50:
                    price_per_unit *= 0.90  # 10% discount

                total_price = price_per_unit * quantity
                selected_items.append({
                    "category": item["category"],
                    "item": item["item"],
                    "unit_price": item["price"],
                    "discounted_price": price_per_unit,
                    "quantity": quantity,
                    "total_price": total_price
                })

# Order summary
if selected_items:
    selected_df = pd.DataFrame(selected_items)
    total_order_price = selected_df["total_price"].sum()
    st.write("### Order Summary")
    st.dataframe(selected_df[["category", "item", "unit_price", "discounted_price", "quantity", "total_price"]])
    st.write(f"**Total Price:** ${total_order_price:.2f}")

    # Order button
    if st.button("Place Order"):
        st.success("Order placed successfully!")
else:
    st.write("No items selected.")
