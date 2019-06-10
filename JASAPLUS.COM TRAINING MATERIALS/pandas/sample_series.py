#!/usr/bin/env python3

import numpy as np 
import pandas as pd
data = np.array([1,2,3])
seri1 = pd.Series(data)
print(seri1)

print("=" * 20)

data2 = [1,2,3]
seri2 = pd.Series(data2)
print(seri2)
