class Node(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val, self.next, self.prev = val, next, prev

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = Node(val = homepage)

    def visit(self, url):
        self.current.next = Node(val = url, prev=self.current)
        self.current = self.current.next

    def back(self, steps):
        while True:
            if steps == 0 or self.current.prev is None:
                break
            self.current = self.current.prev
            steps -=1
        return self.current.val
    
    def forward(self, steps):
        while True:
            if steps == 0 or self.current.next is None:
                break
            self.current = self.current.next
            steps -= 1
        return self.current.val