# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 01:52:38 2021

@author: mjach
"""

'''
Shopping List Project
1. Create a shopping list - items add
2. Iteam view from the shopping list
3. Delete shopping items from the list.
4. Writing to the file all the shopping items.
5. Exit from the program
'''
#importing libraries
import sys
import os

#creating empty list
shopping_list = []

try:
    with open('shoppingList.txt', 'r') as shopping_list_file:
        for item in shopping_list_file:
            shopping_list.append(item)
    shopping_list_file.close()
except FileNotFoundError as file_error:
    #pass
    print('No such file exits', file_error)
            

def mainMenu():
    #to clear the screen
    os.system('cls')
    print('\t\t----Shopping List----')
    print('\t\t---------------------')
    print('Please select an options:\n')
    print('(a)dd an item.')
    print('(v)iew the list.')
    print('(d)elete an item.')
    print('(e)xit the program.')
    
    user_choice = input('Please select an option: ')
    
    if len(user_choice) > 0:
        if user_choice.lower()[0] == 'a':
            addItems()
        elif user_choice.lower()[0] == 'v':
            view_shopping_list()
        elif user_choice.lower()[0] == 'd':
            delete_shopping_item()           
        elif user_choice.lower()[0] == 'e':
            sys.exit()
        else:
            mainMenu()
    else:
        mainMenu()

# add items function
def addItems():
    os.system('cls')
    print('\t\t----Add Item Screen----')
    print('\t\t---------------------\n')
    print('Please enter the name of the item:')
    print('Please press enter to go back to main menu.')
    
    user_input = input('Item Name: ')
    if len(user_input) > 0:
        shopping_list.append(user_input)
        print('Item has been added.')
        #calling save_to_file function
        save_to_file()
        
        addItems()
    else:
        mainMenu()
        
#crating view function

def view_shopping_list():
    os.system('cls')
    print('\t\t----View Item Screen----')
    print('\t\t---------------------\n')
    
    for item in shopping_list:
        print(item)
    
    print('Press enter to go back to main menu.')
    input()
    mainMenu()

def delete_shopping_item():
    os.system('cls')
    print('\t\t----Delete Item Screen----')
    print('\t\t---------------------\n')
    
    count = 0
    
    for item in shopping_list:
        print(count, '-', item)
        count = count + 1
        
    print('What item number you want to delete?:')
    
    user_choice = input('Plese enter a number:')
    
    if len(user_choice) > 0:
        try:
            del shopping_list[int(user_choice)]
            print('Item has been deleted')
            
            save_to_file()
        except:
            print('Please check your number.')
            
        delete_shopping_item()
    else:
        mainMenu()

def save_to_file():
    writing_to_file = open('shoppingList.txt', 'w')
    for item in shopping_list:
        writing_to_file.write(item + '\n')
    writing_to_file.close()
    
#calling main menu funciton
mainMenu()