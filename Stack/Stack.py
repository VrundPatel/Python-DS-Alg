class Stack(object):
    def __init__(self):
        self.stack = []
        self.numOfItems = 0
        
    def isEmpty(self):
        return self.stack == []

    # Using the built-in insert method.
	def push(self, data):
		self.stack.insert(self.numOfItems, data)
		self.numOfItems = self.numOfItems + 1

    # Using the built-in pop method.
    def pop(self):
        self.numOfItems = self.numOfItems - 1
        data = self.stack.pop(self.numOfItems)
        return data

	def sizeOfStack(self):
		return len(self.stack)