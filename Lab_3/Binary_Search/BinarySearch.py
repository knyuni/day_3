class binarySearch(list):
	def __init__(self, data=None, left=None, right=None):
		self.left = left
        self.right = right
        self.data = data

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid
		


	def search(a, b):
		a = 0
		b = len(a)-1
		length = False
		if node is None:
			return False
		else:
			if node.data == item:
				return True

       	elif node.data < item:
       		return self.search(node.right, item)
       	else:
           	return self.search(node.left, item)
	
