# transport.py

class Vehicle:
    def move(self):
        return "This vehicle moves in its own way."


class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road."


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying through the sky."


class Boat(Vehicle):
    def move(self):
        return "🛥️ Sailing on water."


# Sample usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        print(v.move())
