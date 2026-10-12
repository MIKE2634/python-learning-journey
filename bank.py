import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# ============================================================
# HEHA SAVINGS BANKING SERVICES
# ============================================================

class Customer:

    def __init__(self, name, age, national_id, account_number):
        self.name = name
        self.age = age
        self.national_id = national_id
        self.account_number = account_number
        self.balance = 0
        self.transactions = []

    # --------------------------------------------------------
    # DEPOSIT
    # --------------------------------------------------------

    def deposit(self, amount, method):

        if amount <= 0:
            return False, "Amount must be greater than zero."

        self.balance += amount

        self.transactions.append(
            {
                "type": "Deposit",
                "amount": amount,
                "method": method,
                "date": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
        )

        return True, f"KES {amount:,.2f} deposited successfully."

    # --------------------------------------------------------
    # WITHDRAW
    # --------------------------------------------------------

    def withdraw(self, amount):

        if amount <= 0:
            return False, "Amount must be greater than zero."

        if amount > self.balance:
            return False, "Insufficient balance."

        self.balance -= amount

        self.transactions.append(
            {
                "type": "Withdrawal",
                "amount": amount,
                "method": "Cash",
                "date": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
        )

        return True, f"KES {amount:,.2f} withdrawn successfully."

    # --------------------------------------------------------
    # TRANSFER
    # --------------------------------------------------------

    def transfer(self, amount, recipient):

        if amount <= 0:
            return False, "Amount must be greater than zero."

        if amount > self.balance:
            return False, "Insufficient balance."

        self.balance -= amount

        self.transactions.append(
            {
                "type": "Transfer",
                "amount": amount,
                "method": f"To {recipient.name}",
                "date": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
        )

        recipient.balance += amount

        recipient.transactions.append(
            {
                "type": "Received",
                "amount": amount,
                "method": f"From {self.name}",
                "date": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
        )

        return True, f"KES {amount:,.2f} transferred to {recipient.name}."


# ============================================================
# CUSTOMERS
# ============================================================

customer1 = Customer(
    "John",
    20,
    345673,
    "HEHA-0001"
)

customer2 = Customer(
    "Mike",
    20,
    12345,
    "HEHA-0002"
)

customer3 = Customer(
    "Sarah",
    22,
    456789,
    "HEHA-0003"
)

customers = [
    customer1,
    customer2,
    customer3
]


# ============================================================
# MAIN APPLICATION
# ============================================================

class HehaBank:

    def __init__(self, root):

        self.root = root

        self.root.title("HEHA Savings Bank")
        self.root.geometry("1000x650")
        self.root.minsize(900, 600)

        self.current_customer = None

        # ----------------------------------------------------
        # COLORS
        # ----------------------------------------------------

        self.bg = "#F4F7FB"
        self.dark = "#172554"
        self.blue = "#2563EB"
        self.green = "#16A34A"
        self.red = "#DC2626"
        self.orange = "#EA580C"
        self.white = "#FFFFFF"
        self.text = "#1E293B"
        self.gray = "#64748B"
        self.light_blue = "#DBEAFE"
        self.light_green = "#DCFCE7"
        self.light_red = "#FEE2E2"
        self.light_orange = "#FFEDD5"

        self.root.configure(bg=self.bg)   

        self.show_login()


    # ========================================================
    # CLEAR SCREEN
    # ========================================================

    def clear_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # ========================================================
    # LOGIN SCREEN
    # ========================================================

    def show_login(self):

        self.clear_screen()

        container = tk.Frame(
            self.root,
            bg=self.bg
        )

        container.pack(
            expand=True
        )

        # Logo / Bank name

        tk.Label(
            container,
            text="HEHA",
            font=("Arial", 34, "bold"),
            fg=self.blue,
            bg=self.bg
        ).pack(pady=(40, 0))

        tk.Label(
            container,
            text="SAVINGS BANK",
            font=("Arial", 14, "bold"),
            fg=self.dark,
            bg=self.bg
        ).pack()

        tk.Label(
            container,
            text="Secure • Simple • Reliable",
            font=("Arial", 10),
            fg=self.gray,
            bg=self.bg
        ).pack(pady=(5, 30))

        # Login card

        card = tk.Frame(
            container,
            bg=self.white,
            padx=40,
            pady=35
        )

        card.pack()

        tk.Label(
            card,
            text="Welcome Back",
            font=("Arial", 20, "bold"),
            fg=self.text,
            bg=self.white
        ).pack()

        tk.Label(
            card,
            text="Enter your National ID to continue",
            font=("Arial", 10),
            fg=self.gray,
            bg=self.white
        ).pack(pady=(5, 25))

        tk.Label(
            card,
            text="National ID",
            font=("Arial", 10, "bold"),
            fg=self.text,
            bg=self.white
        ).pack(anchor="w")

        self.id_entry = tk.Entry(
            card,
            width=35,
            font=("Arial", 12),
            relief="solid",
            bd=1
        )

        self.id_entry.pack(
            ipady=8,
            pady=(5, 20)
        )

        tk.Button(
            card,
            text="LOGIN",
            command=self.login,
            bg=self.blue,
            fg=self.white,
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            width=30
        ).pack(
            ipady=8
        )

        tk.Label(
            container,
            text="© 2026 HEHA Savings Bank",
            font=("Arial", 9),
            fg=self.gray,
            bg=self.bg
        ).pack(pady=30)


    # ========================================================
    # LOGIN
    # ========================================================

    def login(self):

        try:

            national_id = int(
                self.id_entry.get()
            )

        except ValueError:

            self.notification(
                "ERROR",
                "National ID must contain numbers only.",
                self.red
            )

            return

        for customer in customers:

            if customer.national_id == national_id:

                self.current_customer = customer

                self.show_dashboard()

                return

        self.notification(
            "LOGIN FAILED",
            "Customer was not found.",
            self.red
        )


    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.clear_screen()

        # ====================================================
        # HEADER
        # ====================================================

        header = tk.Frame(
            self.root,
            bg=self.dark,
            height=75
        )

        header.pack(
            fill="x"
        )

        tk.Label(
            header,
            text="HEHA",
            font=("Arial", 22, "bold"),
            fg=self.white,
            bg=self.dark
        ).pack(
            side="left",
            padx=30,
            pady=20
        )

        tk.Label(
            header,
            text="SAVINGS BANK",
            font=("Arial", 11, "bold"),
            fg="#BFDBFE",
            bg=self.dark
        ).pack(
            side="left"
        )

        tk.Button(
            header,
            text="LOGOUT",
            command=self.logout,
            bg=self.red,
            fg=self.white,
            relief="flat",
            cursor="hand2",
            font=("Arial", 9, "bold")
        ).pack(
            side="right",
            padx=25
        )


        # ====================================================
        # MAIN AREA
        # ====================================================

        main = tk.Frame(
            self.root,
            bg=self.bg
        )

        main.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )


        # ====================================================
        # WELCOME
        # ====================================================

        tk.Label(
            main,
            text=f"Good day, {self.current_customer.name} 👋",
            font=("Arial", 22, "bold"),
            fg=self.text,
            bg=self.bg
        ).pack(
            anchor="w"
        )

        tk.Label(
            main,
            text=f"Account: {self.current_customer.account_number}",
            font=("Arial", 10),
            fg=self.gray,
            bg=self.bg
        ).pack(
            anchor="w",
            pady=(2, 15)
        )


        # ====================================================
        # BALANCE CARD
        # ====================================================

        balance_card = tk.Frame(
            main,
            bg=self.blue,
            padx=25,
            pady=20
        )

        balance_card.pack(
            fill="x"
        )

        tk.Label(
            balance_card,
            text="AVAILABLE BALANCE",
            font=("Arial", 10, "bold"),
            fg="#DBEAFE",
            bg=self.blue
        ).pack(
            anchor="w"
        )

        self.balance_label = tk.Label(
            balance_card,
            text=f"KES {self.current_customer.balance:,.2f}",
            font=("Arial", 28, "bold"),
            fg=self.white,
            bg=self.blue
        )

        self.balance_label.pack(
            anchor="w",
            pady=5
        )


        # ====================================================
        # SERVICES
        # ====================================================

        tk.Label(
            main,
            text="Banking Services",
            font=("Arial", 15, "bold"),
            fg=self.text,
            bg=self.bg
        ).pack(
            anchor="w",
            pady=(20, 10)
        )


        services = tk.Frame(
            main,
            bg=self.bg
        )

        services.pack(
            fill="x"
        )


        self.service_button(
            services,
            "DEPOSIT",
            self.show_deposit,
            self.green
        ).grid(
            row=0,
            column=0,
            padx=(0, 10),
            pady=5,
            sticky="ew"
        )

        self.service_button(
            services,
            "WITHDRAW",
            self.show_withdraw,
            self.orange
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=5,
            sticky="ew"
        )

        self.service_button(
            services,
            "TRANSFER",
            self.show_transfer,
            self.blue
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=5,
            sticky="ew"
        )

        self.service_button(
            services,
            "STATEMENT",
            self.show_statement,
            self.dark
        ).grid(
            row=0,
            column=3,
            padx=(10, 0),
            pady=5,
            sticky="ew"
        )


        for i in range(4):
            services.columnconfigure(
                i,
                weight=1
            )


        # ====================================================
        # BOTTOM AREA
        # ====================================================

        bottom = tk.Frame(
            main,
            bg=self.bg
        )

        bottom.pack(
            fill="both",
            expand=True,
            pady=(20, 0)
        )


        # Profile

        profile = tk.Frame(
            bottom,
            bg=self.white,
            padx=20,
            pady=15
        )

        profile.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        tk.Label(
            profile,
            text="MY PROFILE",
            font=("Arial", 12, "bold"),
            fg=self.text,
            bg=self.white
        ).pack(
            anchor="w"
        )

        tk.Label(
            profile,
            text=f"Name: {self.current_customer.name}\n"
                 f"Age: {self.current_customer.age}\n"
                 f"National ID: {self.current_customer.national_id}\n"
                 f"Account: {self.current_customer.account_number}",
            justify="left",
            font=("Arial", 10),
            fg=self.gray,
            bg=self.white
        ).pack(
            anchor="w",
            pady=10
        )


        # Recent transactions

        recent = tk.Frame(
            bottom,
            bg=self.white,
            padx=20,
            pady=15
        )

        recent.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        tk.Label(
            recent,
            text="RECENT TRANSACTIONS",
            font=("Arial", 12, "bold"),
            fg=self.text,
            bg=self.white
        ).pack(
            anchor="w"
        )

        transactions = self.current_customer.transactions

        if not transactions:

            tk.Label(
                recent,
                text="No transactions yet.",
                font=("Arial", 10),
                fg=self.gray,
                bg=self.white
            ).pack(
                anchor="w",
                pady=15
            )

        else:

            for transaction in transactions[-4:][::-1]:

                sign = "+"

                if transaction["type"] == "Withdrawal":
                    sign = "-"

                if transaction["type"] == "Transfer":
                    sign = "-"

                if transaction["type"] == "Received":
                    sign = "+"

                row = tk.Frame(
                    recent,
                    bg=self.white
                )

                row.pack(
                    fill="x",
                    pady=3
                )

                tk.Label(
                    row,
                    text=transaction["type"],
                    font=("Arial", 10, "bold"),
                    fg=self.text,
                    bg=self.white
                ).pack(
                    side="left"
                )

                tk.Label(
                    row,
                    text=f"{sign} KES {transaction['amount']:,.2f}",
                    font=("Arial", 10, "bold"),
                    fg=(
                        self.green
                        if sign == "+"
                        else self.red
                    ),
                    bg=self.white
                ).pack(
                    side="right"
                )


    # ========================================================
    # SERVICE BUTTON
    # ========================================================

    def service_button(
        self,
        parent,
        text,
        command,
        color
    ):

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=self.white,
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            height=2
        )


    # ========================================================
    # DEPOSIT WINDOW
    # ========================================================

    def show_deposit(self):

        self.transaction_window(
            "Deposit Money",
            "DEPOSIT",
            self.process_deposit
        )


    def process_deposit(
        self,
        amount,
        method
    ):

        success, message = self.current_customer.deposit(
            amount,
            method
        )

        if success:

            self.notification(
                "SUCCESS",
                message,
                self.green
            )

            self.show_dashboard()

        else:

            self.notification(
                "DEPOSIT FAILED",
                message,
                self.red
            )


    # ========================================================
    # WITHDRAW WINDOW
    # ========================================================

    def show_withdraw(self):

        self.transaction_window(
            "Withdraw Money",
            "WITHDRAW",
            self.process_withdraw
        )


    def process_withdraw(
        self,
        amount,
        method
    ):

        success, message = self.current_customer.withdraw(
            amount
        )

        if success:

            self.notification(
                "SUCCESS",
                message,
                self.green
            )

            self.show_dashboard()

        else:

            self.notification(
                "WITHDRAWAL FAILED",
                message,
                self.red
            )


    # ========================================================
    # TRANSACTION WINDOW
    # ========================================================

    def transaction_window(
        self,
        title,
        transaction_type,
        process_function
    ):

        window = tk.Toplevel(
            self.root
        )

        window.title(title)

        window.geometry("400x350")

        window.configure(
            bg=self.bg
        )

        tk.Label(
            window,
            text=title,
            font=("Arial", 18, "bold"),
            fg=self.text,
            bg=self.bg
        ).pack(
            pady=25
        )


        tk.Label(
            window,
            text="Amount (KES)",
            font=("Arial", 10, "bold"),
            bg=self.bg,
            fg=self.text
        ).pack()


        amount_entry = tk.Entry(
            window,
            width=30,
            font=("Arial", 12)
        )

        amount_entry.pack(
            pady=8,
            ipady=5
        )


        method_var = tk.StringVar(
            value="MPESA"
        )


        if transaction_type == "DEPOSIT":

            tk.Label(
                window,
                text="Deposit Method",
                font=("Arial", 10, "bold"),
                bg=self.bg,
                fg=self.text
            ).pack(
                pady=(10, 5)
            )

            method_menu = tk.OptionMenu(
                window,
                method_var,
                "MPESA",
                "CASH",
                "BANK TRANSFER"
            )

            method_menu.config(
                width=25
            )

            method_menu.pack()


        def submit():

            try:

                amount = float(
                    amount_entry.get()
                )

            except ValueError:

                self.notification(
                    "ERROR",
                    "Please enter a valid amount.",
                    self.red
                )

                return

            process_function(
                amount,
                method_var.get()
            )

            window.destroy()


        tk.Button(
            window,
            text=transaction_type,
            command=submit,
            bg=self.blue,
            fg=self.white,
            font=("Arial", 10, "bold"),
            relief="flat",
            width=25,
            cursor="hand2"
        ).pack(
            pady=25,
            ipady=7
        )


    # ========================================================
    # TRANSFER
    # ========================================================

    def show_transfer(self):

        window = tk.Toplevel(
            self.root
        )

        window.title("Transfer Money")

        window.geometry("400x400")

        window.configure(
            bg=self.bg
        )

        tk.Label(
            window,
            text="Transfer Money",
            font=("Arial", 18, "bold"),
            bg=self.bg,
            fg=self.text
        ).pack(
            pady=25
        )


        tk.Label(
            window,
            text="Recipient National ID",
            bg=self.bg,
            fg=self.text
        ).pack()

        recipient_entry = tk.Entry(
            window,
            width=30
        )

        recipient_entry.pack(
            pady=8,
            ipady=5
        )


        tk.Label(
            window,
            text="Amount (KES)",
            bg=self.bg,
            fg=self.text
        ).pack(
            pady=(15, 0)
        )

        amount_entry = tk.Entry(
            window,
            width=30
        )

        amount_entry.pack(
            pady=8,
            ipady=5
        )


        def transfer_money():

            try:

                recipient_id = int(
                    recipient_entry.get()
                )

                amount = float(
                    amount_entry.get()
                )

            except ValueError:

                self.notification(
                    "ERROR",
                    "Please enter valid numbers.",
                    self.red
                )

                return


            recipient = None

            for customer in customers:

                if customer.national_id == recipient_id:

                    recipient = customer
                    break


            if recipient is None:

                self.notification(
                    "TRANSFER FAILED",
                    "Recipient not found.",
                    self.red
                )

                return


            if recipient == self.current_customer:

                self.notification(
                    "TRANSFER FAILED",
                    "You cannot transfer money to yourself.",
                    self.red
                )

                return


            success, message = self.current_customer.transfer(
                amount,
                recipient
            )


            if success:

                window.destroy()

                self.notification(
                    "TRANSFER SUCCESSFUL",
                    message,
                    self.green
                )

                self.show_dashboard()

            else:

                self.notification(
                    "TRANSFER FAILED",
                    message,
                    self.red
                )


        tk.Button(
            window,
            text="TRANSFER MONEY",
            command=transfer_money,
            bg=self.blue,
            fg=self.white,
            font=("Arial", 10, "bold"),
            relief="flat",
            width=25,
            cursor="hand2"
        ).pack(
            pady=25,
            ipady=7
        )


    # ========================================================
    # BANK STATEMENT
    # ========================================================

    def show_statement(self):

        window = tk.Toplevel(
            self.root
        )

        window.title("Bank Statement")

        window.geometry("650x500")

        window.configure(
            bg=self.bg
        )

        tk.Label(
            window,
            text="BANK STATEMENT",
            font=("Arial", 20, "bold"),
            bg=self.bg,
            fg=self.text
        ).pack(
            pady=20
        )


        text = tk.Text(
            window,
            width=70,
            height=20,
            font=("Courier New", 10)
        )

        text.pack(
            padx=20,
            pady=10
        )


        text.insert(
            tk.END,
            "HEHA SAVINGS BANK\n"
        )

        text.insert(
            tk.END,
            "==========================================\n"
        )

        text.insert(
            tk.END,
            f"Name: {self.current_customer.name}\n"
        )

        text.insert(
            tk.END,
            f"Account: {self.current_customer.account_number}\n"
        )

        text.insert(
            tk.END,
            f"Balance: KES {self.current_customer.balance:,.2f}\n"
        )

        text.insert(
            tk.END,
            "==========================================\n\n"
        )


        if not self.current_customer.transactions:

            text.insert(
                tk.END,
                "No transactions available.\n"
            )

        else:

            for transaction in self.current_customer.transactions:

                sign = "+"

                if transaction["type"] in [
                    "Withdrawal",
                    "Transfer"
                ]:
                    sign = "-"

                text.insert(
                    tk.END,
                    f"{transaction['date']}  "
                    f"{transaction['type']:<12} "
                    f"{sign}KES {transaction['amount']:,.2f}  "
                    f"{transaction['method']}\n"
                )


        text.config(
            state="disabled"
        )


    # ========================================================
    # NOTIFICATION
    # ========================================================

    def notification(
        self,
        title,
        message,
        color
    ):

        popup = tk.Toplevel(
            self.root
        )

        popup.title(title)

        popup.geometry("420x180")

        popup.configure(
            bg=self.white
        )

        tk.Frame(
            popup,
            bg=color,
            height=8
        ).pack(
            fill="x"
        )

        tk.Label(
            popup,
            text=title,
            font=("Arial", 15, "bold"),
            fg=color,
            bg=self.white
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            popup,
            text=message,
            font=("Arial", 10),
            fg=self.text,
            bg=self.white,
            wraplength=350
        ).pack(
            pady=5
        )

        tk.Button(
            popup,
            text="OK",
            command=popup.destroy,
            bg=color,
            fg=self.white,
            relief="flat",
            width=15,
            cursor="hand2"
        ).pack(
            pady=15
        )


    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if answer:

            self.current_customer = None

            self.show_login()


# ============================================================
# START APPLICATION
# ============================================================

root = tk.Tk()

app = HehaBank(root)

root.mainloop()