from operator import itemgetter

data = "palm.cpu 0.5 1150864247\npalm.cpu 0.5 1150864248\neardrum.cpu 3.0 1150864250\neardrum.cpu 4.0 1150864251\neardrum.memory 4200000.0 1503320872"
data_list = [l.split() for l in data.split("\n")]
print(data_list)

serv_dic = {}
for section in data_list:
    key = section[0]
    value = float(section[1])
    timestamp = int(section[2])
    #print("{} ts {} val {}".format(key, timestamp, value))
    if key in serv_dic:
        serv_dic[key] = serv_dic[key] + [(timestamp,value)]
    else:
        serv_dic[key] = [(timestamp,value)]

for key,value in serv_dic.items():
    value.sort(key=itemgetter(1))

print(serv_dic)