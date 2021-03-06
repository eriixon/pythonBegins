import os
import tempfile

class File:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.isfile(file_path):
            self.file_path = self.create_file()
        self.content = self.get_content()

    def __str__(self):
        return self.file_path

    # def __add__(self, other):
    #     f1 = self.file_path
    #     f2 = other.file_path
    #     new_file_path = os.path.join(tempfile.gettempdir(), 'new_file')
    #
    #
    #
    #     return File(new_file_path)
    #     # context = self.read_file() + other.read_file()
    #     # new_file_path = os.path.join(tempfile.gettempdir(), 'new_file')
    #     # with open(new_file_path, 'w') as f:
    #     #     f.write(context)
    #     # return File(new_file_path)
    def __add__(self, other):
        new_file_path = os.path.join(tempfile.gettempdir(), 'new_file')
        with open(new_file_path,mode='w', encoding='utf-8') as f:
            f.write(self.content.strip())
            f.write(other.content.strip())
        new_file_obj = File(new_file_path)
        return new_file_obj

    def __getitem__(self, index):
        context = self.get_content().splitlines(True)
        return context[index]

    def create_file(self):
        new_path = os.path.join(tempfile.gettempdir(), 'file')
        with open(new_path, 'w+') as f:
            f.write("Hello from {} \n We love bananas and pizza\n Bye \n".format(self.file_path))
        return new_path

    def get_content(self):
        with open(self.file_name, mode='r', encoding='utf-8') as f:
            return f.read()

    def write(self, line):
        with open(self.file_path,mode='w', encoding='utf-8') as f:
            f.write(line)

    # def __iter__(self):
    #     return self
    # def __next__(self):
    #     if self.current >= self.end:
    #         raise StopIteration
    #     curr_line = self.read_file().splitlines()[self.current]
    #     self.current += 1
    #     return curr_line

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

print("Last file:")
new_obj = first + second
print(new_obj)
for line in new_obj:
    print(line)