
from Heap import Heap
from Element import *
#Adam Egan 115359356

class PriorityQueue(object):
    def __init__(self):
        self.queue=Heap()
    #Adds element to the Apq
    def add(self,key,value):
        i=self.length()
        item=Element(key,value,i)
        self.queue.AddHeap(item)
        return item
    #Returns the minimum element
    def min(self):
        return self.queue.topElement()
    #Remove the minimum element
    def remove_min(self):
        return self.queue.removeTop()
    #Returns True if the queue is empty
    def is_empty():
        if self.queue.getSize()==0:
            return True
        else:
            return False
    #Prints out the APQ
    def print2(self):
         self.queue.HeapPrint()
    #Returns length of APQ
    def length(self):
        return self.queue.getSize()
    #Updates the key of an element in the APQ
    def update_key(self,element,newkey):
        lst=self.queue.returnHeap()
        if len(lst)-1>=element.getElement():
            element.setKey(newkey)
            if lst[(element.getElement()-1)//2]>lst[element.getElement()]:
                self.queue._bubbleUp(lst,element.getElement())
            else:
                self.queue._bubbledown(element.getElement())
        else:
            print("not in lst")
            
    #Returns key of a Key with element      
    def get_key(self,element):
        lst=self.queue.returnHeap()
        key=lst[element]
        return key.getKey()
        
    #Remove a items using element
    def remove(self,element):
        swapped=False
        lst=self.queue.returnHeap()
        for i in lst:
            
            if element==i.getElement():
                if swapped==True:
                    break
                remove=i.getElement()
                store=i.getElement()
                lst[remove].setElement(lst[self.length()-1].getElement())
                lst[self.length()-1].setElement(store)
                lst[remove],lst[self.length()-1]=lst[self.length()-1],lst[remove]
                swapped=True
                swapper=lst[store]
                if swapper.getKey()< lst[(store-1)//2].getKey():
                    self.queue._bubbleUp(lst,store())
                else:
                    self.queue._bubbledown(store)
                delete=lst[self.length()-1]
                lst.pop()
        return delete
            
                
                
            
        
        


def main():
    pass
if __name__=='__main__':
    main()
    p1=PriorityQueue()
    p1.add(8,5)
    p1.add(9,1)
    p1.add(10,3)
    p1.print2()
    p1.remove_min()
    p1.print2()

        
