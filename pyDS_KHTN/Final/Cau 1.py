tu_dien = {"man": ["đàn ông"], "woman": ["đàn bà", "phụ nữ"],
           "house": ["nhà", "ngôi nhà", "căn nhà"], "sun": ["mặt trời"],
           "moon": ["mặt trăng"], "earth": ["trái đất", "quả đất", "địa cầu"],
           "mountain": ["núi", "ngọn núi"]}


list_keys = list()
for i in tu_dien.keys():
    list_keys += [i]

import random
while True:
    so = random.randrange(0,len(list_keys),1)
    guess = input("Bạn hãy cho biết '%s' có nghĩa là gì?\n" %list_keys[so])
    if guess in tu_dien[list_keys[so]]: # vì Value là 1 list nên cần dùng "in"
        print("Bạn đã đoán đúng")
    else:
        print("Bạn đã đoán sai. Nghĩa của từ %s phải là:\n%s" %(list_keys[so],tu_dien[list_keys[so]]))

    ask = input("Bạn có muốn tiếp tục không (y/n)? --> ")
    if ask == "y":
        continue
    else:
        print("Đã kết thúc!")
        break