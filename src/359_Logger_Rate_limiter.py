from typing import *


class Logger:

    def __init__(self):
        self.records = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.records.keys():
            self.records[message] = timestamp
            return True

        if timestamp - self.records[message] < 10:
            return False

        self.records[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)