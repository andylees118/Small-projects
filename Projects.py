#Multiples of 3 and 5 below 1000
def multiples():
	result = 0
	for i in range(1,1000):
		if i % 3 == 0 or i % 5 == 0:
			result += i
	return result

#Checks for the largest number that can be the result of multiplying numbers between 100 - 999
def checker():
	n = 0  
	#Check range between 999-100
	for a in range(999, 100, -1):
	#Check range between 999-100, using a: 999 x 999, 999 x 998 etc
		for b in range(a, 100, -1):  
		#product of a and b 
			x = a * b  
			if x > n:  
				s = str(a * b)  
				if s == s[::-1]:  
					n = a * b  
	print(n)
	
#Finds the smallest number divisible by 1-20
def divisor():
	j = 99999999999
	#Forget all numbers other than 20
	for j in range(20,99999999999,20):
		result = True
		for i in range(2,20):
			number = j
			if j % i != 0:
				result = False
				i = 20
		if result == True:
			print('while')
			return number
		j += 1
		
#Square numbers 1 - 100, sum them. Sum numbers 1 - 100 square result find the difference between the two.
def squaresummer():
	atotal = 0
	jtotal = 0
	btotal = 0
	difference = 0
	for i in range(0,101):
		atotal += i**2
	for j in range(0,101):
		jtotal += j
	btotal = jtotal ** 2
	print(atotal)
	print(jtotal)
	difference = btotal - atotal
	return difference
	

def primenumber():
	list = [2]
	for p in range(3, 9999999,2):
		for i in range (2, p):
			if p % i == 0:
				break
		else:
			list.append(p)
	return list[10001]
	
	
import random

def guessnumber():
  number = str(random.randint(1,10))
  print (number)
  answer = str(input("Guess the number"))

  if answer == number:
    print("Success!")
  else:
    print ("Try again")
    guessnumber()

	

import random

def get_random_word():
    words = ["plane","garage","tractor"]
    word = words[random.randint(0,len(words) -1 )]
    return word
  
def show_word(word):
	for character in word:
		print(character, " ", end = "")

def get_guess():
	print("Enter a letter: ")
	return input()
	
def process_letter(letter, secret_word, blanked_word):
	result = False
	for i in range(0, len(secret_word)):
		if secret_word[i] == letter:
			result = True
			blanked_word[i] = letter
	return result

def print_strikes(number_of_strikes):
	for i in range(0,number_of_strikes):
		print("X ", end = "")
	print("")
	
def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True
    word  = get_random_word()
    blanked_word = list("_" * len(word))
    
    while playing:
		show_word(blanked_word)
		letter = get_guess()
		found = process_letter(letter,word,blanked_word)
		if not found:
			strikes += 1
			print_strikes(strikes)
		      
		if strikes >= max_strikes:
			playing = False
		
		if not "_" in blanked_word:
			playing = False
	
    if strikes >= max_strikes:
      print("Loser!")
    else:
      print("Winner!")

print("Game started")
play_word_game()
print("Game over")
  
import random

def rockgame():
  print("Please select one of the following options")
  print("1 - Rock")
  print("2 - Paper")
  print("3 - Scissors")
  cycle = False
  while cycle == False:
    answer = input()
    if answer == '1' or answer == '2' or answer == '3':
        cycle = True
        comp_answer = str(random.randint(1,3))
        if answer == '1' and comp_answer == '2':
          print("Computer chooses Paper you chose Rock")
          print("You Lose!")
          return
        elif answer == '1' and comp_answer == '3':
          print("Computer chooses Scissors you chose Rock")
          print("You Win!")
          return
        
        elif answer == '2' and comp_answer == '1':
          print("Computer chooses Rock you chose Paper")
          print("You Win!")
          return
        elif answer == '2' and comp_answer == '3':
          print("Computer chooses Scissors you chose Paper")
          print("You Lose!")
          return
        
        elif answer == '3' and comp_answer == '1':
          print("Computer chooses Rock you chose Scissors")
          print("You Lose!")
          return
        elif answer == '3' and comp_answer == '2':
          print("Computer chooses Paper you chose Scissors")
          print("You Win!")
          return        
        
        elif answer == comp_answer:
          print("Draw! You chose the same option.")
          return
        
        
        
    print("Please try again")
  return False

 #########################################
  
def get_order():
	print("[command], [item] (command is a is to add, d is to remove and q is to quit)")
	line = input()
	
	command = line[:1]
	item = line[2:]
	return command, item

def add_item(item,cart):
    if not item in cart:
       cart[item] = 0
    cart[item] += 1

def remove_item(item,cart):
    if item in cart:
       cart[item] -= 1
    if cart[item] == 0:
      cart.pop(item, None)

def process_order(order, cart):
	command, item = order
	if command == 'a':
		add_item(item,cart)
	elif command == 'd' and item in cart:
		remove_item(item,cart)
	elif command == 'q':
		return False	
	
	return True
	
def go_shopping():
	cart = dict()
	while True:
		order = get_order()
		if not process_order(order,cart):
			break
	print(cart)
	print("Finished!")
	
	
import random

def number_game():
    score = 1
    play = "y"
    while play =="y":
      print("Do you want to double your score?[y/n]")
      play = input()
      if play.lower() == "y":
        result = random.randint(1,4)
        print(result)
        if result == 1:
          print("You've lost")
        else:
          score = score * 2
          print(score)
    print(score)
	

import random

def poetry_machine():
    part1 = ["Tears","Fear","Happiness","Life"]
    part2 = ["like a","for the","near the","against a"]
    part3 = ["mountain","shadow","heartache","briefcase"]
    part4 = ["of a lifetime","of my heart","near my face","in a reflection"]
  
    rand1 = random.randint(0, len(part1) - 1)
    rand2 = random.randint(0, len(part2) - 1)
    rand3 = random.randint(0, len(part3) - 1)
    rand4 = random.randint(0, len(part4) - 1)
    
    poem = part1[rand1] + ", " + part2[rand2] + " " + part3[rand3] + " " + part4[rand4]
    print(poem)
	
	

def rpg_inventory():
    inventory = []
    health = 50
    action = "go"
    while action != "stop":
      request = input("Do you want to add or use from the inventory?[a/u]")
      if request[0].lower() == "a":
          item = input("Adding?")
          inventory.append(item.lower())
      if request[0].lower() == "u":
          item = input("Using?")
          if item.lower() in inventory:
            inventory.remove(item.lower())
            if item.lower() == "potion":
              health += 50
          else:
            print("This item is not there")
      action = input("Type stop to end this")
    print(inventory,health)
	
	
def leet_dic():
    leet = {"a" : "4",
            "b" : "l3",
            "c" : "(",
            "d" : "[)",
            "e" : "3",
            "g" : "6",
            "l" : "1",
            "o" : "0",
            "s" : "5",
            "t" : "7",
            "w" : "\/\/"
            }
    print("l337 (0nv3rt3r")
    print("==============")
    textIn = ""
    while textIn.lower() != "q":
      textIn = input("Enter a sentence to translate. q to quit").lower()
      textOut = ""
      for char in textIn:
        if char in leet:
          textOut += leet[char] 
        else:
          textOut += char
      print(textOut)
	  
	  
def doorgame():
	doors = ["0" , "X", "0"]
	guess = int(input("Choose door 1, 2 or 3: "))
	if doors[guess -1] == "X":
		print(":)")
	else:
		print(":(")
		

	

def age_checker():
    try:
        first = int(input("How old is first person?"))
        second = int(input("How old is second person?"))
    except ValueError:
        print("Need to enter a valid value")
        age_checker()
    
    if first < 0 or second < 0:
      print("Need to enter a valid age")
      age_checker()
    if first > second:
      total = first - second
      total = str(total)
      return ('There is ' + total + ' years difference')
    else:
      total = second - first
      total = str(total)
      return ('There is ' + total + ' years difference')
	  
def word_count(x):
    counter = len(x.split())
    return counter
	
	
	
class Cart:
    def __init__(self):
	   self._contents = dict()
	   
	def process(self,order):
        if order.add:
            if not order.item in self._contents:
                self.contents[order.item]= 0
            self._contents[order.item] += 1
        elif order.delete:
            if order.item in self._contents:
                self._contents[order.item] -= 1
                if self._contents[order.item]				
	 
	 
class Order:
    def __init__(self):
	    self.quit = False
		self.add = False
		self.delete = False
		
	def get_input(self):
	    print("[command], [item] (command is a is to add, d is to remove and q is to quit)")
	    line = input()
	
	    command = line[:1]
	    item = line[2:]
		
		if command == "a":
		    self.add == True
	    elif command == "d":
		    self.delete = True
		elif command == "q":
            self.quit == True		
		
	    return command, item
		if command == "q":
		    return False
	    
		
def banner():
    name = input("Enter name here: ")
    style = input("Border style to use: ")
    length = len(name) + 4
    line = style * length
    print(line)
    print('{0} {1} {0}'.format(style,name))
    print(line)
	
	
def average_calc():
   alist = []
   total = 0
   itemnumber = int(input("Number of items to add to the list: "))
   for i in range(0,itemnumber):
     answer = int(input("Enter items for the list: "))
     alist.append(answer)
   for j in alist:
     total = total + j
   mean = total / itemnumber
   print(total)
   return "The mean is " + str(mean)

   
############################################################
#Battleships#

from random import randint

def create_board():
    board = []
    
    for i in range(0,5):
        board.append(["O"] * 5)

    return board
    
def print_board(board):
    for j in board:
        print(" ".join(j))
        

def random_row(board):
  return randint(0, len(board) -1)
  
def random_column(board):
  return randint(0, len(board[0]) -1)

def guess_row():
  row_guess = int(input("Guess the row: "))
  return row_guess
  
def guess_column():
  column_guess = int(input("Guess the column: "))
  return column_guess  

def game():
  board = create_board()
  print_board(board)
  row = random_row(board)
  column = random_column(board)
  game = True
  print(row,column)
  while game == True:
     row_guess = guess_row()
     column_guess = guess_column()
     print(row_guess,column_guess)
     if row_guess == row and column_guess == column:
         print("Success")
         game = False
     elif row_guess >= len(board) or column_guess >= len(board[0]):
          print("Needs to be smaller than board length")
          row_guess = guess_row()
          column_guess = guess_column()
     else:
         print("Fail, try again")
         board[row_guess][column_guess] = "X"
         print_board(board)
  
##################################

def bottles():
  number = 10
  while number > 1:
    print("{0} bottles of beer on the wall, {0} bottles of beer.".format(number))
    number -=1
    print("Take one down and pass it around, {} bottles of beer on the wall.".format(number))
    if number == 1:
      print("{0} bottle of beer on the wall, {0} bottle of beer.".format(number))
      number = 0
      print("Take one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.")