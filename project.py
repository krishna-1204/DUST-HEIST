import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime, date, time
import json
import os

class CarWashApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dust Heist - Doorstep Car Wash Service")
        self.root.geometry("900x700")
        self.root.configure(bg="#2c3e50")
        
        # File to store bookings
        self.bookings_file = "car_wash_bookings.json"
        self.load_bookings()
        
        # Package prices
        self.packages = {
            "Basic Wash": 299,
            "Premium Wash": 499,
            "Deluxe Detail": 799
        }
        
        self.create_widgets()
    
    def load_bookings(self):
        """Load bookings from JSON file"""
        if os.path.exists(self.bookings_file):
            try:
                with open(self.bookings_file, 'r') as f:
                    self.bookings = json.load(f)
            except:
                self.bookings = []
        else:
            self.bookings = []
    
    def save_bookings(self):
        """Save bookings to JSON file"""
        with open(self.bookings_file, 'w') as f:
            json.dump(self.bookings, indent=2, fp=f)
    
    def create_widgets(self):
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Tab 1: Home/Booking
        self.booking_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.booking_frame, text="Book Service")
        self.create_booking_tab()
        
        # Tab 2: View Packages
        self.packages_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.packages_frame, text="Our Packages")
        self.create_packages_tab()
        
        # Tab 3: View Bookings
        self.view_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.view_frame, text="View Bookings")
        self.create_view_tab()
    
    def create_booking_tab(self):
        # Header
        header = tk.Frame(self.booking_frame, bg="#34495e", height=100)
        header.pack(fill='x')
        
        title = tk.Label(header, text="🎯 Dust Heist", font=("Arial", 28, "bold"),
                        bg="#34495e", fg="#ecf0f1")
        title.pack(pady=10)
        
        subtitle = tk.Label(header, text="We Are Here to Heist All the Dust!",
                           font=("Arial", 12), bg="#34495e", fg="#bdc3c7")
        subtitle.pack()
        
        # Booking Form
        form_frame = tk.Frame(self.booking_frame, bg="white")
        form_frame.pack(pady=20, padx=40, fill='both', expand=True)
        
        tk.Label(form_frame, text="Book Your Service", font=("Arial", 20, "bold"),
                bg="white").pack(pady=10)
        
        # Customer Name
        tk.Label(form_frame, text="Customer Name:", font=("Arial", 11),
                bg="white").pack(anchor='w', pady=(10,0))
        self.name_entry = tk.Entry(form_frame, font=("Arial", 11), width=40)
        self.name_entry.pack(pady=5)
        
        # Phone Number
        tk.Label(form_frame, text="Phone Number:", font=("Arial", 11),
                bg="white").pack(anchor='w', pady=(10,0))
        self.phone_entry = tk.Entry(form_frame, font=("Arial", 11), width=40)
        self.phone_entry.pack(pady=5)
        
        # Address
        tk.Label(form_frame, text="Address:", font=("Arial", 11),
                bg="white").pack(anchor='w', pady=(10,0))
        self.address_entry = tk.Entry(form_frame, font=("Arial", 11), width=40)
        self.address_entry.pack(pady=5)
        
        # Package Selection
        tk.Label(form_frame, text="Select Package:", font=("Arial", 11),
                bg="white").pack(anchor='w', pady=(10,0))
        self.package_var = tk.StringVar()
        package_combo = ttk.Combobox(form_frame, textvariable=self.package_var,
                                     font=("Arial", 11), width=38, state='readonly')
        package_combo['values'] = [f"{name} - ₹{price}" for name, price in self.packages.items()]
        package_combo.pack(pady=5)
        
        # Date Selection
        date_frame = tk.Frame(form_frame, bg="white")
        date_frame.pack(pady=10)
        
        tk.Label(date_frame, text="Date:", font=("Arial", 11),
                bg="white").pack(side='left', padx=5)
        
        today = date.today()
        self.day_var = tk.StringVar(value=str(today.day))
        self.month_var = tk.StringVar(value=str(today.month))
        self.year_var = tk.StringVar(value=str(today.year))
        
        day_spin = tk.Spinbox(date_frame, from_=1, to=31, textvariable=self.day_var,
                             width=5, font=("Arial", 11))
        day_spin.pack(side='left', padx=2)
        
        tk.Label(date_frame, text="/", bg="white").pack(side='left')
        
        month_spin = tk.Spinbox(date_frame, from_=1, to=12, textvariable=self.month_var,
                               width=5, font=("Arial", 11))
        month_spin.pack(side='left', padx=2)
        
        tk.Label(date_frame, text="/", bg="white").pack(side='left')
        
        year_spin = tk.Spinbox(date_frame, from_=2024, to=2026, textvariable=self.year_var,
                              width=8, font=("Arial", 11))
        year_spin.pack(side='left', padx=2)
        
        # Time Selection
        time_frame = tk.Frame(form_frame, bg="white")
        time_frame.pack(pady=10)
        
        tk.Label(time_frame, text="Time:", font=("Arial", 11),
                bg="white").pack(side='left', padx=5)
        
        self.hour_var = tk.StringVar(value="09")
        self.minute_var = tk.StringVar(value="00")
        
        hour_spin = tk.Spinbox(time_frame, from_=0, to=23, textvariable=self.hour_var,
                              width=5, font=("Arial", 11), format="%02.0f")
        hour_spin.pack(side='left', padx=2)
        
        tk.Label(time_frame, text=":", bg="white", font=("Arial", 12)).pack(side='left')
        
        minute_spin = tk.Spinbox(time_frame, from_=0, to=59, textvariable=self.minute_var,
                                width=5, font=("Arial", 11), format="%02.0f")
        minute_spin.pack(side='left', padx=2)
        
        # Additional Notes
        tk.Label(form_frame, text="Additional Notes (Optional):", font=("Arial", 11),
                bg="white").pack(anchor='w', pady=(10,0))
        self.notes_text = tk.Text(form_frame, height=4, width=40, font=("Arial", 10))
        self.notes_text.pack(pady=5)
        
        # Submit Button
        submit_btn = tk.Button(form_frame, text="Book Now", font=("Arial", 14, "bold"),
                              bg="#34495e", fg="white", padx=30, pady=10,
                              command=self.submit_booking, cursor="hand2")
        submit_btn.pack(pady=20)
    
    def create_packages_tab(self):
        # Header
        header = tk.Frame(self.packages_frame, bg="#34495e", height=80)
        header.pack(fill='x')
        
        tk.Label(header, text="Our Affordable Packages", font=("Arial", 24, "bold"),
                bg="#34495e", fg="#ecf0f1").pack(pady=20)
        
        # Packages Container
        container = tk.Frame(self.packages_frame, bg="white")
        container.pack(fill='both', expand=True, padx=20, pady=20)
        
        packages_info = {
            "Basic Wash": {
                "price": "₹299",
                "features": [
                    "✓ Exterior hand wash",
                    "✓ Wheel cleaning",
                    "✓ Window cleaning",
                    "✓ Tire shine",
                    "✓ Quick dry"
                ],
                "color": "#7f8c8d"
            },
            "Premium Wash": {
                "price": "₹499",
                "features": [
                    "✓ Everything in Basic",
                    "✓ Interior vacuuming",
                    "✓ Dashboard cleaning",
                    "✓ Door panel wiping",
                    "✓ Air freshener",
                    "✓ Mat cleaning"
                ],
                "color": "#95a5a6"
            },
            "Deluxe Detail": {
                "price": "₹799",
                "features": [
                    "✓ Everything in Premium",
                    "✓ Complete wax & polish",
                    "✓ Engine bay cleaning",
                    "✓ Leather conditioning",
                    "✓ Carpet shampooing",
                    "✓ Headlight restoration"
                ],
                "color": "#34495e"
            }
        }
        
        row = 0
        col = 0
        for pkg_name, pkg_info in packages_info.items():
            pkg_frame = tk.Frame(container, bg=pkg_info["color"], relief='raised', bd=2)
            pkg_frame.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
            
            tk.Label(pkg_frame, text=pkg_name, font=("Arial", 16, "bold"),
                    bg=pkg_info["color"], fg="white").pack(pady=10)
            
            tk.Label(pkg_frame, text=pkg_info["price"], font=("Arial", 32, "bold"),
                    bg=pkg_info["color"], fg="white").pack(pady=10)
            
            features_frame = tk.Frame(pkg_frame, bg="white")
            features_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            for feature in pkg_info["features"]:
                tk.Label(features_frame, text=feature, font=("Arial", 10),
                        bg="white", anchor='w').pack(fill='x', pady=3)
            
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(3):
            container.grid_columnconfigure(i, weight=1)
        container.grid_rowconfigure(0, weight=1)
        
        # Contact Info
        contact_frame = tk.Frame(self.packages_frame, bg="#ecf0f1")
        contact_frame.pack(fill='x', pady=10)
        
        tk.Label(contact_frame, text="📞 Phone: (555) 123-4567  |  📧 Email: info@dustheist.com  |  ⏰ Mon-Sat: 8AM-8PM",
                font=("Arial", 10), bg="#ecf0f1").pack(pady=10)
    
    def create_view_tab(self):
        # Header
        header = tk.Frame(self.view_frame, bg="#34495e", height=80)
        header.pack(fill='x')
        
        tk.Label(header, text="All Bookings", font=("Arial", 24, "bold"),
                bg="#34495e", fg="#ecf0f1").pack(pady=20)
        
        # Buttons Frame
        btn_frame = tk.Frame(self.view_frame, bg="white")
        btn_frame.pack(pady=10)
        
        refresh_btn = tk.Button(btn_frame, text="Refresh", font=("Arial", 11),
                               bg="#7f8c8d", fg="white", padx=20, pady=5,
                               command=self.refresh_bookings, cursor="hand2")
        refresh_btn.pack(side='left', padx=5)
        
        clear_btn = tk.Button(btn_frame, text="Clear All Bookings", font=("Arial", 11),
                             bg="#95a5a6", fg="white", padx=20, pady=5,
                             command=self.clear_bookings, cursor="hand2")
        clear_btn.pack(side='left', padx=5)
        
        # Bookings Display
        self.bookings_text = scrolledtext.ScrolledText(self.view_frame, font=("Courier", 10),
                                                       height=20, width=100)
        self.bookings_text.pack(padx=20, pady=10, fill='both', expand=True)
        
        self.refresh_bookings()
    
    def submit_booking(self):
        # Validate inputs
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()
        package = self.package_var.get()
        
        if not all([name, phone, address, package]):
            messagebox.showerror("Error", "Please fill in all required fields!")
            return
        
        try:
            # Create date and time objects
            booking_date = date(int(self.year_var.get()), 
                              int(self.month_var.get()), 
                              int(self.day_var.get()))
            booking_time = time(int(self.hour_var.get()), 
                               int(self.minute_var.get()))
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time!")
            return
        
        # Create booking record
        booking = {
            "booking_id": len(self.bookings) + 1,
            "name": name,
            "phone": phone,
            "address": address,
            "package": package,
            "date": booking_date.strftime("%Y-%m-%d"),
            "time": booking_time.strftime("%H:%M"),
            "notes": self.notes_text.get("1.0", "end-1c").strip(),
            "booked_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.bookings.append(booking)
        self.save_bookings()
        
        messagebox.showinfo("Success", f"Booking confirmed!\n\nBooking ID: {booking['booking_id']}\nWe'll contact you soon!")
        
        # Clear form
        self.name_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.package_var.set('')
        self.notes_text.delete("1.0", "end")
    
    def refresh_bookings(self):
        self.load_bookings()
        self.bookings_text.delete("1.0", "end")
        
        if not self.bookings:
            self.bookings_text.insert("1.0", "No bookings yet.\n")
            return
        
        self.bookings_text.insert("1.0", f"Total Bookings: {len(self.bookings)}\n")
        self.bookings_text.insert("end", "=" * 100 + "\n\n")
        
        for booking in self.bookings:
            booking_text = f"""
Booking ID: {booking['booking_id']}
Customer: {booking['name']}
Phone: {booking['phone']}
Address: {booking['address']}
Package: {booking['package']}
Date: {booking['date']} at {booking['time']}
Notes: {booking.get('notes', 'N/A')}
Booked On: {booking['booked_on']}
{'-' * 100}
"""
            self.bookings_text.insert("end", booking_text)
    
    def clear_bookings(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all bookings?"):
            self.bookings = []
            self.save_bookings()
            self.refresh_bookings()
            messagebox.showinfo("Success", "All bookings cleared!")

def main():
    root = tk.Tk()
    app = CarWashApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()