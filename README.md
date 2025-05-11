# 📦 Inventory Management System – Python OOP Project

This is a modular, menu-driven **Inventory Management System** built in Python using Object-Oriented Programming principles. The project is designed to demonstrate concepts like **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction** in a real-world application.

---

## 📁 Project Structure

```

INVENTORY\_MANAGEMENT/
│
├── .venv/                     # Virtual environment (managed by uv)
│
├── models/                   # Core object models
│   ├── **init**.py
│   ├── inventory.py          # Inventory class (handles item storage and logic)
│   ├── item.py               # Item base class
│   └── perishable.py         # PerishableItem class (extends Item)
│
├── utils/                    # Utilities and user interface
│   └── cli.py                # CLI-based MainApp logic
│
├── main.py                   # Main entry point for the application
├── pyproject.toml            # Project dependencies and config (for uv)
├── uv.lock                   # Locked dependency versions
├── .python-version           # Python version used
└── README.md                 # Project documentation (this file)

````

---

## 🚀 Features

- Add regular and perishable items
- Remove items from the inventory
- View detailed list of all items
- Calculate total value of inventory
- Show expiry date for perishable items
- User-friendly CLI interface

---

## 🧠 OOP Concepts Implemented

| Principle      | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Encapsulation** | Item data is private and accessed via getter methods                       |
| **Inheritance**   | PerishableItem inherits from Item and extends its behavior                 |
| **Polymorphism**  | `get_info()` behaves differently for each class                            |
| **Abstraction**   | All business logic is separated into classes (`Inventory`, `Item`, etc.)   |
| **Composition**   | MainApp uses Inventory, which stores a collection of Items                 |

---

## 💻 How to Run

### If using `uv`:
```bash
uv init
uv run main.py
````

### Or with standard Python:

```bash
python main.py
```

---

## 📟 Sample Output (CLI)

```
=== INVENTORY MANAGEMENT SYSTEM ===
1. Add Item
2. Add Perishable Item
3. Remove Item
4. Show All Items
5. Show Total Inventory Value
6. Exit
Enter your choice: 1
Enter item name: Sugar
Enter price (PKR): 85
Enter quantity: 25
Item added successfully.
```

---

## ✨ Example: Perishable Item Class

```python
class PerishableItem(Item):
    def __init__(self, name, price, quantity, expiry_date):
        super().__init__(name, price, quantity)
        self.__expiry_date = expiry_date

    def get_info(self):
        return f"{super().get_info()}, Expiry Date: {self.__expiry_date}"
```

This class shows **inheritance** (from `Item`) and **polymorphism** (overriding `get_info()`).

---

## 🔧 Future Enhancements

* Save/load data to JSON or CSV files
* GUI using Tkinter or PyQt
* Alerts for expired items
* User login and authentication
* Search and filter functionality

---

## 👤 Author

**Riaz Hussain**
Project developed for OOP Viva | May 2025
Python 3.x | UV-based modular architecture

## 📜 License

This project is released for educational and learning purposes only.

