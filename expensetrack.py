import tkinter as tk
from tkinter import ttk, messagebox

expenses = []
budget = 0


BG_COLOR = "#121212"       
CARD_COLOR = "#1e1e1e"     
ACCENT = "#4cc9f0"         
TEXT_COLOR = "#ffffff"     
BTN_HOVER = "#3a86ff"      


def set_budget():
    def save_budget():
        global budget
        try:
            budget = int(budget_entry.get())
            messagebox.showinfo("Success", "Budget set successfully!")
            budget_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")

    budget_window = tk.Toplevel(root)
    budget_window.title("Set Budget")
    budget_window.configure(bg=CARD_COLOR)
    ttk.Label(budget_window, text="Enter Monthly Budget:", background=CARD_COLOR, foreground=TEXT_COLOR).pack(pady=10)
    budget_entry = ttk.Entry(budget_window)
    budget_entry.pack(pady=5)
    ttk.Button(budget_window, text="Save", command=save_budget).pack(pady=10)


def add_expense():
    def save_expense():
        try:
            amount = int(amount_entry.get())
            place = place_entry.get()
            date = date_entry.get()
            expenses.append({"amount": amount, "place": place, "date": date})
            messagebox.showinfo("Success", "Expense recorded!")
            expense_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Enter valid amount")

    expense_window = tk.Toplevel(root)
    expense_window.title("Add Expense")
    expense_window.configure(bg=CARD_COLOR)
    ttk.Label(expense_window, text="Amount:", background=CARD_COLOR, foreground=TEXT_COLOR).pack(pady=5)
    amount_entry = ttk.Entry(expense_window)
    amount_entry.pack(pady=5)
    ttk.Label(expense_window, text="Place:", background=CARD_COLOR, foreground=TEXT_COLOR).pack(pady=5)
    place_entry = ttk.Entry(expense_window)
    place_entry.pack(pady=5)
    ttk.Label(expense_window, text="Date (DD-MM-YYYY):", background=CARD_COLOR, foreground=TEXT_COLOR).pack(pady=5)
    date_entry = ttk.Entry(expense_window)
    date_entry.pack(pady=5)
    ttk.Button(expense_window, text="Save", command=save_expense).pack(pady=10)


def view_expenses():
    if not expenses:
        messagebox.showinfo("Info", "No expenses recorded yet!")
        return
    exp_window = tk.Toplevel(root)
    exp_window.title("All Expenses")
    exp_window.configure(bg=CARD_COLOR)
    tree = ttk.Treeview(exp_window, columns=("Date", "Place", "Amount"), show="headings", height=10)
    tree.heading("Date", text="Date")
    tree.heading("Place", text="Place")
    tree.heading("Amount", text="Amount")

    
    for i, exp in enumerate(expenses):
        tag = "even" if i % 2 == 0 else "odd"
        tree.insert("", tk.END, values=(exp["date"], exp["place"], exp["amount"]), tags=(tag,))
    tree.tag_configure("even", background="#2a2a2a", foreground=TEXT_COLOR)
    tree.tag_configure("odd", background="#333333", foreground=TEXT_COLOR)
    tree.pack(fill=tk.BOTH, expand=True)


def show_summary():
    if not expenses:
        messagebox.showinfo("Info", "No expenses recorded yet!")
        return
    total_spent = sum(exp["amount"] for exp in expenses)
    remaining = budget - total_spent
    summary_window = tk.Toplevel(root)
    summary_window.title("Summary")
    summary_window.configure(bg=CARD_COLOR)

    ttk.Label(summary_window, text=f"Monthly Budget: {budget}", background=CARD_COLOR, foreground=ACCENT, font=("Arial", 12, "bold")).pack(pady=5)
    ttk.Label(summary_window, text=f"Total Spent: {total_spent}", background=CARD_COLOR, foreground="#ff6b6b", font=("Arial", 12, "bold")).pack(pady=5)
    ttk.Label(summary_window, text=f"Remaining: {remaining}", background=CARD_COLOR, foreground="#06d6a0", font=("Arial", 12, "bold")).pack(pady=5)


root = tk.Tk()
root.title("Expense Tracker")
root.geometry("520x420")
root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=12, relief="flat", background=ACCENT, foreground="black", font=("Arial", 11, "bold"))
style.map("TButton", background=[("active", BTN_HOVER)])
style.configure("TLabel", background=BG_COLOR, foreground=TEXT_COLOR)

title = tk.Label(root, text="💰 Expense Tracker", font=("Arial", 20, "bold"), fg=ACCENT, bg=BG_COLOR)
title.pack(pady=20)

ttk.Button(root, text="Set Budget", command=set_budget).pack(pady=10, fill="x", padx=60)
ttk.Button(root, text="Add Expense", command=add_expense).pack(pady=10, fill="x", padx=60)
ttk.Button(root, text="View Expenses", command=view_expenses).pack(pady=10, fill="x", padx=60)
ttk.Button(root, text="Show Summary", command=show_summary).pack(pady=10, fill="x", padx=60)
ttk.Button(root, text="Exit", command=root.destroy).pack(pady=15, fill="x", padx=60)

root.mainloop()
