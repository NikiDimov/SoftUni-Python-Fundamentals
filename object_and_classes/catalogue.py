class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        new_products = []
        for product in self.products.copy():
            if product[0] == first_letter:
                new_products.append(product)
        return new_products

    def __repr__(self):
        text = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{text}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
