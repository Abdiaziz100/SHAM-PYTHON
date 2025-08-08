from datetime import datetime

# Logging function
def write_file(f_name, txt):
    with open(f_name, 'a') as file:
        file.write(f"{txt}\n")

class Car:
    # Class variables (shared by all cars)
    brand = "Generic Motors"
    total_cars = 0

    def __init__(self, model, year):
        print("A new car object was created!")
        self._model = model
        self._year = year
        self._mileage = 0
        self.__class__.total_cars += 1  # Count total cars made

    @property
    def model(self):
        now = datetime.now()
        write_file("car_log.txt", f"At {now}, model '{self._model}' was accessed.")
        return self._model

    @model.setter
    def model(self, new_model):
        if not isinstance(new_model, str):
            print("Invalid model name. Must be a string.")
            return
        now = datetime.now()
        write_file("car_log.txt", f"At {now}, model changed from '{self._model}' to '{new_model}'.")
        self._model = new_model

    def drive(self, km):
        if km <= 0:
            print("Distance must be positive.")
            return
        self._mileage += km
        print(f"You drove {km} km. Total mileage: {self._mileage} km.")

    def show_details(self):
        print("------ Car Details ------")
        print("Brand:", self.brand)
        print("Model:", self._model)
        print("Year:", self._year)
        print("Mileage:", self._mileage, "km")
        print("-------------------------")

# Example usage
car1 = Car("Sedan", 2020)
car2 = Car("SUV", 2022)

car1.drive(150)
car2.drive(90)

print("Total cars created:", Car.total_cars)

car1.show_details()
car2.show_details()

car1.model = "Luxury Sedan"  # This will log the change
print("Updated model:", car1.model)  # This will log the access