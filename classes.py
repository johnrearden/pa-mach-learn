from datetime import datetime

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def get_user_values(self):
        print('Current info')
        print(self)
        print('---------------')
        self.make = input('Enter new make : ')
        self.model = input('Enter new model : ')
        
        while(True):
            try:
                value = input('Enter new year : ')
                self.year = int(value)
                break
            except ValueError:
                print('Please enter a valid year (numbers only)')
                
        print()
        print('Updated info')
        print(self)
        print('---------------')
        
    def __str__(self):
        return f'{self.make} {self.model}, built in {self.year}'
    

class TaxClassMixin:
    def get_age_bracket(self):
        this_year = datetime.now().year
        age = this_year - self.year
        
        if age < 5:
            return 'Brand New'
        elif age < 20:
            return 'Legacy'
        else:
            return 'Vintage'
    
    
class Bus(Vehicle, TaxClassMixin):
    def __init__(self, make, model, year, passengers):
        super().__init__(make, model, year)
        self.passengers = passengers
        
    def __str__(self):
        return f'{super().__str__()}, carrying {self.passengers} passengers'
    

bus = Bus('Ford', 'Minivan', 2002, 43)

bus.get_user_values()
        
        
    
        