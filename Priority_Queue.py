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
