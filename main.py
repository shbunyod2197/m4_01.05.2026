# 16
class Food:
    def __init__(self, name, calories, weight):
        self.name = name
        self.calories = calories
        self.weight = weight

    def prepare(self):
        print(f"{self.name} tayyorlanmoqda")

class FastFood(Food):
    def __init__(self, name, calories, weight, price, time):
        super().__init__(name, calories, weight)
        self.price = price
        self.time = time

    def prepare(self):
        super().prepare()
        print(f"{self.time} daqiqada tayyor bo'ladi")

    def serve(self):
        print(f"Narxi: {self.price} so'm")

d = FastFood("Burger", 500, 300, 25000, 5)
d.prepare()
d.serve()


# 17
class Media:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def play(self):
        print(f"{self.title} ijro etilmoqda")

class Video(Media):
    def __init__(self, title, author, year, duration, quality):
        super().__init__(title, author, year)
        self.duration = duration
        self.quality = quality

    def play(self):
        super().play()
        print(f"Davomiyligi: {self.duration} daqiqa, Sifat: {self.quality}")

    def pause(self):
        print(f"{self.title} pauza qilindi")

e = Video("Dune", "Denis", 2021, 155, "4K")
e.play()
e.pause()


# 18
class Building:
    def __init__(self, floors, area, location):
        self.floors = floors
        self.area = area
        self.location = location

    def build(self):
        print(f"{self.location}da bino qurilmoqda")

class House(Building):
    def __init__(self, floors, area, location, rooms, price):
        super().__init__(floors, area, location)
        self.rooms = rooms
        self.price = price

    def build(self):
        super().build()
        print(f"Xonalar soni: {self.rooms}")

    def show_price(self):
        print(f"Narxi: {self.price} dollar")

f = House(3, 200, "Toshkent", 6, 150000)
f.build()
f.show_price()


# 19
class Product:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

class Laptop(Product):
    def __init__(self, name, price, brand, ram, cpu, storage):
        super().__init__(name, price, brand)
        self.ram = ram
        self.cpu = cpu
        self.storage = storage

    def show_info(self):
        print(f"{self.name}")
        print(f" {self.price}")
        print(f" {self.brand}")
        print(f"{self.ram}")
        print(f"{self.cpu}")
        print(f"{self.storage}")

g = Laptop("MacBook", 2000, "Apple", "16GB", "M3", "512GB")
g.show_info()


# 20
class Course:
    def __init__(self, title, duration, teacher):
        self.title = title
        self.duration = duration
        self.teacher = teacher

class OnlineCourse(Course):
    def __init__(self, title, duration, teacher, platform, price):
        super().__init__(title, duration, teacher)
        self.platform = platform
        self.price = price

    def show_course(self):
        print(f"{self.title}")
        print(f"{self.duration}")
        print(f"{self.teacher}")
        print(f"{self.platform}")
        print(f"{self.price}")

h = OnlineCourse("Python", "3 oy", "Jasur", "Udemy", 500000)
h.show_course()
