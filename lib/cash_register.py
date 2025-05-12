class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        # Calculate transaction value
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction = transaction_amount
        # Add item title to list for each quantity
        self.items += [title] * quantity

    def apply_discount(self):
        if self.discount:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def get_items(self):
        return self.items

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0  # Reset the last transaction
