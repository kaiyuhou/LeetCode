# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:59:35 2015

@author: Mike
"""

class Queue(object):
    def __init__(self):
        self.queue = []
        self.tmp = []
        
    def push(self, x):
        while self.tmp:
            self.queue.append(self.tmp.pop())
        self.queue.append(x)
    
    def pop(self):
        while self.queue:
            self.tmp.append(self.queue.pop())
        self.tmp.pop()
        
    def peek(self):
        while self.queue:
            self.tmp.append(self.queue.pop())
        return self.tmp[-1]

    def empty(self):
        return self.queue == [] and self.tmp == []

sln = Queue()
print sln.empty()
sln.push(1)
print sln.peek()
sln.push(2)
print sln.peek()
sln.push(3)
print sln.peek()
sln.pop()
print sln.peek()
print sln.empty()