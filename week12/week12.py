# 교과서 181쪽
from week04.List_DS import artists


class Stack:
    def __init__(self):
        self.items = list() # self.items = [] 와 같음

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        #return self.items[-1] / 밑과 같은 뜻
        return self.items[len(self.items)-1]

subjects = Stack()
artists = Stack()
artists.push("핑클")
subjects.push("웹프로그래밍")
subjects.push("자료구조")
artists.push("SES")
print(subjects.pop()) # top에 있던 값을 리턴(언급)하고 삭제
print(subjects.peek()) # top 원소 확인
print(artists.peek())