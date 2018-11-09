import warnings
warnings.filterwarnings('ignore')
import os

os.chdir(r'C:\Users\赵前进\Desktop\结业项目 Due10.25')
import pandas as pd
pd.set_option('display.max_columns', 1000)
data = pd.read_csv('houseInfo_2018_09_10.csv')

print(data.head())
df = data.sample(10000)

# df.to_csv("data_sam.csv")



