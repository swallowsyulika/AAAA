
frame_filename = "test_frame.txt"
content_filename = "test_content.txt"

map_dic = {}
change_dic = dict(zip("aeiou", "!@#$%"))

with open(frame_filename) as f:
    raws = [x.strip().split("_") for x in f.readlines()]
    for raw in raws:
        map_dic[raw[0]] = [raw[1], raw[2]]


with open(content_filename) as f:
    raws = [x.strip().split("_") for x in f.readlines()]
    for raw in raws:
        map_dic[raw[0]].append(raw[1])

### ================================= ###

for key_id in map_dic.keys():
    value = abs(int(map_dic[key_id][0]) - int(map_dic[key_id][1]))

    if value % 2 == 0:
        # "_"
        content = list(map_dic[key_id][2])
        content = "_".join(content)
        
    elif value % 5 == 0:
        # " "
        content = list(map_dic[key_id][2])
        content = " ".join(content)
        
    elif value % 7 == 0:
        # aeiou -> !@#$%
        content = map_dic[key_id][2]
        for ele in change_dic.keys():
            content = content.replace(ele, change_dic[ele])
    else:
        content = map_dic[key_id][2]


    tmp = map_dic[key_id]
    tmp.insert(0, key_id)
    tmp.insert(3, content)
    print("_".join(tmp))
    
