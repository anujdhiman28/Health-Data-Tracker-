import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        elif 25 <= bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obesity"
        status_label.config(text=f"Status: {status}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Setting up the main window
root = tk.Tk()
root.title("Health Data Tracker")
root.geometry("300x250")
root.configure(bg="#f0f8ff")

# Title label
title_label = tk.Label(root, text="Health Data Tracker", font=("Helvetica", 16), bg="#f0f8ff")
title_label.pack(pady=10)

# Input fields for weight and height
tk.Label(root, text="Weight (kg):", bg="#f0f8ff").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Height (cm):", bg="#f0f8ff").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white")
calculate_button.pack(pady=15)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f8ff")
result_label.pack(pady=5)

status_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f8ff")
status_label.pack(pady=5)

# Run the application
root.mainloop()
