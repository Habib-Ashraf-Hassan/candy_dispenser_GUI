def sort_pq(pq):
    n = len(pq)
    for i in range(0, n-1):
        for j in range(i, n):
            if pq[i][0] <= pq[j][0]:
                pq[i], pq[j] = pq[j], pq[i]  #swap

    return pq            


class Priority_queue:
    def __init__(self):
        self.pq = []
    
    def add(self, k, v):
        self.item = [k, v]
        self.pq.append(self.item)
        self.pq = sort_pq(self.pq)

    def first_item(self):
        return self.pq[0]
    
    def remove_first(self):
        return self.pq.pop(0)
    
    def is_empty(self):
        return len(self.pq) == 0
    
    def get_length(self):
        return len(self.pq)
    
    def get_pq(self):
        return self.pq
    

my_pq = Priority_queue()
print(my_pq.is_empty())
print("---------------")
my_pq.add(12, "Abdul")
print(my_pq.get_pq())
print("------------")
my_pq.add(20, "Fufu")
my_pq.add(10, "bob")
my_pq.add(33, "zainab")
my_pq.add(30, "Riziki")
print(my_pq.get_pq())
print("--------")
print(my_pq.first_item())
my_pq.remove_first()
print(my_pq.first_item())
print(my_pq.get_pq())
print(my_pq.get_length())
print(my_pq.is_empty())

