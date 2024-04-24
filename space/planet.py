class Planet: 

    shape = 'round'

    def __init__(self, name, radius, gravity, system): # constructor function
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self): # normal function
        return f'{self.name} is orbiting in the {self.system  }'
    
    @classmethod    # it is associated with the class, works with class since its parameter is always the class itself.
    def commons(cls): 
        return f'All planets are {cls.shape} because of gravity'
    
    @staticmethod   # knows nothing about the class, deals with the parameters.
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins at {speed}'
