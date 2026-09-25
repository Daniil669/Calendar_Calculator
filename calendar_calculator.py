import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

class DateCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Date Calculator")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 10, 'pady': 6}

        # Desired date selection: today or custom
        self.date_mode = tk.StringVar(value="today")
        frame_date_mode = ttk.LabelFrame(self.root, text="1) Desired Date")
        frame_date_mode.pack(fill='x', **padding)

        rb_today = ttk.Radiobutton(frame_date_mode, text="Today", variable=self.date_mode, value="today", command=self.toggle_custom_date)
        rb_today.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        rb_custom = ttk.Radiobutton(frame_date_mode, text="Custom Date", variable=self.date_mode, value="custom", command=self.toggle_custom_date)
        rb_custom.grid(row=0, column=1, sticky='w', padx=5, pady=5)

        # Custom date inputs
        frame_custom_date = ttk.Frame(frame_date_mode)
        frame_custom_date.grid(row=1, column=0, columnspan=2, pady=5)

        ttk.Label(frame_custom_date, text="Day:").grid(row=0, column=0, sticky='e')
        self.entry_day = ttk.Entry(frame_custom_date, width=5, state='disabled')
        self.entry_day.grid(row=0, column=1, sticky='w', padx=(0, 10))

        ttk.Label(frame_custom_date, text="Month:").grid(row=0, column=2, sticky='e')
        self.entry_month = ttk.Entry(frame_custom_date, width=5, state='disabled')
        self.entry_month.grid(row=0, column=3, sticky='w', padx=(0, 10))

        ttk.Label(frame_custom_date, text="Year:").grid(row=0, column=4, sticky='e')
        self.entry_year = ttk.Entry(frame_custom_date, width=8, state='disabled')
        self.entry_year.grid(row=0, column=5, sticky='w')

        # Number of days input
        frame_days = ttk.Frame(self.root)
        frame_days.pack(fill='x', **padding)
        ttk.Label(frame_days, text="2) Number of days:").grid(row=0, column=0, sticky='w')
        self.entry_days = ttk.Entry(frame_days, width=15)
        self.entry_days.grid(row=0, column=1, sticky='w', padx=5)

        # Add or subtract selection
        frame_operation = ttk.LabelFrame(self.root, text="3) Operation")
        frame_operation.pack(fill='x', **padding)
        self.operation = tk.StringVar(value="add")
        rb_add = ttk.Radiobutton(frame_operation, text="Add", variable=self.operation, value="add")
        rb_add.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        rb_subtract = ttk.Radiobutton(frame_operation, text="Subtract", variable=self.operation, value="subtract")
        rb_subtract.grid(row=0, column=1, sticky='w', padx=5, pady=5)

        # Calculate button
        self.btn_calculate = ttk.Button(self.root, text="4) Calculate", command=self.calculate_date)
        self.btn_calculate.pack(pady=15)

        # Output label
        self.output_label = ttk.Label(self.root, text="", font=("Segoe UI", 12), foreground="blue")
        self.output_label.pack(pady=10)

    def toggle_custom_date(self):
        if self.date_mode.get() == "custom":
            state = 'normal'
        else:
            state = 'disabled'
            # Clear custom date entries when disabled
            self.entry_day.delete(0, tk.END)
            self.entry_month.delete(0, tk.END)
            self.entry_year.delete(0, tk.END)

        self.entry_day.config(state=state)
        self.entry_month.config(state=state)
        self.entry_year.config(state=state)

    def calculate_date(self):
        try:
            # Get base date
            if self.date_mode.get() == "today":
                base_date = datetime.today()
                base_date = base_date.replace(hour=0, minute=0, second=0, microsecond=0)
            else:
                day_str = self.entry_day.get()
                month_str = self.entry_month.get()
                year_str = self.entry_year.get()
                if not (day_str and month_str and year_str):
                    raise ValueError("Please enter day, month, and year for the custom date.")
                day = int(day_str)
                month = int(month_str)
                year = int(year_str)
                base_date = datetime(year, month, day)

            # Get number of days
            days_str = self.entry_days.get()
            if not days_str:
                raise ValueError("Please enter the number of days.")
            days = int(days_str)
            if days < 0:
                raise ValueError("Number of days must be zero or positive.")

            # Add or subtract days
            if self.operation.get() == "add":
                new_date = base_date + timedelta(days=days)
            else:
                new_date = base_date - timedelta(days=days)

            # Format and display result
            result_str = new_date.strftime("%d.%m.%Y")
            self.output_label.config(text=f"New calculated date: {result_str}")

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")

def main():
    root = tk.Tk()
    app = DateCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
