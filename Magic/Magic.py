import os
import tempfile

class File:
    def __init__(self, file_path):
        self.file_path = file_path
        z = os.path.isfile(file_path)
        if not z:
            path = tempfile.gettempdir()
            new_path = os.path.join(path, 'file.txt')
            with open(new_path, 'w+') as f:
                f.write("Hello from {} \n".format(file_path))
                f.write("Temp dir {}\n".format(path))
                f.write("Bye \n")
            self.file_path = new_path
        self.file_dict = self.getDictonary()

    def __add__(self, other):
        file_context = self.file_dict + other.file_dict
        new_file_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        with open(new_file_path, 'w') as f:
            for line in file_context:
                f.write(line)
        return File(new_file_path)

    def __str__(self):
        return self.file_path

    def __getitem__(self, index):
        return self.file_dict[index]

    def getDictonary(self):
        with open(self.file_path, 'r') as f:
            return f.read().splitlines()

    def write(self, line):
        with open(self.file_path, 'w') as f:
            f.write(line)

# file = "file.txt"
# obj = File(file)
# print(obj)
# obj.write('line\n')

first = File('temp/file1.txt')
print ("First file:")
for line in first:
    print(line)

print ("Second file:")
second = File('file2.txt')
for line in second:
    print(line)
#
print ("Last file:")
new_obj = first + second
for line in new_obj:
    print(line)