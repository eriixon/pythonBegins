import sys

file = str(sys.argv[1])

class FileReader:
    def __init__(self, file):
        self.address = file

    def read(self):
        try:
            with open(self.address) as f:
                return f.read().replace('\n', '')
        except IOError:
            return ''

reader = FileReader(file)
print(reader.read())
