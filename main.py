#9-m
class Protuct:
    def __init__(self, name, quantity):
        self.name = name
        self.__quantity = quantity
        
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity
        
p1  = Protuct("Juan", 100)

print(p1.name)
print(p1.get_quantity())

p1.set_quantity(65757)
print(p1.get_quantity())
