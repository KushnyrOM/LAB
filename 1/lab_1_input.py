class OrderProcessor:
    def process_order(self, order):
        # Validate order
        if not order.is_valid():
            return False

        # Calculate total
        total = 0
        for item in order.items:
            total += item.price

        # Apply discounts
        if order.customer.is_vip():
            total *= 0.9  # 10% discount for VIP customers
        if order.total > 1000:
            total *= 0.95  # 5% discount for orders over $1000
        if order.order_date.month == 12:
            total *= 0.9  # 10% discount for orders in December

        # Process payment
        if not order.payment.process():
            return False

        # Update inventory
        for item in order.items:
            item.quantity_in_stock -= 1

        # Send confirmation email
        order.customer.send_email(f"Thank you for your order of {total:.2f}")

        return True