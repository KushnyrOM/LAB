class Product:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

class ProductRepository:
    def search_product(self, products, query):
        # Пошук товару за запитом
        pass

    def display_product(self, product):
        # Відображення інформації про товар
        pass

class OrderService:
    def order_product(self, product, quantity):
        # Замовлення товару
        pass

# Приклад використання
product = Product("Товар 1", 100, "Категорія 1")
product_repo = ProductRepository()
order_service = OrderService()

product_repo.display_product(product)
order_service.order_product(product, 5)