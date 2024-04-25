class Tab:
    menu = {    # dictionary
        'wine': 5,
        'beer': 3,
        'soft_drink': 2,
        'chicken': 8,
        'veggie': 12,
        'desert': 15
    }

    def __init__(self): # constructor
        self.total = 0
        self.items = [] # list of items

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service / 100) * self.total
        total = self.total + tax + service

        for item in self.items: 
            print(f'{item} Rs{self.menu[item]}')

        print(f'{"Total":20} Rs{total:.2f}')


table1 = Tab()
table1.add('soft_drink')
table1.add('chicken')
table1.add('desert')
table1.add('wine')
table1.print_bill(10, 10)