
# Silvia Siu Luo
# 
class Player:
	def __init__(self, name, map, list, directions):
		self.name = name
		self.map = map
		self.list = list
		self.room = self.list[0]
		self.times = self.room - 1 #This variable is to get the number of times the user have moved from room to room
		self.room_1 = self.room - 1
		self.current_room = self.map[self.room_1]
		self.directions = directions#self.current is the list inside map.
		
	def movements(self, user):
		self.move = user
		self.room_1 = self.room - 1
		self.current_room = self.map[self.room_1]
		if self.move == self.directions[0]: #if the user input is equal to the value of list direction at index 0. The same happen to other index of directions.
			if self.current_room[0] >= 1:#The value at the current_room need to be large than zero.
				self.room = self.current_room[0]
				self.times += 1 
			else:
				print("You can't move there") #if the value at current_room is 0
		elif self.move == self.directions[1]: 
			if self.current_room[1] >= 1:
				self.room = self.current_room[1]
				self.times += 1
			else:
				print("You can't move there")
		elif self.move == self.directions[2]:
			if self.current_room[2] >= 1:
				self.room = self.current_room[2]
				self.times += 1
			else:
				print("You can't move there")
		elif self.move ==self.directions[3]:
			if self.current_room[3] >= 1:
				self.room = self.current_room[3]
				self.times += 1
			else:
				print("You can't move there")
		return self.current_room #this return the new current_room
		update()
		
	def exits_in_room(self):
		print("The exits in this room are located at:")
		
		#To find the elements in we need to use the for loop, which will give us the position of
		#the numbers bigger than zero.
		
		for self.a in self.current_room: #for every value in the first list.
			if self.a in self.list:
				
				self.door = self.current_room.index(self.a)
				self.transform = self.directions[self.door]#This will transform self.door to one of the values of directions.
				print (self.transform)
	def display_times(self):
		return self.times
	def player_position(self):
		#this method will try to get the position of the player
		return self.room 
	
		
	def player_name(self):
		return self.name #returns the user name

def main():		
	map = [[0, 2, 0, 0], [0, 20, 3, 1], [2, 4, 0, 0], [0, 9, 5, 3], [4, 0, 0, 0], [0, 8, 7, 0], [6, 0, 0, 0], [10, 0, 0, 6], [0, 10, 0, 4],[12, 11, 8, 9], [0, 0, 0, 10], [16, 13, 10, 0], [0, 14, 0, 12], [0, 0, 0, 13], [0, 0, 0, 16], [17, 15, 12, 18], [0, 0, 16, 0], [0, 16, 0, 19], [0, 18, 20, 0], [19, 0, 0, 2]]
	name = input("What is your name? ")
	list = []#This list is empty, but it will get bigger as it appends more elements.
	directions = ["North", "East", "South", "West"]
	for i in range (1, 21):
		list.append(i)
		#i is the room's name
	avatar = Player(name,map,list, directions)#starting the class
	print("Game Started")
	while True:
		
		#this will give the user their position in their game.
		position = avatar.player_position()
		print("{}, you are in room {}".format(avatar.player_name(), position))
		
		#Print the exits in the room
		avatar.exits_in_room()
		#ask the user to decide where to go.
		user = input("Where do you want to go? ")
		#move the player
		avatar.movements(user)
		#gives the user the times he has moved
		count = avatar.display_times()
		print("Times moved:", count)
		#if the user type "Quit" it will finish the game.
		if user == "Quit":
			break
	print("Game Over")
main()#call the main function