import tkinter as tk
import os
import subprocess

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Convenience Store - Menu")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (500/2)
        y = (screen_height/2) - (400/2)
        self.geometry('500x400+'+ str(int(x))+ '+' +str(int(y)))
        self.resizable(False,False)
        self.configure(bg="#f0f0f0")

        tk.Label(self, text="Convenience Store System",
                 font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=30)

        tk.Button(self, text="📦 Product Entry", font=("Arial", 12), width=20,
                  bg="#1E90FF", fg="white", command=self.open_entry).pack(pady=10)

        tk.Button(self, text="🛒 Purchase Items", font=("Arial", 12), width=20,
                  bg="#16A085", fg="white", command=self.open_purchase).pack(pady=10)

        tk.Button(self, text="📑 Sold List", font=("Arial", 12), width=20,
                  bg="#E67E22", fg="white", command=self.open_soldlist).pack(pady=10)

        tk.Button(self, text="❌ Exit", font=("Courier", 12), width=20,
                  bg="#C0392B", fg="white", command=self.Close).pack(pady=10)

   
    def Close(self):
        self.destroy()
    def open_entry(self):
        subprocess.Popen(["py", os.path.join(os.path.dirname(__file__), "Entry.py")])

    def open_purchase(self):
        subprocess.Popen(["py", os.path.join(os.path.dirname(__file__), "Purchase.py")])

    def open_soldlist(self):
        subprocess.Popen(["py", os.path.join(os.path.dirname(__file__), "Sold_list.py")])


if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
