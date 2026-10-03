""" bst.py

Student: Hugo Jonsson
E-mail: Hugo8jonsson@gmail.com
Reviewed by: Shengkai
Review date: 2026-09-24
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    # def contains(self, k): # given function
    #     n = self.root
    #     while n and n.key != k:
    #         if k < n.key:
    #             n = n.left
    #         else:
    #             n = n.right
    #     return n is not None

    def contains(self, k): # Exc8: write recursive contains
        def _contains(n):
            if n is None:
                return False
            elif n.key == k:
                return True
            return _contains(n.left) if k < n.key else _contains(n.right) # om mindre än key gå vänster

        return _contains(self.root)
        
        
    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):             # Exc9     
        def _mheight(r):
            if r is None:
                return 0
            return 1 + max(_mheight(r.left), _mheight(r.right)) #tar max av höger resp vänster barns träd rekursivt
        return _mheight(self.root)

    def __str__(self):            # Exc10       
        return "<"+ ", ".join(str(x) for x in self) + ">"

    def to_list(self):            # Exc11   
        return [x for x in self]
        # Complexity of to_list:
        # theta(n) #går igenom alla värden en gång

    def to_LinkedList(self):    # Exc12
        llst = LinkedList()
        def _reverse_iter_insert(r):
            if r:
                _reverse_iter_insert(r.right) # går hela vägen höger (högsta)
                llst.insert(r.key)            # insert värde
                _reverse_iter_insert(r.left)  # utgår från där vi är och tar vänster gren av den noden
        _reverse_iter_insert(self.root)
        return llst            

        # Complexity of to_LinkedList:
        # theta(n), since we now insert values infront, which is theta(1) --> total: theta(1)*n

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):      # Exc13
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k) # går djupare i trädet tills nyckel hittas.
        elif k > r.key:
            r.right = self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                cur = r.right # loops to smallest key (choosen in the right tree (smallest of the bigger))
                while cur.left:
                    cur = cur.left
                r.key = cur.key # smallest key in right tree
                r.right = self._remove(r.right, cur.key) #removes the newly moved key from the leftmost position in the original right tree

                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above



def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    

if __name__ == "__main__":
    main()


"""
Exc14: In a binary search tree with n nodes and height h, what is the complexity in the
following scenarios:
==============================

1. Worst case of successful search
2. Worst case of unsuccessful search
theta(h) eftersom båda fallen kräver att man går igenom noderna för hela höjden för att tillslut lyckas/misslyckas.
alltså h steg resp h+1 steg.
höjden är ju däremot inte självklar och beror på trädets struktur. värsta strukturen ger h = n --> theta(n) 
Men i bästa fall för trädetsstruktur (balanserat träd) blir relationen mellan noder och höjd n = 2^h-1
--> h = log(n+1) = theta(log(n))
Bonus:
Man kan även se höjden som maximala antalet halveringar för att komma till botten, vilket från binära sökningar ger theta(log(n))
"""
