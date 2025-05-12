import streamlit as st
from models.item import Item
from models.perishable import PerishableItem
from models.inventory import Inventory

st.set_page_config(page_title="Inventory Pro", page_icon="📦", layout="wide")

if 'inventory' not in st.session_state:
    st.session_state.inventory = Inventory()

inventory = st.session_state.inventory

menu = [
    "➕ Add Item",
    "🌿 Add Perishable Item",
    "➖ Remove Item",
    "📊 View Inventory",
    "💰 Inventory Value"
]
choice = st.sidebar.selectbox("Navigation", menu)

st.title("🛍️ Inventory Management Pro")
st.markdown("Manage your stock easily with real-time updates.")
st.markdown("---")

if choice == "➕ Add Item":
    st.subheader("Add a New Item")
    with st.form("add_form"):
        name = st.text_input("Item Name")
        price = st.number_input("Price (PKR)", min_value=0.01, format="%.2f")
        quantity = st.number_input("Quantity", min_value=1)
        submit = st.form_submit_button("Add Item")
    if submit:
        if name:
            item = Item(name, price, quantity)
            result = inventory.add_item(item)
            if result == "added":
                st.success(f"✅ '{name}' added to inventory.")
            else:
                st.info(f"🔄 '{name}' updated in inventory.")
        else:
            st.warning("⚠️ Name field cannot be empty.")

elif choice == "🌿 Add Perishable Item":
    st.subheader("Add a Perishable Item")
    with st.form("add_perishable_form"):
        name = st.text_input("Item Name")
        price = st.number_input("Price (PKR)", min_value=0.01, format="%.2f")
        quantity = st.number_input("Quantity", min_value=1)
        expiry = st.date_input("Expiry Date")
        submit = st.form_submit_button("Add Perishable Item")
    if submit:
        if name:
            item = PerishableItem(name, price, quantity, expiry.strftime("%Y-%m-%d"))
            result = inventory.add_item(item)
            if result == "added":
                st.success(f"✅ Perishable item '{name}' added.")
            else:
                st.info(f"🔄 '{name}' updated.")
        else:
            st.warning("⚠️ Name field cannot be empty.")

elif choice == "➖ Remove Item":
    st.subheader("Remove an Item")
    if not inventory.items:
        st.info("Inventory is empty.")
    else:
        item_names = [item.name for item in inventory.items]
        selected = st.selectbox("Select item to remove", item_names)
        if st.button("❌ Remove"):
            inventory.remove_item(selected)
            st.success(f"'{selected}' removed from inventory.")
            st.rerun()  # Updated method to rerun app safely

elif choice == "📊 View Inventory":
    st.subheader("Inventory Overview")
    if inventory.items:
        table = []
        for item in inventory.items:
            table.append({
                "Name": item.name,
                "Price (PKR)": item.price,
                "Quantity": item.quantity,
                "Expiry Date": getattr(item, 'expiry_date', 'N/A'),
                "Total Value (PKR)": item.get_value()
            })
        st.dataframe(table, use_container_width=True)
    else:
        st.info("No items to display.")

elif choice == "💰 Inventory Value":
    st.subheader("Total Inventory Value")
    total_value = inventory.get_total_value()
    st.metric(label="Total Stock Worth (PKR)", value=f"{total_value:.2f}")

st.sidebar.markdown("---")
st.sidebar.info("📦 Developed by Riaz Hussain | Inventory Pro v1.1")
