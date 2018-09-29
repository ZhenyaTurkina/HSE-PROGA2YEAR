
# coding: utf-8

# # комментарий
# 
# здесь мог бы быть ваш код

# In[82]:

#comment
print ('Hello!')


# In[83]:

json_string = """{"summer": "books",
                    "books": [
                    {"jules_verne": "earth", "chekhov": "dame"},
                    {"jules_verne": "captain", "chekhov": "fat"},
                    {"jules_verne": "fifteen", "chekhov": "joke"},
                    {"jules_verne": "matias", "chekhov": "chameleon"}
                    ], 
                    "school": "lessons",
                    "dance_club": "step",
                    "climbing_gym": "climbing",
                    "SoYJ": "journalistics",
                    "university": "death"
                    }"""


# In[84]:

import json

data = json.loads(json_string)
print(type(data))


# In[85]:

from pprint import pprint as pp

pp(data)


# In[86]:

for key in data:
    print(key, end = ' ')


# In[87]:

d = {"John": 21, "Kate": 20, "Bill": 27}
json_string = json.dumps(d)
print(type(json_string))


# In[88]:

print(json_string)


# In[89]:

arr = ['hello', 'world']
json_string = json.dumps(arr)
print(type(json_string)) 
print(json_string)


# In[90]:

import json
import urllib.request

user = "ZhenyaTurkina"  # пользователь, про которого мы хотим что-то узнать
url = 'https://api.github.com/users/%s/repos' % user 
# по этой ссылке мы будем доставать джейсон, попробуйте вставить ссылку в браузер и посмотреть, что там

response = urllib.request.urlopen(url)  # посылаем серверу запрос и достаем ответ
text = response.read().decode('utf-8')  # читаем ответ в строку
data = json.loads(text) # превращаем джейсон-строку в объекты питона

print(len(data))  # можно распечатать, сколько у пользователя репозиториев
for i in data:
    print(i["description"]) # и распечатать названия всех репозиториев)


# In[ ]:



