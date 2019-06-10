#!/usr/bin/env python3
'''
sample_dataframe.py
panda dataframe sample
for training material at www.jasaplus.com
'''
import numpy as np
import pandas as pd

'''
input type : dictionary
'''
print("\tdictionary")

dict1 = {
    'id' : ['0', '1', '2'],
    'product' : ["Servo Motor", "DC Motor", "Muscle Wire"],
    'stock' : [50, 200, 20]
}
df2 = pd.DataFrame(dict1)
print(df2)

print("=" * 30)

'''
input type : list
'''
print("\tlist using from_records")

prods = [('Servo Moto', 50),
         ('DC Motor', 200),
         ('Stepper Motor', 20)]
labels = ['Product', 'Stock']
df = pd.DataFrame.from_records(prods, columns=labels)
print(df)
