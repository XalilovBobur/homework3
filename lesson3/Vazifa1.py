class Car:
    def __init__(self, color, price, owner) -> None:
        self._color = color
        self._price = price
        self._owner = owner
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        self._color = new_color
    
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = new_price
    
   
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner


car1 = Car("red", 20000, "Alice")


car1.color = "red"
print(f"Rangi: {car1.color}") 

car1.price=20000
print(f"Narxi: {car1.price} usd")

car1.owner = "Bobur"
print(f"Yangi egasi: {car1.owner}") 