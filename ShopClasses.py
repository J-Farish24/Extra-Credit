#Create Customer class
class Customer:
    #Initialize object with data attributes
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    #Mutator methods
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_phone(self, phone):
        self.__phone = phone
    #Accessor methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
    
#Create Car class
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
    #Mutator methods
    def set_make(self, make):
        self.__make = make
    
    def set_model(self, model):
        self.__model = model
    
    def set_year(self, year):
        self.__year = year
    #Accessor methods
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year

#Create ServiceQuote class
class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge
    #Mutator methods
    def set_parts_charge(self, pcharge):
        self.__parts_charges = pcharge

    def set_labor_charge(self, lcharge):
        self.__labor_charges = lcharge
    #Accessor methods
    def get_parts_charge(self):
        return self.__parts_charges
    
    def get_labor_charge(self):
        return self.__labor_charges
    
    def get_sales_tax(self):
        return (self.__labor_charges + self.__parts_charges) * .0825
    
    def get_total_charges(self):
        return (self.__parts_charges + self.__labor_charges) * 1.0825