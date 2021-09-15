#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Tham trị
# Xây dựng hàm
def tinh_binh_phuong(so):
    so = so ** 2
    print("Kết quả trong hàm:", so)
    return


# Gọi hàm
n = 10
print("Giá trị ban đầu:", n)

tinh_binh_phuong(n)

print("Giá trị ban đầu:", n)


# In[2]:


def change_list(list_so):
    list_so.append(100)
    list_so.append(200)
    print("Giá trị trong hàm:", list_so)
    return


ds_so = [3, 7, 2, 4]
print("Giá trị ban đầu:", ds_so)

change_list(ds_so)

print("Giá trị ban đầu:", ds_so)


# In[4]:


def in_loi_chao(loi_chao, mon_hoc, *danh_sach_ten):
    for ten in danh_sach_ten:
        print(loi_chao, "bạn", ten, "đến với ngôn ngữ", mon_hoc)


in_loi_chao("Chào mừng", "Python", "Lan", "Mai", "Trúc", "Đào", "Nam")


# In[5]:


def tinh_diem_tb(hk1, hk2):
    dtb = (hk1 + hk2 * 2) / 3
    return dtb


# In[6]:


def tinh_diem_tb(hk1, hk2):
    return (hk1 + hk2 * 2) / 3

tinh_diem_tb(7, 8)


# In[8]:


tinh_dtb = lambda hk1, hk2: (hk1 + hk2 * 2) / 3
print(tinh_dtb(8, 9))


# In[9]:


tinh_bmi = lambda can_nang, chieu_cao: can_nang / chieu_cao ** 2
tinh_bmi(60, 1.78)


# In[12]:


list_1 = [1, 2, 3, 4, 5]
print(list_1)
list_2 = []
for so in list_1:
    binh_phuong = so ** 2
    list_2.append(binh_phuong)
print(list_2)


# In[14]:


list_1 = [1, 2, 3, 4, 5]
print(list_1)
list_2 = list(map(lambda so: so ** 2, list_1))
print(list_2)


# In[15]:


def tinh_binh_phuong(so):
    return so ** 2

list_1 = [1, 2, 3, 4, 5]
print(list_1)
list_2 = list(map(tinh_binh_phuong, list_1))
print(list_2)


# In[16]:


list_1 = [1, 2, 3, 4, 5]
list_3 = [6, 7, 8, 9, 10]

list_4 = list(map(lambda gtri_1, gtri_2: gtri_1 + gtri_2, list_1, list_3))
print(list_4)


# In[17]:


list_1 = [1, 2, 3, 4, 5]
list_3 = [6, 7, 8]

list_4 = list(map(lambda gtri_1, gtri_2: gtri_1 + gtri_2, list_1, list_3))
print(list_4)


# In[18]:


list_1 = [1, 2, 3, 4, 5]
list_3 = (6, 7, 8)

list_4 = list(map(lambda gtri_1, gtri_2: gtri_1 + gtri_2, list_1, list_3))
print(list_4)


# In[21]:


list_1 = [1, 2, 3, 4, 5]
dict_1 = {"one": 6, "two": 7, "three": 8}

list_4 = list(map(lambda gtri_1, gtri_2: gtri_1 + gtri_2, list_1, dict_1))
print(list_4)


# In[22]:


list_1 = [1, 2, 3, 4, 5]
dict_1 = {1: "one", 2: "two", 3: "three"}

list_4 = list(map(lambda gtri_1, gtri_2: gtri_1 + gtri_2, list_1, dict_1))
print(list_4)


# In[23]:


from operator import add

list_1 = [1, 2, 3, 4, 5]
dict_1 = {1: "one", 2: "two", 3: "three"}

list_4 = list(map(add, list_1, dict_1))
print(list_4)


# In[25]:


from operator import sub

list_1 = [1, 2, 3, 4, 5]
dict_1 = {1: "one", 2: "two", 3: "three"}

list_4 = list(map(sub, list_1, dict_1))
print(list_4)


# In[26]:


from operator import mul

list_1 = [1, 2, 3, 4, 5]
dict_1 = {1: "one", 2: "two", 3: "three"}

list_4 = list(map(mul, list_1, dict_1))
print(list_4)


# In[27]:


from operator import truediv

list_1 = [1, 2, 3, 4, 5]
dict_1 = {1: "one", 2: "two", 3: "three"}

list_4 = list(map(truediv, list_1, dict_1))
print(list_4)


# In[31]:


chuoi = "hello ababababa"
list_ki_tu = list(chuoi)
print(list_ki_tu)
print(chuoi[1])


# In[ ]:




