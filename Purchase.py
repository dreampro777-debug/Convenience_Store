import tkinter as tk
from tkinter import ttk, messagebox
from SQL_connect import *

def load_products():
    for row in tree.get_children():
        tree.delete(row)

    rows = select_query("SELECT product_id, name, price, stock FROM products")
    for row in rows:
        tree.insert("", tk.END, values=row)

def make_purchase():
    try:
        selected = tree.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a product!")
            return

        product_id, name, price, stock = tree.item(selected[0], "values")
        qty = int(entry_qty.get())

        if qty <= 0:
            messagebox.showerror("Error", "Quantity must be positive!")
            return

        if qty > int(stock):
            messagebox.showerror("Error", "Not enough stock!")
            return

        sale_id = generate_id("sales", "S", "sale_id")
        total_price = int(price) * qty

        # Insert into sales
        sql_sale = f"INSERT INTO sales (sale_id, total_amount) VALUES ('{sale_id}', {total_price})"
        execute_query(sql_sale)

        # Insert into sale_items
        sql_item = f"""
            INSERT INTO sale_items (sale_id, product_id, quantity, price)
            VALUES ('{sale_id}', '{product_id}', {qty}, {int(price)})
        """
        execute_query(sql_item)

        # Update stock
        sql_stock = f"UPDATE products SET stock = stock - {qty} WHERE product_id = '{product_id}'"
        execute_query(sql_stock)

        messagebox.showinfo("Success", f"✅ Purchase complete!\nSale ID: {sale_id}\nTotal: {total_price}\n(Thank you for purchasing!)")
        load_products()

    except Exception as e:
        messagebox.showerror("Error", "Invalid keyword occured!")


root = tk.Tk()
root.title("Available items")
root.geometry('1000x350')
root.configure(bg='#31473A')

tree = ttk.Treeview(root, columns=("ID", "Name", "Price", "Stock"), show="headings")
for col in ("ID", "Name", "Price", "Stock"):
    tree.heading(col, text=col)
tree.pack(pady=10)

frame = tk.Frame(root)
frame.pack()
frame.configure(bg='#31473A')

tk.Label(frame, text="Quantity:").grid(row=0, column=0)
entry_qty = tk.Entry(frame)
entry_qty.grid(row=0, column=1)

tk.Button(frame, text="Buy", command=make_purchase,width=10,bg='black',fg='white',borderwidth=3.5).grid(row=0, column=2, padx=10)



load_products()
root.mainloop()
