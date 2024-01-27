import tkinter as tk
from tkinter import ttk, messagebox
import csv

class DataStorage:
    def __init__(self):
        self.data_sets = {}

    def add_data_set(self, name, data):
        self.data_sets[name] = data

    def delete_data_set(self, name):
        if name in self.data_sets:
            del self.data_sets[name]

    def search_data_set(self, name, key):
        if name in self.data_sets:
            return self.data_sets[name].get(key, "Not found")
        else:
            return "Data set not found"

class EmployeeDatabase:
    def __init__(self):
        self.employees = {}
        self.unique_id_counter = 1

    def add_employee(self, name, position, ssn, home_address, email, phone_numbers, skills):
        unique_id = self.unique_id_counter
        self.unique_id_counter += 1
        self.employees[unique_id] = {
            'name': name,
            'position': position,
            'ssn': ssn,
            'home_address': home_address,
            'email': email,
            'phone_numbers': phone_numbers,
            'skills': skills
        }
        return unique_id

    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        else:
            return False

def validate_ssn(ssn):
    # Add your SSN validation logic here
    pass

def validate_email(email):
    # Add your email validation logic here
    pass

def validate_order_number(order_number):
    # Add your order number validation logic here
    pass

def validate_product_id(product_id):
    # Add your product ID validation logic here
    pass

def validate_phone_number(phone_number):
    # Add your phone number validation logic here
    pass

class GUI(tk.Tk):
    def __init__(self, data_storage, employee_database):
        super().__init__()
        self.data_storage = data_storage
        self.employee_db = employee_database
        self.title("Employee Database App")

        # Create and place GUI components
        self.label = ttk.Label(self, text="Employee Database App")
        self.label.pack(pady=10)

        self.add_employee_button = ttk.Button(self, text="Add Employee", command=self.show_add_employee_window)
        self.add_employee_button.pack(pady=10)

        self.delete_employee_button = ttk.Button(self, text="Delete Employee", command=self.show_delete_employee_window)
        self.delete_employee_button.pack(pady=10)

        self.show_employees_button = ttk.Button(self, text="Show Employees", command=self.show_employees)
        self.show_employees_button.pack(pady=10)

    def show_add_employee_window(self):
        add_employee_window = tk.Toplevel(self)
        add_employee_window.title("Add Employee")

        # Create and place entry fields and labels
        ttk.Label(add_employee_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(add_employee_window, text="Position:").grid(row=1, column=0, padx=10, pady=5)
        ttk.Label(add_employee_window, text="SSN:").grid(row=2, column=0, padx=10, pady=5)
        ttk.Label(add_employee_window, text="Home Address:").grid(row=3, column=0, padx=10, pady=5)
        ttk.Label(add_employee_window, text="Email:").grid(row=4, column=0, padx=10, pady=5)
        ttk.Label(add_employee_window, text="Phone Numbers:").grid(row=5, column=0, padx=10, pady=5)
        ttk.Label(add_employee_window, text="Skills:").grid(row=6, column=0, padx=10, pady=5)

        name_entry = ttk.Entry(add_employee_window)
        position_entry = ttk.Entry(add_employee_window)
        ssn_entry = ttk.Entry(add_employee_window)
        home_address_entry = ttk.Entry(add_employee_window)
        email_entry = ttk.Entry(add_employee_window)
        phone_numbers_entry = ttk.Entry(add_employee_window)
        skills_entry = ttk.Entry(add_employee_window)

        name_entry.grid(row=0, column=1, padx=10, pady=5)
        position_entry.grid(row=1, column=1, padx=10, pady=5)
        ssn_entry.grid(row=2, column=1, padx=10, pady=5)
        home_address_entry.grid(row=3, column=1, padx=10, pady=5)
        email_entry.grid(row=4, column=1, padx=10, pady=5)
        phone_numbers_entry.grid(row=5, column=1, padx=10, pady=5)
        skills_entry.grid(row=6, column=1, padx=10, pady=5)

        add_button = ttk.Button(add_employee_window, text="Add", command=lambda: self.add_employee(
            name_entry.get(), position_entry.get(), ssn_entry.get(), home_address_entry.get(),
            email_entry.get(), phone_numbers_entry.get(), skills_entry.get(), add_employee_window))
        add_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_employee(self, name, position, ssn, home_address, email, phone_numbers, skills, window):
        # Validate fields (you may want to enhance the validation)
        if not name or not position or not ssn or not email:
            messagebox.showerror("Error", "Please fill in required fields.")
            return

        # Add employee to the database
        unique_id = self.employee_db.add_employee(name, position, ssn, home_address, email, phone_numbers.split(','), skills.split(','))

        # Display success message
        messagebox.showinfo("Success", f"Employee added successfully with ID: {unique_id}")

        # Close the add employee window
        window.destroy()

    def show_delete_employee_window(self):
        delete_employee_window = tk.Toplevel(self)
        delete_employee_window.title("Delete Employee")

        # Create and place entry field and label
        ttk.Label(delete_employee_window, text="Employee ID:").pack(pady=10)
        employee_id_entry = ttk.Entry(delete_employee_window)
        employee_id_entry.pack(pady=10)

        delete_button = ttk.Button(delete_employee_window, text="Delete", command=lambda: self.delete_employee(employee_id_entry.get(), delete_employee_window))
        delete_button.pack(pady=10)

    def delete_employee(self, employee_id, window):
        try:
            employee_id = int(employee_id)
        except ValueError:
            messagebox.showerror("Error", "Invalid Employee ID. Please enter a valid numeric ID.")
            return

        success = self.employee_db.delete_employee(employee_id)

        if success:
            messagebox.showinfo("Success", f"Employee with ID {employee_id} deleted successfully.")
        else:
            messagebox.showerror("Error", f"Employee with ID {employee_id} not found.")

        # Close the delete employee window
        window.destroy()

    def show_employees(self):
        employees_window = tk.Toplevel(self)
        employees_window.title("Employee List")

        # Create and place a text widget to display employee information
        employees_text = tk.Text(employees_window, height=10, width=50)
        employees_text.pack(padx=10, pady=10)

        # Display employee information in the text widget
        for employee_id, details in self.employee_db.employees.items():
            employees_text.insert(tk.END, f"Employee ID: {employee_id}\n")
            employees_text.insert(tk.END, f"Name: {details['name']}\n")
            employees_text.insert(tk.END, f"Position: {details['position']}\n")
            employees_text.insert(tk.END, f"SSN: {details['ssn']}\n")
            employees_text.insert(tk.END, f"Home Address: {details['home_address']}\n")
            employees_text.insert(tk.END, f"Email: {details['email']}\n")
            employees_text.insert(tk.END, f"Phone Numbers: {', '.join(details['phone_numbers'])}\n")
            employees_text.insert(tk.END, f"Skills: {', '.join(details['skills'])}\n\n")

if __name__ == "__main__":
    # Example usage:

    # Read and Parse CSV Files
    with open('orders.csv', 'r') as orders_file:
        orders_data = list(csv.reader(orders_file))

    with open('orders.csv', 'r') as order_details_file:
        order_details_data = list(csv.reader(order_details_file))

    # Store the data in an appropriate data structure
    data_storage = DataStorage()
    data_storage.add_data_set('orders', [])
    data_storage.add_data_set('order_details', [])

    # Create and add some sample employees to the Employee Database
    employee_db = EmployeeDatabase()
    employee_db.add_employee("John Doe", "Developer", "123-45-6789", "123 Main St", "john.doe@email.com", ["1234567890"], ["Python", "Java"])
    employee_db.add_employee("Jane Doe", "Designer", "987-65-4321", "456 Oak St", "jane.doe@email.com", ["9876543210"], ["Photoshop", "Illustrator"])

    # Create and run the GUI
    app = GUI(data_storage, employee_db)
    app.mainloop()
