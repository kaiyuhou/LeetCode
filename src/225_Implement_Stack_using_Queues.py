# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:17:56 2015

@author: Mike
"""
import Queue

class Stack(object):
    stack = Queue.Queue()
    count = 0
    
    def __init__(self):
        self.stack = Queue.Queue();        
        self.count = 0
     
        
    def push(self, x):
        self.stack.put(x)
        for i in range(self.count):
            self.stack.put(self.stack.get())
        self.count += 1
        

    def pop(self):
        self.stack.get()
        self.count -= 1
                         
    def top(self):
        ans = self.stack.get()
        self.stack.put(ans)
        for i in range(self.count-1):
            self.stack.put(self.stack.get())
        return ans

    def empty(self):
        return self.stack.empty()
        
sln = Stack()
print sln.empty()
sln.push(1)
sln.push(2)
sln.push(3)
print sln.top()
print sln.top()
sln.pop()
print sln.top()
sln.pop()
print sln.empty()
sln.pop()
print sln.empty()