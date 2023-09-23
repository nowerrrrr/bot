import requests
import datetime
import time
import os
import tkinter as tk
from tkinter import messagebox

# Function to update the GitHub repository description
def update_github_description():
    # Retrieve user inputs from the GUI
    github_repo_url = github_repo_url_entry.get()
    github_access_token = github_access_token_entry.get()
    start_date = start_date_entry.get()
    special_message = special_message_entry.get()

    try:
        # Convert the start date input to a date object
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
        return

    # Calculate the number of days since the start date
    current_date = datetime.date.today()
    days_learning_python = (current_date - start_date).days

    # Construct the new GitHub repository description
    new_description = f"Day {days_learning_python}: {special_message}"

    # Send a request to update the GitHub repository description
    headers = {"Authorization": f"token {github_access_token}"}
    payload = {"description": new_description}
    response = requests.patch(github_repo_url, headers=headers, json=payload)

    if response.status_code == 200:
        messagebox.showinfo("Success", "GitHub description updated successfully.")
    else:
        messagebox.showerror("Error", f"Error updating GitHub description. Status code: {response.status_code}")

# Create the main application window
root = tk.Tk()
root.title("GitHub Description Updater")

# Create and arrange GUI elements
github_repo_url_label = tk.Label(root, text="GitHub Repository URL:")
github_repo_url_entry = tk.Entry(root, width=40)
github_access_token_label = tk.Label(root, text="GitHub Access Token:")
github_access_token_entry = tk.Entry(root, width=40)
start_date_label = tk.Label(root, text="Start Date (YYYY-MM-DD):")
start_date_entry = tk.Entry(root, width=15)
special_message_label = tk.Label(root, text="Special Message:")
special_message_entry = tk.Entry(root, width=40)
count_button = tk.Button(root, text="Count Up", command=update_github_description)

# Arrange elements using grid layout
github_repo_url_label.grid(row=0, column=0, sticky="w")
github_repo_url_entry.grid(row=0, column=1, columnspan=2)
github_access_token_label.grid(row=1, column=0, sticky="w")
github_access_token_entry.grid(row=1, column=1, columnspan=2)
start_date_label.grid(row=2, column=0, sticky="w")
start_date_entry.grid(row=2, column=1)
special_message_label.grid(row=3, column=0, sticky="w")
special_message_entry.grid(row=3, column=1, columnspan=2)
count_button.grid(row=4, column=1, pady=10)

# Start the GUI application
root.mainloop()
