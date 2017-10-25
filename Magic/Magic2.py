import os
import tempfile


class File:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.isfile(file_path):
            self.file_path = self.create_file()

    def __str__(self):
        return self.file_path

    def __add__(self, other):
        new_file_path = os.path.join(tempfile.gettempdir(), 'new_file')
        new_obl_con = self.get_content() + other.get_content()
        with open(new_file_path,'w') as f:
            f.write(new_obl_con)
        new_file_obj = File(new_file_path)
        return new_file_obj

    def __getitem__(self, index):
        return self.get_content().splitlines(False)[index]

    def create_file(self):
        file_name = self.get_file_name()
        new_path = os.path.join(tempfile.gettempdir(), file_name)
        with open(new_path, 'w+') as f:
            pass
        return new_path

    def get_file_name(self):
        path_list = self.file_path.split('/')
        return path_list[len(path_list)-1]

    def get_content(self):
        with open(self.file_path, mode='r', encoding='utf-8') as f:
            return f.read()

    def write(self, line):
        with open(self.file_path, mode='w', encoding='utf-8') as f:
            f.write(line)


first = File('file1')
print("First file:")
# first.write("Hello\n")
for line in first:
    print(line)

second = File('file2')
print("Second file:")
# second.write("world\n")
for line in second:
    print(line)

print("Last file:")
new_obj = first + second
print(new_obj)
for line in new_obj:
    print(line)