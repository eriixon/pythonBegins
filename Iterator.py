class MyIterator:
    def __init__(self, top):
        self.top = top
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.top:
            raise StopIteration
        current = self.current
        self.current+=1
        return current

iterator = MyIterator(5)

for i in iterator:
    print(i)