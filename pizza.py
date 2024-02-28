class Pizza:
    def __init__(self,name,ingredients,price):
        self.name = name
        self.ingredients= ingredients
        self.price = price
       
    def __str__(self):
        return f"{self.name} - Ingredients: {', '.join(self.ingredients)} - Price: ${self.price:.2f}"

