class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_dict = self.getDictonary()

    def __str__(self):
        return self.file_path

    def __getitem__(self, index):
        return self.file_dict[index]

    def getDictonary(self):
        with open(self.file_path, 'r') as f:
            return f.read().splitlines()

    def write(self, line):
        with open(self.file_path, 'a') as f:
            f.write(line)

file = "file.txt"
obj = File(file)

print(obj)

obj.write('line\n')

for line in obj:
    print(line)