import random

potential_item_names = [
    "Reloj Antiguo", "Cámara Vintage", "Anillo de Oro", "Collar de Plata", "Pendientes de Diamantes",
    "Moneda Rara", "Bate de Béisbol Firmado", "Libro Primera Edición", "Guitarra Clásica", "Pintura Antigua",
    "Jarrón de Cerámica", "Sello Coleccionable", "Decantador de Cristal", "Maletín de Cuero", "Navaja de Bolsillo",
    "Estatua de Bronce", "Muñeca de Porcelana", "Figura de Jade", "Juguete Mecánico", "Máquina de Escribir"
]

all_items = []
for i in range(20):
    item_name = random.choice(potential_item_names)
    item_name_with_id = f"{item_name} #{i+1}"
    price = round(random.uniform(50, 1000), 2)
    all_items.append({"name": item_name_with_id, "price": price})

selected_items_for_sale = random.sample(all_items, 5)

print("--- Artículos Seleccionados para la Venta ---")
for item in selected_items_for_sale:
    print(f"Artículo: {item['name']}, Precio: ${item['price']:.2f}")

class Customer:
    def __init__(self, name, min_offer, max_offer, offers_value):
        self.name = name
        self.min_offer = min_offer
        self.max_offer = max_offer
        self.offers_value = offers_value

    def __str__(self):
        behavior = "ofrece un valor" if self.offers_value else "escucha la propuesta"
        return (f"Cliente: {self.name}, Oferta Mínima: ${self.min_offer:.2f}, "
                f"Oferta Máxima: ${self.max_offer:.2f}, Comportamiento: {behavior}")

potential_customer_names = [
    "Ana", "Benito", "Carlos", "Diana", "Elena", "Fernando", "Gabriela", "Hugo", "Isabel", "Javier",
    "Karen", "Luis", "Marta", "Nacho", "Olivia", "Pedro", "Quique", "Rosa", "Sergio", "Tania"
]

customers = []
for i in range(10):
    name = random.choice(potential_customer_names) + f"_{i+1}"
    min_offer = round(random.uniform(20, 200), 2)
    max_offer = round(random.uniform(min_offer + 50, 500), 2)
    offers_value = random.choice([True, False])

    customers.append(Customer(name, min_offer, max_offer, offers_value))

print("\n--- Clientes Creados ---")
for customer in customers:
    print(customer)
