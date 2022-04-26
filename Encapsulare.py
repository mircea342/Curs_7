class Car:
    def __init__(self, brand, year, color):
        self.__brand = brand
        self.__year = year
        self.__color = color

    def get_color(self):
        return self.__color
   # ATENTIE: BRAND si YEAR NU SE MAI MODOFICA!!
    def get_brand(self):
        return self.__brand

    def get_year(self):
        return self.__year
    # Vopseaua unei maasini se mai poate modifica ulterior!
    def set_color(self, new_color):
        self.__color = new_color

c1 = Car("Toyota", 2012, "red")

# eu accesez atributul color din afara clasei ( din programul principal )
# ceea ce nu este chiar ok dpdv al principiilor OOP
# Incapsulare : eu, din prog principal, sa nu mai am acces diret la color din c1,
# ci sa obtin color prin intermediul unui "getter" (aka o metoda din clasa Car care imi returneaza color)
# print(c1.__color)

print(c1.get_color())

# NO!!!
c1.brand = "BMW"
# c1.year = 2018
# NO!!!

print(c1.get_brand())

