import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key', nargs='?')
parser.add_argument('--value', nargs='?')
data = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if os.path.exists(storage_path)== False :
    with open(storage_path, 'w') as f:
        f.write('')

with open(storage_path, 'r+') as f:
    context = f.read()
    storage = {}
    if context !='':
        storage = json.loads(context)
    if(data.value != None and data.key in storage):
        storage[data.key] = "{}, {}".format(storage[data.key],data.value)
    if (data.value != None and data.key not in storage):
        storage[data.key] = data.value
    if (data.value == None and data.key in storage):
        print(storage[data.key])
    if (data.value == None and data.key not in storage):
        print('None')

    json_data = json.dumps(storage)
    f.seek(0)
    f.write(json_data)
    f.truncate()

