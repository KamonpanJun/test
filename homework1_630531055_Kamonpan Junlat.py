# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 10:30:43 2021

@author: Lenovo
"""

number = int(input("How many sticks(N) in the pile:"))
if number <=0:
    print("please you take input of sticks more than 1.")
else:
    print ("There are",number,"sticks in the pile.")  
    name = (input("What is your name :")) 
    times_of_pick = 0 
    while number >0:  
        ques = int(input(f"{name},how many sticks you will take (1 or 2):")) 
        if ques > 2 :
            print("No you cannot take more than 2 sticks!") 
        elif ques <= 0 : 
            print("No you cannot take less than 1 stick!") 
        else:  
            if ques > number : 
                print("There are no enough stick to take.") 
            else: 
                number = number - ques 
                print("There are",number,"sticks in the pile.") 
                times_of_pick = times_of_pick + 1 
    else:  
        print("OK.There is no stick left in the pile. You spent",times_of_pick,"times.")
  
    


        
        
        
        
        
    
        

