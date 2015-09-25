Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

### 题目
使用栈来实现队列

### 题解
使用两个栈来实现。
最裸的想法是2N的时间，其实可以保证三个操作的时间都是N