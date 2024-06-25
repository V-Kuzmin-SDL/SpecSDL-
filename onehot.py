'''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

import random
import pandas as pd

# coding: utf-8 
   
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходные данные:")
print(data.head())

                             # Преобразование в one-hot вид
one_hot_data = pd.DataFrame()

for category in data['whoAmI'].unique():
                                         # Создаем столбцы для каждой категории и заполняем их 1 и 0
    one_hot_data[category] = (data['whoAmI'] == category).astype(int)

one_hot_data = one_hot_data.reset_index(drop=True)
print("\nOne-hot вид:")
print(one_hot_data.head())
