import json




if __name__=="__main__":
    data = []
    with open("./dataset/VSDv1/val.json") as f:
        data = json.load(f)
    offset=0
    for i in range(len(data)):
        img_id=data[i-offset]["img_id"]
        if "png" not in img_id and "jpg" not in img_id:
            del data[i-offset]
            offset+=1

    print("data remain:{}".format(len(data)))

    with open('./dataset/VSDvv1/val.json', 'w+') as f:
        json.dump(data, f)




