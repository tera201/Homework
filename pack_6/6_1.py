import Lib
import random


class LinkedCircularList(Lib.DoublyLinkedBase):
    def __init__(self):
        self._header = Lib._Node(None, None, None)
        self._header._prev = self._header
        self._header._next = self._header
        self._size = 0

    def insert_head(self, symbols):
        self._insert_between(symbols, self._header, self._header._next)

    def delete_head(self):
        if self.is_empty():
            raise Lib.Empty('List is empty')
        else:
            self._delete_node(self._header._next)

    def insert_tail(self, symbols):
        self._insert_between(symbols, self._header._prev, self._header)

    def delete_tail(self):
        if self.is_empty():
            raise Lib.Empty('List is empty')
        else:
            self._delete_node(self._header._prev)

    def __str__(self):
        string = '['
        if self._size != 0:
            step = self._header._next
            string += str(step._element)
            while step._next._element != None:
                step = step._next
                string += ' ' + str(step._element)
        string += ']'
        return string


short = LinkedCircularList()
short.insert_head(random.randint(1, 10))
short.delete_head()
short.insert_head(random.randint(666, 777))
short.insert_tail(random.randint(30, 100))
short.delete_tail()
short.insert_tail(random.randint(666, 777))
short.insert_tail(random.randint(1, 5))
short.insert_head(random.randint(1, 5))

exam = short._header._next
print('Пример : ')
i = 0

while i < 1:
    if exam._element != None:
        print(exam._element)
    exam = exam._next
    if exam._element == None:
        i += 1
print(short)
