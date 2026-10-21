import tkinter as tk
from tkinter import messagebox
import secrets
import string


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4 or length > 128:
            messagebox.showerror(
                "Invalid Length",
                "Please enter a length between 4 and 128."
            )
            return

        characters = ""

        if uppercase_var.get():
            characters += string.ascii_uppercase

        if lowercase_var.get():
            characters += string.ascii_lowercase

        if numbers_var.get():
            characters += string.digits

        if symbols_var.get():
            characters += "!@#$%^&*()-_=+?"

        if not characters:
            messagebox.showwarning(
                "Select Options",
                "Please select at least one character type."
            )
            return

        required = []

        if uppercase_var.get():
            required.append(secrets.choice(string.ascii_uppercase))

        if lowercase_var.get():
            required.append(secrets.choice(string.ascii_lowercase))

        if numbers_var.get():
            required.append(secrets.choice(string.digits))

        if symbols_var.get():
            required.append(secrets.choice("!@#$%^&*()-_=+?"))

        remaining = [
            secrets.choice(characters)
            for _ in range(length - len(required))
        ]

        password_chars = required + remaining
        secrets.SystemRandom().shuffle(password_chars)

        password = "".join(password_chars)

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

        strength_label.config(
            text=f"Password Length: {length}",
            fg="#15803D"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )


def copy_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard!"
    )


def clear_password():
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")
    strength_label.config(text="Your password will appear here.")


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x560")
root.resizable(False, False)
root.configure(bg="#F1F5F9")

title = tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 20, "bold"),
    bg="#F1F5F9",
    fg="#1E293B"
)
title.pack(pady=(25, 8))

subtitle = tk.Label(
    root,
    text="Create a secure random password",
    font=("Arial", 11),
    bg="#F1F5F9",
    fg="#64748B"
)
subtitle.pack(pady=(0, 20))

length_label = tk.Label(
    root,
    text="Password Length (4–128)",
    font=("Arial", 11, "bold"),
    bg="#F1F5F9",
    fg="#334155"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center",
    width=15
)
length_entry.insert(0, "12")
length_entry.pack(pady=8)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

options_frame = tk.Frame(root, bg="#F1F5F9")
options_frame.pack(pady=10)

tk.Checkbutton(
    options_frame,
    text="Uppercase (A-Z)",
    variable=uppercase_var,
    bg="#F1F5F9",
    font=("Arial", 10)
).grid(row=0, column=0, sticky="w", padx=10, pady=5)

tk.Checkbutton(
    options_frame,
    text="Lowercase (a-z)",
    variable=lowercase_var,
    bg="#F1F5F9",
    font=("Arial", 10)
).grid(row=0, column=1, sticky="w", padx=10, pady=5)

tk.Checkbutton(
    options_frame,
    text="Numbers (0-9)",
    variable=numbers_var,
    bg="#F1F5F9",
    font=("Arial", 10)
).grid(row=1, column=0, sticky="w", padx=10, pady=5)

tk.Checkbutton(
    options_frame,
    text="Symbols (!@#$)",
    variable=symbols_var,
    bg="#F1F5F9",
    font=("Arial", 10)
).grid(row=1, column=1, sticky="w", padx=10, pady=5)

generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=10,
    cursor="hand2"
)
generate_button.pack(pady=15)

password_entry = tk.Entry(
    root,
    font=("Consolas", 12),
    justify="center",
    width=35,
    state="readonly"
)
password_entry.pack(pady=5, ipady=5)

strength_label = tk.Label(
    root,
    text="Your password will appear here.",
    font=("Arial", 10),
    bg="#F1F5F9",
    fg="#64748B"
)
strength_label.pack(pady=8)

button_frame = tk.Frame(root, bg="#F1F5F9")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 10, "bold"),
    bg="#15803D",
    fg="white",
    relief="flat",
    padx=12,
    pady=8,
    cursor="hand2"
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_password,
    font=("Arial", 10, "bold"),
    bg="#64748B",
    fg="white",
    relief="flat",
    padx=18,
    pady=8,
    cursor="hand2"
).grid(row=0, column=1, padx=8)

footer = tk.Label(
    root,
    text="Built with Python and Tkinter",
    font=("Arial", 9),
    bg="#F1F5F9",
    fg="#94A3B8"
)
footer.pack(side="bottom", pady=15)

root.mainloop()
