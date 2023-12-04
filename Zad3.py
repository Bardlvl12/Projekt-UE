# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property:\nArea: {self.area} sq. m\nRooms: {self.rooms}\nPrice: {self.price} USD\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House:\n{super().__str__()}\nPlot Size: {self.plot} sq. m"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat:\n{super().__str__()}\nFloor: {self.floor}"



house = House(area=150, rooms=4, price=300000, address="123 Main Street", plot=500)
flat = Flat(area=80, rooms=2, price=150000, address="456 Side Street", floor=3)


print(house)
print("\n====================\n")
print(flat)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
