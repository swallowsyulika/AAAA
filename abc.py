
frame_filename = "test_frame.txt"
content_filename = "test_content.txt"

frame_dic = {}
content_dic = {}
change_dic = dict(zip("aeiou", "!@#$%"))

with open(frame_filename) as f:
    raws = [x.strip().split("_") for x in f.readlines()]
    for raw in raws:
        frame_dic[raw[0]] = [raw[1], raw[2]]


with open(content_filename) as f:
    raws = [x.strip().split("_") for x in f.readlines()]
    for raw in raws:
        content_dic[raw[0]] = raw[1]

### ================================= ###

for key_id in frame_dic.keys():
    value = abs(int(frame_dic[key_id][0]) - int(frame_dic[key_id][1]))

    if value % 2 == 0:
        # "_"
        content = list(content_dic[key_id])
        content = "_".join(content)
        
    elif value % 5 == 0:
        # " "
        content = list(content_dic[key_id])
        content = " ".join(content)
        
    elif value % 7 == 0:
        # aeiou -> !@#$%
        content = content_dic[key_id]
        for ele in change_dic.keys():
            content = content.replace(ele, change_dic[ele])
    else:
        content = content_dic[key_id]

    content = content + "_" + content_dic[key_id]

    tmp = [key_id]
    tmp.extend(frame_dic[key_id])
    tmp.append(content)
    print("_".join(tmp))
    
