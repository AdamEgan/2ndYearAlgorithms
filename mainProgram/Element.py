#Adam Egan 115359356
class Element:
 """ A key, value and index. """

 def __init__(self, k, v,i):
     self._key = k
     self._value = v
     self._index = i
 def __lt__(self, other):
     return self._key < other._key
 def __str__(self):
     return("%s"%(self._value))
 #Gets the index of the element
 def getElement(self):
     return self._index
 #sets the index of the element
 def setElement(self,element):
     self._index=element
 def __repr__(self):
     return self.__str__()
 #gets the key of the element
 def getKey(self):
     return self._key
 #sets the key of the element
 def setKey(self,newkey):
     self._key=newkey
 #gets the value of the element
 def getValueE(self):
     return self._value
 
 def _wipe(self):
     self._key = None
     self._value = None
     self._index = None

