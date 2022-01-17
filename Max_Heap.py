class Max_Heap:
    def __init__(self):
        self.Heap_List = []
        self.current_size = 0
        self.flag = False

    def insert(self, value):
        self.Heap_List.append(value)
        self.current_size = self.current_size + 1
        self.Shift_Up(self.current_size-1)
    def Shift_Up(self, index):
        while index != 0:
            if self.Heap_List[index] > self.Heap_List[(index) // 2]:
                self.Heap_List[index], self.Heap_List[(index) // 2] = self.Heap_List[(index) // 2], self.Heap_List[index]
            index = index//2
    def Shift_Down(self, index):
        if (index*2)+2 <= self.current_size and index <= self.current_size//2:
            value = self.Max_Child(index)
            if self.Heap_List[index] < self.Heap_List[value]:
                self.Heap_List[index], self.Heap_List[value] = self.Heap_List[value], self.Heap_List[index]
                self.Shift_Down(value)
    def Max_Child(self, i):
        if self.Heap_List[(i*2)+1] > self.Heap_List[(i*2)+2]:
            return (i * 2) + 1
        else:
            return (i * 2) + 2
    def Delete(self):
        Return_Value = self.Heap_List[0]
        self.Heap_List[0] = self.Heap_List[self.current_size-1]
        self.current_size = self.current_size - 1
        self.Heap_List.pop()
        self.Shift_Down(0)
        return Return_Value
    
    def get_values(self):
        return self.Heap_List
    
    def Search_Values(self,k):
        for i in self.Heap_List:
            if k == i:
                self.flag = True
                return
    def Display(self):
        print("a. Insert (add a value in the heap)")
        print("b. search (search an element from the heap )")
        print("c. delete (to delete a value from heap )")
        print("d. display elements of heap.")
        Heap = Max_Heap()
        while True:
            choice = input("pleased enter your choice from a,b,c,d,e,f,g,s,h: ") 
            if choice == "a":
                loop = input("enter how many time you want to insert value: ")
                for i in range(int(loop)):
                    N = int(input("please enter the value for value: "))
                    Heap.Insert_Value(N)
            if choice == "b":
                value = int(input("enter the value which you want to seach in heap: "))
                Heap.Search_Values(value)
                if Heap.flag:  
                    print("value exists in the heap")  
                else:  
                    print("value does not exist in the heap") 
            if choice == "c":
                Value = int(input("Enter the node which you want to delete from Binary tree: "))
                print(Heap.Delete(Value))
                print(Heap.get_values())
            if choice == 'd':
                print(Heap.get_values())
heap = Max_Heap()
# heap.insert(23)
# heap.insert(56)
# heap.insert(34)
# heap.insert(21)
# heap.insert(11)
# heap.insert(67)
# heap.insert(2)
# heap.insert(67)
# heap.insert(98)
# heap.insert(101)
# heap.insert(45)
# heap.insert(23)
# print(heap.get_values())
heap.Display()
