import tkinter as tk
from tkinter import messagebox
import re
def assess_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_char_error]
    score = 5 - sum(errors)
    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"
    feedback = []
    if length_error:
        feedback.append("• At least 8 characters long")
    if lowercase_error:
        feedback.append("• Include lowercase letters")
    if uppercase_error:
        feedback.append("• Include uppercase letters")
    if digit_error:
        feedback.append("• Include numbers")
    if special_char_error:
        feedback.append("• Include special characters (!@#$%...)")
    return strength, feedback
def check_password():
    password = entry.get()
    strength, suggestions = assess_password_strength(password)
    result_label.config(text=f"Strength: {strength}", fg="green" if "Strong" in strength else "orange" if "Moderate" in strength else "red")
    feedback_text.delete("1.0", tk.END)
    if suggestions:
        feedback_text.insert(tk.END, "Suggestions:\n" + "\n".join(suggestions))
def exit_app():
    root.destroy()
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()
check_button = tk.Button(root, text="Check Strength", command=check_password, font=("Arial", 11))
check_button.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()
feedback_text = tk.Text(root, height=5, width=40, font=("Arial", 10))
feedback_text.pack(pady=5)
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)
root.mainloop()