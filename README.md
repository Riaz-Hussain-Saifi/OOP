# 🛍️ Inventory Management System – Streamlit & CLI (Python OOP Project)

**Developer:** Riaz Hussain  
**Project Type:** OOP + GUI  
**Date:** 12 May 2025

---

## 📦 Overview

This project is a beginner-friendly, modular inventory management system built in Python using Object-Oriented Programming principles. It includes:

- 🖥️ A CLI-based menu system (ideal for console practice)
- 🌐 A beautiful, responsive web interface built using **Streamlit**
- 🧠 Demonstrates **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction**
- 💡 Real-time inventory management for regular and perishable items

---

## 🗂️ Project Structure

```
Inventory_Management/
│
├── models/
│   ├── item.py              # Base Item class
│   ├── perishable.py        # Inherits from Item and adds expiry date
│   └── inventory.py         # Handles item add/remove/value logic
│
├── utils/
│   └── cli.py               # Command-line interface logic
│
├── streamlit_app.py         # Streamlit UI (modern, beautiful web app)
├── main.py                  # CLI entry point
├── requirements.txt         # Dependency list
└── README.md                # Project instructions
```

---

## 🚀 Features

- ➕ Add both **Regular** and **Perishable** items
- 🗑️ Remove items from the inventory
- 📄 View all items in a formatted list
- 💰 Show total value of current stock
- 📆 Track **expiry dates** for perishable products
- 📊 Live inventory table display in Streamlit
- 🎨 Modern, emoji-enhanced user interface

---

## ⚙️ OOP Concepts Demonstrated

| OOP Principle   | Usage                                                                 |
|----------------|------------------------------------------------------------------------|
| Encapsulation   | Internal item data hidden from direct access                         |
| Inheritance     | `PerishableItem` inherits from `Item`                                |
| Polymorphism    | `get_info()` behaves differently for regular vs. perishable items    |
| Abstraction     | Logic separated into dedicated classes like `Inventory`, `Item`      |
| Composition     | `MainApp` uses `Inventory` which contains `Item` instances           |

---

## 🧰 Setup Instructions

### ▶️ Option 1: Standard Python

```bash
uv add -r requirements.txt
```

If you get a `typing_extensions` error:

```bash
uv add typing_extensions
```

---

## 🖥️ Run the CLI App

```bash
uv run main.py
```

You will interact with a numbered menu for inventory management.

---

## 🌐 Run the Streamlit App (GUI)

```bash
streamlit run streamlit_app.py
```

Then open the browser at the link shown in terminal to use the web interface.

---

## 🔍 Sample CLI Output

```
=== INVENTORY MANAGEMENT SYSTEM ===
1. Add Item
2. Add Perishable Item
3. Remove Item
4. Show All Items
5. Show Total Inventory Value
6. Exit
```

---

## 🔧 Planned Enhancements

- Save/load inventory from file (CSV or JSON)
- Notifications for expiring items
- Search bar and filter functionality in UI
- Add item categories
- Multi-user support

---

## 👨‍💻 Author

**Riaz Hussain**  
Python Developer – GIAIC Quarter 3 Assignment  
Email: *[infosaifideveloper@gmail.com]*

---

## 📜 License

This project is released for academic and educational use only.
