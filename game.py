import random 
import time



name = input('NOTE: This may change in game experience \nBe careful what you choose.. it may end badly\n\nPlease choose a name: \n')
age = input('\nPlease choose a age: \n')
gender = input('\nPlease choose a gender: (Boy, Girl)\n')
def intro():
	print(f'\n\n\nWelcome to The Quest of The Legends {name}!\nThe options you chose when you first loaded in may affect your ingame experience!')
intro()


def part2():
	print('Now you pack everything up and say goodbye to Johnathan..\nYou hope you\'ll meet him again some day\n')


def part1():
	cookie = 0
	cookies = input(f'Hello there {name}! Welcome to Tunnel Burg!\n\nMy name is Johnathan!\nCare for some cookies?(Y/N)\n')

	if cookies.lower() == 'y': 
		if gender.lower() == 'boy':
			print('For sure!\nI notice you are a very strong man so you get 5 instead of my usual 4! (Gain 5 Cookies)\n')
			cookie += 5
			walkoreat = int(input('1: Start walking now toward\'s a house you see in the distance\n2: Eat 1 cookie\n'))
		
		elif gender.lower() == 'girl':
			print('Yes you can!\nI shall give you 4 cookies!')
			cookie += 4
			walkoreat = int(input('1: Start walking now toward\'s a house you see in the distance\n2: Eat 1 cookie\n'))
		else: 
			print('Sure!\nI shall give you 1 cookie\n')
			cookie += 1
			walkoreat = int(input('1: Start walking now toward\'s a house you see in the distance\n2: Eat 1 cookie\n'))
		
	elif cookies.lower() == 'n':
		print('Thats okay... I was planning on eating them anyway\n')
		walkoreat = int(input('1: Start walking now toward\'s a house you see in the distance \n2: Eat 1 cookie \n\n'))


	if walkoreat == 1:
		time.sleep(1)
		restart1 = input('\n\nYou start walking towards the house... \nYou finally reach it.. You open the door and find a knight standing with Shiny Armor\nYou die... \n\n1: Restart\n\n2: Go back to the last checkpoint\n\n')
		if restart1 == '1':
			intro()
		elif restart1 == '2':
			part1()
		else:
			part1()
	elif walkoreat	== 2:
		time.sleep(1)
		if cookie >= 1:
			print('You eat one cookie... Now you\'re ready for the quest.. \n\n\nPart 2')
			cookie -= 1
			part2()
		elif cookie < 1:
			print('Hey you don\'t have any cookies.. You start walking towards the house... \n\n')
			cookie -= 1
			time.sleep(1)
			part2()

part1()


input('Press enter to quit')
