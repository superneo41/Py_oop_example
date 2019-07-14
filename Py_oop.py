# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:35:44 2019

@author: Neo
"""

class Dog:
    
    # class attribute
    species = 'mammal'
    
    # initializer / instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name,self.age)
    
    # instance method
    def speak(self,sound):
        return "{} says {}".format(self.name,sound)



###########################################################
## main  ##

# initiate the dog object
philo = Dog('Philo',2)
mikey = Dog('Mikey',3)


# Access the instance attributes
print("{} is {} and {} is {}".format(
        philo.name,philo.age,mikey.name,mikey.age))

# is philo a mammal ?
print("{} is a {}".format(philo.name,philo.species))

# call instance method
print(philo.description())
print(philo.speak("Wang Wang"))
