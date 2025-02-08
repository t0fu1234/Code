class Blueprint:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def get_details(self):
        return f"{self.name} ({self.category})"

class House(Blueprint):
    def __init__(self, name, category, rooms):
        super().__init__(name, category)
        self.rooms = rooms

    def show_details(self):
        return f"{self.get_details()} with {self.rooms} rooms"

house = House("Villa", "Residential", 4)
print(house.show_details())  