import tkinter as tk
from tkmacosx import Button  # For enhanced button design
from tkinter import PhotoImage
import random
import string


# Function to generate password
def generate_password():
    try:
        global generated_password  # Make password accessible to the copy function
        length = int(length_entry.get())
        include_uppercase = uppercase_var.get()
        include_numbers = numbers_var.get()
        include_special = special_var.get()

        # Define character pools
        lowercase = string.ascii_lowercase
        characters = lowercase

        if include_uppercase:
            characters += string.ascii_uppercase
        if include_numbers:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        # Ensure at least one character from each selected category
        password = []
        if include_uppercase:
            password.append(random.choice(string.ascii_uppercase))
        if include_numbers:
            password.append(random.choice(string.digits))
        if include_special:
            password.append(random.choice(string.punctuation))

        # Fill remaining characters randomly
        remaining_length = length - len(password)
        if remaining_length > 0:
            password += random.choices(characters, k=remaining_length)

        # Shuffle and display password
        random.shuffle(password)
        generated_password = ''.join(password)
        result_label.config(text="Generated Password: " + generated_password, fg="#2E7D32")
    except ValueError:
        result_label.config(text="Please enter a valid number for length.", fg="#D32F2F")


# Function to copy password to clipboard
def copy_to_clipboard():
    try:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        root.update()  # Ensures clipboard content is updated
        result_label.config(text="Password copied to clipboard!", fg="#1976D2")
    except NameError:
        result_label.config(text="No password to copy! Please generate one.", fg="#D32F2F")


# Hover effect for buttons
def on_enter(e):
    e.widget['bg'] = '#2E7D32'
    e.widget['fg'] = 'white'


def on_leave(e):
    e.widget['bg'] = '#4CAF50'
    e.widget['fg'] = 'white'


# Create the main window
root = tk.Tk()
root.title("Password Genie - Your Key to Secure Passwords")
root.geometry("450x450")
root.iconphoto(True, PhotoImage(file='/Users/subhamrakshit/Desktop/coding/GUI/pass-generator-tkinter/pass-gen-icon.png'))
root.configure(bg="#F8F9FA")

# Title label
title_label = tk.Label(
    root, text="Password Genie", font=("Helvetica", 26, "bold"), bg="#F8F9FA", fg="#1E88E5"
)
title_label.pack(pady=10)

# Content frame for better alignment
content_frame = tk.Frame(root, bg="#F8F9FA")
content_frame.pack(padx=20, pady=10, fill="x")

# Password length input
length_label = tk.Label(
    content_frame, text="Password Length:", font=("Helvetica", 14), bg="#F8F9FA", fg="#333333", anchor="w"
)
length_label.grid(row=0, column=0, pady=5, sticky="w")
length_entry = tk.Entry(content_frame, font=("Helvetica", 14), width=10, bg="#E3F2FD", fg="#333333", relief="solid")
length_entry.grid(row=0, column=1, pady=5, padx=10)

# Uppercase option
uppercase_var = tk.BooleanVar()
uppercase_label = tk.Label(
    content_frame, text="Include Uppercase Letters?", font=("Helvetica", 14), bg="#F8F9FA", fg="#333333", anchor="w"
)
uppercase_label.grid(row=1, column=0, pady=5, sticky="w")
uppercase_yes = tk.Radiobutton(
    content_frame, text="Yes", variable=uppercase_var, value=True, font=("Helvetica", 12), bg="#F8F9FA", fg="#333333",
    activebackground="#F8F9FA", activeforeground="#1E88E5"
)
uppercase_no = tk.Radiobutton(
    content_frame, text="No", variable=uppercase_var, value=False, font=("Helvetica", 12), bg="#F8F9FA", fg="#333333",
    activebackground="#F8F9FA", activeforeground="#D32F2F"
)
uppercase_yes.grid(row=1, column=1, sticky="w", padx=10)
uppercase_no.grid(row=1, column=2, sticky="w")

# Numbers option
numbers_var = tk.BooleanVar()
numbers_label = tk.Label(
    content_frame, text="Include Numbers?", font=("Helvetica", 14), bg="#F8F9FA", fg="#333333", anchor="w"
)
numbers_label.grid(row=2, column=0, pady=5, sticky="w")
numbers_yes = tk.Radiobutton(
    content_frame, text="Yes", variable=numbers_var, value=True, font=("Helvetica", 12), bg="#F8F9FA", fg="#333333",
    activebackground="#F8F9FA", activeforeground="#1E88E5"
)
numbers_no = tk.Radiobutton(
    content_frame, text="No", variable=numbers_var, value=False, font=("Helvetica", 12), bg="#F8F9FA", fg="#333333",
    activebackground="#F8F9FA", activeforeground="#D32F2F"
)
numbers_yes.grid(row=2, column=1, sticky="w", padx=10)
numbers_no.grid(row=2, column=2, sticky="w")

# Special characters option
special_var = tk.BooleanVar()
special_label = tk.Label(
    content_frame, text="Include Special Characters?", font=("Helvetica", 14), bg="#F8F9FA", fg="#333333", anchor="w"
)
special_label.grid(row=3, column=0, pady=5, sticky="w")
special_yes = tk.Radiobutton(
    content_frame, text="Yes", variable=special_var, value=True, font=("Helvetica", 12), bg="#F8F9FA", fg="#333333",
    activebackground="#F8F9FA", activeforeground="#1E88E5"
)
special_no = tk.Radiobutton(
    content_frame, text="No", variable=special_var, value=False, font=("Helvetica", 12), bg="#F8F9FA", fg="#333333",
    activebackground="#F8F9FA", activeforeground="#D32F2F"
)
special_yes.grid(row=3, column=1, sticky="w", padx=10)
special_no.grid(row=3, column=2, sticky="w")

# Button frame for alignment
button_frame = tk.Frame(root, bg="#F8F9FA")
button_frame.pack(pady=20)

# Generate Password button
generate_button = Button(
    button_frame,
    text="Generate Password",
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 14),
    activebackground="#388E3C",
    activeforeground="white",
    command=generate_password,
    borderless=True,
)
generate_button.grid(row=0, column=0, padx=10)

# Copy to Clipboard button
copy_button = Button(
    button_frame,
    text="Copy to Clipboard",
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 14),
    activebackground="#388E3C",
    activeforeground="white",
    command=copy_to_clipboard,
    borderless=True,
)
copy_button.grid(row=0, column=1, padx=10)

# Add hover effects to buttons
generate_button.bind("<Return>", on_enter)
generate_button.bind("<Leave>", on_leave)
copy_button.bind("<Return>", on_enter)
copy_button.bind("<Leave>", on_leave)

# Result display label
result_label = tk.Label(
    root, text="", font=("Helvetica", 14, "italic"), bg="#F8F9FA", fg="#444444", wraplength=400, justify="center"
)
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
