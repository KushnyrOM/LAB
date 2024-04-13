class Order:
    def __init__(self, items, customer, payment):
        self.items = items
        self.customer = customer
        self.payment = payment

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def apply_discounts(self, total):
        if self.customer.is_vip():
            total *= 0.9  # 10% discount for VIP customers
        if self.total > 1000:
            total *= 0.95  # 5% discount for orders over $1000
        if self.order_date.month == 12:
            total *= 0.9  # 10% discount for orders in December
        return total

class OrderProcessor:
    def process_order(self, order):
        # Validate order
        if not order.is_valid():
            return False

        # Calculate total and apply discounts
        order.total = order.calculate_total()
        order.total = order.apply_discounts(order.total)

        # Process payment
        if not order.payment.process():
            return False

        # Update inventory
        self.update_inventory(order)

        # Send confirmation email
        self.send_confirmation_email(order)

        return True

    def update_inventory(self, order):
        for item in order.items:
            item.quantity_in_stock -= 1

    def send_confirmation_email(self, order):
        order.customer.send_email(f"Thank you for your order of {order.total:.2f}")