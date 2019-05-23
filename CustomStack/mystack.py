

class stack(object):
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None


if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    print(s.stack)
