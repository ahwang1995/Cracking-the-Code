import time
from Queue import Queue
#create animal shelter class which pops the oldest animal queued
class animalShelter:
	def __init__(self,dogs=None,cats=None):
		self.dogs = Queue()
		self.cats = Queue()
	#timestamp can be done using tuples, but I just queued the timestamp at the end
	def enqueue(self,animal,which):
		#check if dog or cat and enqueue with timestamp
		if which == "cat":
			self.cats.enqueue(time.time())
			self.cats.enqueue(animal)

		if which == "dog":
			self.dogs.enqueue(time.time())
			self.dogs.enqueue(animal)
	#dequeue regardless of dog or cat
	def dequeueAny(self):
		#if both queues empty return false
		if (self.cats.isEmpty()) and (self.dogs.isEmpty()):
			return False

		#if cats is empty dequeue dog
		if (self.cats.isEmpty()) and (not self.dogs.isEmpty()):
			self.dogs.dequeue()
			dog = self.dogs.dequeue()
			return dog

		#if dogs is empty dequeue cat
		if (self.dogs.isEmpty()) and (not self.cats.isEmpty()):
			self.cats.dequeue()
			cat = self.cats.dequeue()
			return cat

		#compare dog and cat timestamps and dequeue oldest
		d = self.dogs.peek()
		c = self.cats.peek()
		if(c < d):
			self.cats.dequeue()
			cat = self.cats.dequeue()
			return cat

		else:
			self.dogs.dequeue()
			dog = self.dogs.dequeue()
			return dog

	#dequeue dog
	def dequeueDog(self):
		if(self.dogs.isEmpty()):
			return False
		self.dogs.dequeue()
		dog = self.dogs.dequeue()
		return dog

	#dequeue cat
	def dequeueCat(self):
		if(self.cats.isEmpty()):
			return False
		self.cats.dequeue()
		cat = self.cats.dequeue()
		return cat
#test
shelter = animalShelter()
shelter.enqueue(1,"cat")
shelter.enqueue(2,"dog")
shelter.enqueue(3,"dog")
shelter.enqueue(4,"cat")
shelter.enqueue(5,"dog")
shelter.enqueue(6,"cat")
print (shelter.dequeueDog())
print (shelter.dequeueAny())
print (shelter.dequeueAny())