import tkinter as tk
from tkinter import scrolledtext
from prettytable import PrettyTable
from SQL_connect import *

def show_sales():
    rows = select_query("""
        SELECT s.sale_id, s.date, p.name, si.quantity, si.price, (si.quantity * si.price) as total
        FROM sales s
        JOIN sale_items si ON s.sale_id = si.sale_id
        JOIN products p ON si.product_id = p.product_id
        ORDER BY s.sale_id DESC
    """)

    table = PrettyTable(["Sale ID", "Date", "Product", "Qty", "Price", "Total"])
    for row in rows:
        table.add_row(row)

    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, str(table))


root = tk.Tk()
root.title("Sales History - Inventory System")
root.configure(bg='#E3867D')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (700/2)
y = (screen_height/2) - (375/2)
root.geometry('700x375+'+ str(int(x))+ '+' +str(int(y)))
root.resizable(False,False)

btn = tk.Button(root, text="Load Sales History", command=show_sales)
btn.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, width=100, height=20)
text_area.pack()

root.mainloop()
