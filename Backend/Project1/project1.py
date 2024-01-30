import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog,Button
import csv

global FILEPATH
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

class OrdersDatabase:
    def __init__(self):
        self.orderss = {}
        self.unique_id_counter = 1



    def add_orders(self, customerID, bookID, bookName, quantity, orderDate, totalAmount, shippingAddress):
        unique_id = self.unique_id_counter
        self.unique_id_counter += 1
        self.orderss[unique_id] = {
            'customerID': customerID,
            'bookID': bookID,
            'bookName': bookName,
            'quantity': quantity,
            'orderDate': orderDate,
            'totalAmount': totalAmount,
            'shippingAddress': shippingAddress
        }
        return unique_id

    def delete_orders(self, orders_id):
        if orders_id in self.orderss:
            del self.orderss[orders_id]
            return True
        else:
            return False

def validate_customerID(customerID):
    # Add your customerID validation logic here
    pass

def validate_bookID(bookID):
    # Add your bookID validation logic here
    pass

def validate_bookName(bookName):
    # Add your bookName validation logic here
    pass

def validate_quantity(quantity):
    # Add your quantity validation logic here
    pass

def validate_orderDate(orderDate):
    # Add your phone number validation logic here
    pass

class GUI(tk.Tk):
    def __init__(self, data_storage, orders_database):
        super().__init__()
        self.data_storage = data_storage
        self.orders_db = orders_database
        self.title("Orders Database App")

        # Create and place GUI components
        self.label = ttk.Label(self, text="Orders Database App" ,
              font=("Bodoni MT Black", 25), background="aquamarine" )
        self.label.pack(pady=10)

        self.add_orders_button = ttk.Button(self, text="Add Orders", command=self.show_add_orders_window)
        self.add_orders_button.pack(pady=10)

        self.delete_orders_button = ttk.Button(self, text="Delete Orders", command=self.show_delete_orders_window)
        self.delete_orders_button.pack(pady=10)

        self.show_orderss_button = ttk.Button(self, text="Show Orders", command=self.show_orderss)
        self.show_orderss_button.pack(pady=10)

    def show_add_orders_window(self):
        add_orders_window = tk.Toplevel(self)
        add_orders_window.title("Add Orders")

        # Create and place entry fields and labels
        ttk.Label(add_orders_window, text="CustomerID:").grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(add_orders_window, text="BookID:").grid(row=1, column=0, padx=10, pady=5)
        ttk.Label(add_orders_window, text="BookName:").grid(row=2, column=0, padx=10, pady=5)
        ttk.Label(add_orders_window, text="Quantity:").grid(row=3, column=0, padx=10, pady=5)
        ttk.Label(add_orders_window, text="OrderDate:").grid(row=4, column=0, padx=10, pady=5)
        ttk.Label(add_orders_window, text="TotalAmount:").grid(row=5, column=0, padx=10, pady=5)
        ttk.Label(add_orders_window, text="ShippingAddress:").grid(row=6, column=0, padx=10, pady=5)

        customerID_entry = ttk.Entry(add_orders_window)
        bookID_entry = ttk.Entry(add_orders_window)
        bookName_entry = ttk.Entry(add_orders_window)
        quantity_entry = ttk.Entry(add_orders_window)
        orderDate_entry = ttk.Entry(add_orders_window)
        totalAmount_entry = ttk.Entry(add_orders_window)
        shippingAddress_entry = ttk.Entry(add_orders_window)

        customerID_entry.grid(row=0, column=1, padx=10, pady=5)
        bookID_entry.grid(row=1, column=1, padx=10, pady=5)
        bookName_entry.grid(row=2, column=1, padx=10, pady=5)
        quantity_entry.grid(row=3, column=1, padx=10, pady=5)
        orderDate_entry.grid(row=4, column=1, padx=10, pady=5)
        totalAmount_entry.grid(row=5, column=1, padx=10, pady=5)
        shippingAddress_entry.grid(row=6, column=1, padx=10, pady=5)

        add_button = ttk.Button(add_orders_window, text="Add", command=lambda: self.add_orders(
                    customerID_entry.get(),
                    bookID_entry.get(),
                    bookName_entry.get(),
                    quantity_entry.get(),
                    orderDate_entry.get(),
                    totalAmount_entry.get(),
                    shippingAddress_entry.get()
                   )
                )
        add_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_orders(self, customerID, bookID, bookName, quantity, orderDate, totalAmount, shippingAddress):
        # Validate fields (you may want to enhance the validation)
        if not bookName or not customerID or not bookID or not orderDate:
            messagebox.showerror("Error", "Please fill in required fields.")
            return

        # Add Orders to the database
        unique_id = self.orders_db.add_orders(customerID, bookID, bookName, quantity, orderDate, totalAmount, shippingAddress)

        # Display success message
        messagebox.showinfo("Success", f"Orders added successfully with ID: {unique_id}")

    def show_delete_orders_window(self):
        delete_orders_window = tk.Toplevel(self)
        delete_orders_window.title("Delete Orders")

        # Create and place entry field and label
        ttk.Label(delete_orders_window, text="Orders ID:").pack(pady=10)
        orders_id_entry = ttk.Entry(delete_orders_window)
        orders_id_entry.pack(pady=10)

        delete_button = ttk.Button(delete_orders_window, text="Delete", command=lambda: self.delete_orders(orders_id_entry.get(), delete_orders_window))
        delete_button.pack(pady=10)

    def delete_orders(self, orders_id, window):
        try:
            orders_id = int(orders_id)
        except ValueError:
            messagebox.showerror("Error", "Invalid Orders ID. Please enter a valid numeric ID.")
            return

        success = self.orders_db.delete_orders(orders_id)

        if success:
            messagebox.showinfo("Success", f"Orders with ID {orders_id} deleted successfully.")
        else:
            messagebox.showerror("Error", f"Orders with ID {orders_id} not found.")

        # Close the delete Orders window
        window.destroy()

    def show_orderss(self):
        orderss_window = tk.Toplevel(self)
        orderss_window.title("Orders List")

        # Create and place a text widget to display Orders information
        orderss_text = tk.Text(orderss_window, height=10, width=50)
        orderss_text.pack(padx=10, pady=10)

        # Display Orders information in the text widget
        for orders_id, details in self.orders_db.orderss.items():
            orderss_text.insert(tk.END, f"Orders ID: {orders_id}\n")
            orderss_text.insert(tk.END, f"CustomerID: {details['customerID']}\n")
            orderss_text.insert(tk.END, f"BookID: {details['bookID']}\n")
            orderss_text.insert(tk.END, f"BookName: {details['bookName']}\n")
            orderss_text.insert(tk.END, f"Quantity: {details['quantity']}\n")
            orderss_text.insert(tk.END, f"OrderDate: {details['orderDate']}\n")
            orderss_text.insert(tk.END, f"TotalAmount: {details['totalAmount']}\n")
            orderss_text.insert(tk.END, f"ShippingAddress: {details['shippingAddress']}\n\n")

def browseFiles():
    global FILEPATH
    FILEPATH = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select CSV a File",
                                        filetypes=[("CSV files", "*.csv")])
    window.destroy()

def exitWindow():
    window.destroy()

if __name__ == "__main__":
    # Example usage:
    # Function for opening the 
    # file explorer window
                                                                                
    # Create the root window
    window = tk.Tk()
    # Set window title
    window.title('File Explorer')
    # Set window size
    window.geometry("500x500")
    #Set window background color
    window.config(background = "white")
    button_explore = Button(window, 
                            text = "Browse CSV Files",
                            command = browseFiles) 
    button_exit = Button(window, 
                        text = "Exit",
                        command = exitWindow) 

    # Grid method is chosen for placing
    # the widgets at respective positions 
    # in a table like structure by
    # specifying rows and columns
    button_explore.grid(column = 1, row = 2)
    button_exit.grid(column = 1,row = 3)
    window.mainloop()

    try:
        # Read and Parse CSV Files
        with open(FILEPATH, 'r') as order_details_file:
            order_details_data = list(csv.reader(order_details_file))
        # Store the data in an appropriate data structure
        data_storage = DataStorage()
        data_storage.add_data_set('orders', [])
        data_storage.add_data_set('order_details', [])

        # Create and add some sample orderss to the Orders Database
        orders_db = OrdersDatabase()
        for order in order_details_data:
            print(order)
            orders_db.add_orders(order[1],order[2],order[3],order[4],order[5],order[6],order[7])

        # Create and run the GUI
        app = GUI(data_storage, orders_db)
        app.title("Software Engineering Project 1")
        app.configure(background="aquamarine")
        app.resizable(width=False, height=False)
        app.geometry("568x568+0+0")
        app.mainloop()
    except:
        print("You exited!!")
