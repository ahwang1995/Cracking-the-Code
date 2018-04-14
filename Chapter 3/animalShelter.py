import time
from Queue import Queue
#create animal shelter class which pops the oldest animal queued
class animalShelter:
	def __init__(self,dogs=None,cats=None):
		self.dogs = Queue()
		self.cats = Queue()
	#timestamp can be done using tuples, but I just queued the timestamp at the end
	def enqueue(self,animal,which):
		if which == "cat":
			self.cats.enqueue(time.time())
			self.cats.enqueue(animal)

		if which == "dog":
			self.dogs.enqueue(time.time())
			self.dogs.enqueue(animal)

	def dequeueAny(self):
		if (self.cats.isEmpty()) and (self.dogs.isEmpty()):
			return False
		if (self.cats.isEmpty()) and (not self.dogs.isEmpty()):
			self.dogs.dequeue()
			dog = self.dogs.dequeue()
			return dog
		if (self.dogs.isEmpty()) and (not self.cats.isEmpty()):
			self.cats.dequeue()
			cat = self.cats.dequeue()
			return cat
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
#test
shelter = animalShelter()
animalShelter.enqueue(1,"cat")
animalShelter.enqueue(2,"dog")
animalShelter.enqueue(3,"dog")
animalShelter.enqueue(4,"cat")
animalShelter.enqueue(5,"dog")
animalShelter.enqueue(6,"cat")
print (animalShelter.dequeueAny())