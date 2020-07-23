class Handphone:

def __init__(self, merk, phone_type, year, color):
self.merk = merk
self.phone_type = phone_type
self.year = year
self.color = color
self.country = "south korea"

def get_info_phone(self):
print(f"""
this phone is {self.merk} phone, from {self.country}
type \t\t: {self.phone_type}
year production \t: {self.year}
Phone color \t: {self.color}
""")

def change_color(self, new_color):
self.color = new_color
print(f"this color phone has been changed({self.color})")
"""
#my_phone = handphone("nokia", "2310", 2008, "blue mist")
#my_phone.get_info_phone()
#my_phone.change_color("True Red")
#my_phone.get_info_phone()
"""
class Battery:

def __init__(self, battery_size = 75):
self.battery_size = battery_size

def show_indicator(self):
print(f"your battery level : {self.battery_size}%")

class Smartphone(Handphone):

def __init__(self, merk, phone_type, year, color, net3g, net4g, wifinet):
super().__init__(merk, phone_type, year, color)
self.net3g = net3g
self.net4g = net4g
self.wifinet = wifinet
self.smart_battery = Battery()

def set_3g_on(self):
self.net3g = True
print("3g service run")

def set_3g_off(self):
self.net3g = False
print("3g service not Running")

def get_info_phone(self):
print(f"{self.merk} - {self.phone_type} is smartphone")

"""
my_phone = smartphone("samsung", "note 10", 2019, "black", True, True, True)
my_phone.get_info_phone()
my_phone.smart_battery.show_indicator()
"""

class Battery:

def __init__(self, battery_size = 75):
self.battery_size = battery_size

def show_indicator(self):
print(f"your battery level : {self.battery_size}%")

class Smartphone(Handphone):

def __init__(self, merk, phone_type, year, color, net3g, net4g, wifinet):
super().__init__(merk, phone_type, year, color)
self.net3g = net3g
self.net4g = net4g
self.wifinet = wifinet
self.smart_battery = Battery()

def set_3g_on(self):
self.net3g = True
print("3g service run")

def set_3g_off(self):
self.net3g = False
print("3g service not Running")

def get_info_phone(self):
print(f"{self.merk} - {self.phone_type} is smartphone")

"""
my_phone = smartphone("samsung", "note 10", 2019, "black", True, True, True)
my_phone.get_info_phone()

my_phone.smart_battery.show_indicator()
"""