import os
import tempfile

class File:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.isfile(file_path):
            self.file_path = self.create_file()
        self.current = 0
        self.end = len(self.read_file().splitlines(True))

    def __str__(self):
        return self.file_path

    def __add__(self, other):
        context = self.read_file() + other.read_file()
        new_file_path = os.path.join(tempfile.gettempdir(), 'new_file')
        with open(new_file_path, 'w') as f:
            f.write(context)
        return File(new_file_path)

    # def __iter__(self):
    #     return self

    # def __iter__(self):
    #     with open(self.file_path, 'r') as f:
    #         while True:
    #             line = f.readline()
    #             if not line:
    #                 break
    #         return_line = yield line
    #         return return_line

    # def __next__(self):
    #     if self.current >= self.end:
    #         raise StopIteration
    #     curr_line = self.read_file().splitlines()[self.current]
    #     self.current += 1
    #     return curr_line

    def __getitem__(self, index):
        context = (self.read_file().splitlines(True)).strip()
        return context[index]

    def create_file(self):
        new_path = os.path.join(tempfile.gettempdir(), 'file')
        with open(new_path, 'w+') as f:
            f.write("Hello from {} \n We love bananas and pizza\n Bye \n".format(self.file_path))
        return new_path

    def read_file(self):
        with open(self.file_path, 'r') as f:
            return f.read().strip()

    def write(self, line):
        with open(self.file_path, 'w') as f:
            f.write(line)

first = File('file1')
print("First file:")
print(first)
for line in first:
    print(line)

second = File('file2')
print("Second file:")
print(second)
for line in second:
    print(line)

print ("Last file:")
new_obj = first + second
print(new_obj)
for line in new_obj:
    print(line)