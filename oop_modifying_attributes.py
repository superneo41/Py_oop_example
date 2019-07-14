# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:39:45 2019

@author: Neo
"""

########################################################
####### Modifying attributes

class email:
    def __init__(self):
        self.is_sent = False
    
    def send_email(self):
        self.is_sent = True


my_email = email()
print(my_email.is_sent)

my_email.send_email()
print(my_email.is_sent)