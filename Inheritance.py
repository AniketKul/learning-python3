#Assuming Employee is a class created already.

#For a subclass to define new class variables, it needs to define __init__()
class specialEmployee(Employee):
    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name, rate) #calls the base classes
        self.bonus = bonus

    def hours(self, numHours):
        self.owed += numHours * self.rate + self.bonus
        return("%.2f hours worked" % numHours)

#A static method can be defined in a class using @staticmethod class decorator.
'''
Static method cannot access the attributes of an instance so their most common
usage is a convenience to group utility functions together.
'''

#Class methods operate on the class itself, not the instance. Also, class variables
#are associated with the classes rather than instances of that class.
#They are defined using the @classmethod decorator and are distinguished by
# from instance methods in that the class is passed as the first argument.
#This is named cls by convention.

class Aexp(object):
    base = 2
    @classmethod
    def exp(cls, x):
        return(cls.base ** x)

class Bexp(Aexp):
    base = 3
    
