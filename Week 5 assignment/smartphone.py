# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class (Inheritance + Encapsulation)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.__storage = storage     # encapsulated
        self.__battery = battery     # encapsulated

    def get_storage(self):
        return self.__storage

    def set_storage(self, storage):
        if storage > 0:
            self.__storage = storage
        else:
            print("Storage must be positive")

    def battery_status(self):
        return f"Battery at {self.__battery}%"

    def call(self, number):
        return f"Calling {number}..."

# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S24", 256, 85)
    print(phone1.device_info())        # Samsung Galaxy S24
    print(phone1.battery_status())     # Battery at 85%
    print(phone1.call("+254700000000"))
    print("Storage:", phone1.get_storage())
