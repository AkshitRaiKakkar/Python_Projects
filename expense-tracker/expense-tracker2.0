import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

budget = np.array([])
dat = np.array([])
area = np.array([])
expen = np.array([])

BG = "#121212"
FG = "#e0e0e0"
ACCENT = "#00bcd4"
BTN1 = "#1abc9c"
BTN2 = "#e67e22"
BTN3 = "#e74c3c"
BTN4 = "#9b59b6"
BTN5 = "#3498db"

def add_budget():
    try:
        b = int(budget_entry.get())
        global budget
        if len(budget) == 0:
            budget = np.append(budget, b)
            messagebox.showinfo("Success", f"Monthly budget set to {b}")
        else:
            messagebox.showwarning("Warning", "Budget already set!")
    except:
        messagebox.showerror("Error", "Enter a valid number")

def add_expense():
    try:
        d = date_entry.get()
        p = place_entry.get()
        e = int(expense_entry.get())
        global dat, area, expen
        dat = np.append(dat, d)
        area = np.append(area, p)
        expen = np.append(expen, e)
        tree.insert("", "end", values=(d, p, e))
        date_entry.delete(0, tk.END)
        place_entry.delete(0, tk.END)
        expense_entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Enter valid expense details")

def show_balance():
    if len(budget) == 0:
        messagebox.showerror("Error", "Set budget first!")
        return
    spent = np.sum(expen)
    remaining = budget[0] - spent
    messagebox.showinfo("Balance", f"Total Spent: {spent}\nRemaining: {remaining}")

def show_high():
    if len(expen) == 0:
        messagebox.showinfo("Info", "No expenses recorded yet")
        return
    idx = np.argmax(expen)
    messagebox.showinfo("Highest Expense", f"{expen[idx]} on {dat[idx]} at {area[idx]}")

def show_low():
    if len(expen) == 0:
        messagebox.showinfo("Info", "No expenses recorded yet")
        return
    idx = np.argmin(expen)
    messagebox.showinfo("Lowest Expense", f"{expen[idx]} on {dat[idx]} at {area[idx]}")

def show_avg():
    if len(expen) == 0:
        messagebox.showinfo("Info", "No expenses recorded yet")
        return
    avg = round(np.mean(expen), 2)
    messagebox.showinfo("Average Expense", f"Average Expense: {avg}")

def show_summary():
    if len(budget) == 0:
        messagebox.showerror("Error", "Set budget first!")
        return
    if len(expen) == 0:
        messagebox.showinfo("Summary", f"Budget: {budget[0]}\nNo expenses yet.")
        return
    spent = np.sum(expen)
    remaining = budget[0] - spent
    msg = f"""
    📑 Monthly Summary
    ------------------------
    Total Budget: {budget[0]}
    Total Spent: {spent}
    Remaining: {remaining}
    Number of Expenses: {len(expen)}
    Average Expense: {round(np.mean(expen),2)}
    Median Expense: {np.median(expen)}
    Std Deviation: {round(np.std(expen),2)}
    """
    messagebox.showinfo("Summary", msg)

root = tk.Tk()
root.title("Expense Tracker - Dark Mode")
root.geometry("750x550")
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background=BG, fieldbackground=BG, foreground=FG, rowheight=25)
style.map("Treeview", background=[("selected", ACCENT)], foreground=[("selected", "black")])

title = tk.Label(root, text="💰 Monthly Expense Tracker 💰", font=("Arial", 20, "bold"), bg=BG, fg=ACCENT)
title.pack(pady=10)

frame1 = tk.Frame(root, bg=BG)
frame1.pack(pady=5)

tk.Label(frame1, text="Budget:", bg=BG, fg=FG).grid(row=0, column=0, padx=5)
budget_entry = tk.Entry(frame1, bg="#1e1e1e", fg=FG, insertbackground="white")
budget_entry.grid(row=0, column=1, padx=5)
tk.Button(frame1, text="Set Budget", command=add_budget, bg=BTN1, fg="white", activebackground=ACCENT).grid(row=0, column=2, padx=5)

tk.Label(frame1, text="Date:", bg=BG, fg=FG).grid(row=1, column=0, padx=5)
date_entry = tk.Entry(frame1, bg="#1e1e1e", fg=FG, insertbackground="white")
date_entry.grid(row=1, column=1, padx=5)

tk.Label(frame1, text="Place:", bg=BG, fg=FG).grid(row=2, column=0, padx=5)
place_entry = tk.Entry(frame1, bg="#1e1e1e", fg=FG, insertbackground="white")
place_entry.grid(row=2, column=1, padx=5)

tk.Label(frame1, text="Expense:", bg=BG, fg=FG).grid(row=3, column=0, padx=5)
expense_entry = tk.Entry(frame1, bg="#1e1e1e", fg=FG, insertbackground="white")
expense_entry.grid(row=3, column=1, padx=5)

tk.Button(frame1, text="Add Expense", command=add_expense, bg=BTN5, fg="white", activebackground=ACCENT).grid(row=4, column=1, pady=10)

tree = ttk.Treeview(root, columns=("Date", "Place", "Expense"), show="headings", height=10)
tree.heading("Date", text="Date")
tree.heading("Place", text="Place")
tree.heading("Expense", text="Expense")
tree.pack(pady=10, fill="x", padx=20)

frame2 = tk.Frame(root, bg=BG)
frame2.pack(pady=10)

tk.Button(frame2, text="Balance", command=show_balance, bg=BTN2, fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame2, text="Highest", command=show_high, bg=BTN3, fg="white").grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame2, text="Lowest", command=show_low, bg=BTN1, fg="white").grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame2, text="Average", command=show_avg, bg=BTN4, fg="white").grid(row=0, column=3, padx=5, pady=5)
tk.Button(frame2, text="Summary", command=show_summary, bg=BTN5, fg="white").grid(row=0, column=4, padx=5, pady=5)

root.mainloop()
