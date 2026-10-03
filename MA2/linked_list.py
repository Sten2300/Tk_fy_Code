""" linked_list.py

Student: Hugo Jonsson
E-mail: Hugo8jonsson@gmail.com
Reviewed by: Shengkai
Review date: 2026-09-24
"""
class Person: #for Ex7
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __str__(self): # så print vet hur representation ser ut
        return f'{self.name}:{self.pnr}'

class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __contains__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Exc1
        cur = self.first
        count = 0
        while cur:
            count += 1
            cur = cur.succ
        return count

    def remove_last(self):        # Exc2
        if self.first is None:
            raise ValueError("Cannot remove from empty list")

        if self.first.succ is None:
            data, self.first = self.first.data, None
            return data

        cur = self.first
        while cur.succ.succ:
            cur = cur.succ
        data = cur.succ.data
        cur.succ = None
        return data

    def remove(self, x):          # Exc3
        if self.first is None: # tom lista
            return False

        if self.first.data == x: # första element är korrekt
            self.first = self.first.succ
            return True

        cur = self.first
        while cur.succ: # för element >2.
            if cur.succ.data == x:
                cur.succ = cur.succ.succ
                return True
            elif cur.succ.data > x:
                return False #listan är sorterad så kommer inte hitta mindre värde.
            cur = cur.succ
        return False


    def to_list(self):            # Exc4
        cur = self.first
        def _concate(cur):
            if cur is None:
                return []
            return [cur.data] + _concate(cur.succ)
        return _concate(cur)
        
    def __str__(self):            # Exc5
        return "(" + ', '.join(str(val) for val in self) + ")"

    # def copy(self):
    #     result = LinkedList()
    #     for x in self:
    #         result.insert(x)
    #     return result
        # Complexity for this implementation:
        #  theta(n^2)

    def copy(self):               # Exc6, should be more efficient
        result = LinkedList()
        if self.first is None:
            return result

        result.first = LinkedList.Node(self.first.data, None)
        prev = result.first

        cur = self.first.succ
        while cur:
            prev.succ = LinkedList.Node(cur.data, None)
            prev = prev.succ 
            cur = cur.succ

        return result
    ##    # Complexity for this implementation:
    ##    # theta(n)



def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    # Test code:
    print("--- plist sort på namn ---")
    plist = LinkedList()
    p = Person("Bob", 1)
    q = Person("Anna", 2)
    r = Person("Charlie", 3)
    plist.insert(p)
    print(plist)
    plist.insert(q)
    plist.insert(r)
    print(plist)









if __name__ == '__main__':
    main()
