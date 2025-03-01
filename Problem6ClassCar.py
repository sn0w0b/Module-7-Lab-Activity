class car:

    def __init__(self, model, year, color, car_type, manufacturer):        
        self.model = model
        self.year = year
        self.color = color
        self.type = car_type
        self.manufacturer = manufacturer


    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color
    
    def get_type(self):
        return self.type
    
    def get_manufacturer(self):
       return self.manufacturer

    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color +''+ self.type+' ' + self.manufacturer

car1 = car("Sports", 2012, "Blue", " Van", " Kia")
car2 = car("Sedan", 2020, "Black", " Truck", " Ford")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())

