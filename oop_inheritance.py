# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:57:50 2019

@author: Neo
"""

##############################################
#### inheritance


# parent class
class Dog:
    
    # class attriute
    species = 'mammal'
    
    # initializer 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name,
                self.age)
    
    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name,sound)
    

# child class
class bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

######################################################
# main

jim = bulldog('Jim', 12)
print(jim.description())
print(jim.run('slowly'))

print(isinstance(jim, Dog))
print(isinstance(Dog,jim))