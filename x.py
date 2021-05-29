import json

data = open('_annotations.coco.json', 'r')
data = data.read()
data = json.loads(data)

json_list = data['annotations']

# category_id = json_list[i].get('category_id')
# area = json_list[i].get('area')

list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
list_8 = []
list_9 = []
list_10 = []

for i in range(len(json_list)):
    print('IMG',json_list[i].get('category_id'), json_list[i].get('area'))
    if json_list[i].get('category_id') == 1:
        list_1.append(json_list[i].get('area'))
    elif json_list[i].get('category_id') == 2:
        list_2.append(json_list[i].get('area'))
    elif json_list[i].get('category_id') == 3:
        list_3.append(json_list[i].get('area'))
    elif json_list[i].get('category_id') == 4:
        list_4.append(json_list[i].get('area'))
    elif json_list[i].get('category_id') == 5:
        list_5.append(json_list[i].get('area'))
    elif json_list[i].get('category_id') == 6:
        list_6.append(json_list[i].get('area'))
    elif json_list[i].get('category_id') == 7:
        list_7.append(json_list[i].get('area'))
    elif json_list[i].get('category_id') == 8:
        list_8.append(json_list[i].get('area'))
    elif json_list[i].get('category_id') == 9:
        list_9.append(json_list[i].get('area'))
    elif json_list[i].get('category_id') == 10:
        list_10.append(json_list[i].get('area'))

print(list_1)