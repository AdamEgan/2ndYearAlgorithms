from Element import Element
#Adam Egan 115359356
#Heap class underlying structure of APQ
class Heap(object):
    def __init__(self):
        self.heap=[]
        self.size=0
    #Prints out heap
    def HeapPrint(self):
        print(self.heap)
    #Returns length of the heap list
    def getSize(self):
        return len(self.heap)
    #Returns top element
    def topElement(self):
        return self.heap[0]
    #Returns heap list
    def returnHeap(self):
        return self.heap
    #Adds item to heap
    def AddHeap(self,num):
        if self.getSize()==0:
                self.heap+=[num]
                self.size+=1
        else:
                self.heap+=[num]
                self.size+=1
                index=len(self.heap)-1
                self._bubbleUp(self.heap,index)
    #Bubbles up element using index
    def _bubbleUp(self,lst,index):
        while lst[index]<lst[(index-1)//2] and index!=0:
                lst[index],lst[(index-1)//2]=lst[(index-1)//2],lst[index]
                store=lst[index].getElement()
                lst[index].setElement(lst[(index-1)//2].getElement())
                lst[(index-1)//2].setElement(store)
                index=(index-1)//2
    #Removes top element in the list
    def removeTop(self):
        if self.getSize()>1:
            self.heap[0],self.heap[self.size-1]=self.heap[self.size-1],self.heap[0]
            self.heap[0].setElement(self.heap[self.size-1].getElement())
            self.heap[self.size-1].setElement(0)
            toRemove=self.heap.pop()
            self.size-=1
            self._bubbledown(0)
            return toRemove
        else:
            toRemove=self.heap.pop()
            self.size-=1
            return toRemove
    
        
    #bubbles down element using index
    def _bubbledown(self,index):
        if (2*index)+2<self.size-1 or(2*index)+1<self.size-1:
            if self.heap[(2*index)+1].getKey()<=self.heap[(2*index)+2].getKey():
                self.heap[index],self.heap[(2*index)+1]=self.heap[(2*index)+1],self.heap[index]
                store=self.heap[index].getElement()
                self.heap[index].setElement(self.heap[(2*index)+1].getElement())
                self.heap[(2*index)+1].setElement(store)
                index=(2*index)+1
            elif self.heap[(2*index)+2].getKey()<self.heap[(2*index)+1].getKey():
                self.heap[index],self.heap[(2*index)+2]=self.heap[(2*index)+2],self.heap[index]
                store=self.heap[index].getElement()
                self.heap[index].setElement(self.heap[(2*index)+2].getElement())
                self.heap[(2*index)+2].setElement(store)
                index=(2*index)+2
            self._bubbledown(index)
        else:
            return self.heap
def main():
    heap=Heap()
    heap.AddHeap(12)
    heap.AddHeap(14)
    heap.AddHeap(44)
    heap.AddHeap(77)
    heap.AddHeap(22)
    heap.AddHeap(56)
    heap.HeapPrint()
    heap.removeTop()
   
    heap.HeapPrint()
    heap.removeTop()
    heap.HeapPrint()
    heap.removeTop()
    heap.HeapPrint()
    heap.AddHeap(10)
    heap.HeapPrint()
    
if __name__=='__main__':
    main()
