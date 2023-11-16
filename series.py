import pandas as pd
import numpy as np

data = np.array(["Ali","Ayşe","Veli"])
s = pd.Series(data,index = [1,2,3])
print(s)

data2 = {"matematik":10, "fizik":20, "beden eğitimi": 100}
s2 = pd.Series(data2, index=["fizik","matematik","beden eğitimi"])
print(s2)

s3 = pd.Series(5, index=[1,2,3,4,5])
print(s3)


# dataframe

data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)


data2 = [["Engin",33,"Ankara"],["Aysun",32,"Sinop"],["Salih",32,"Antalya"]]
df2 = pd.DataFrame(data2,columns = ["İsim","Yaş","Şehir"],index = [1,2,3])
print(df2)


data3 = {"İsim": ["Engin","Ali","Ayşe"],
         "Yaş": [33,32,32],
         "Şehir":["Ankara","Sinop","Antalya"]}
df3 = pd.DataFrame(data3, columns=["İsim","Yaş","Şehir"],index = [1,2,3])
print(df3)
print(df3["Yaş"])
#del df3["Şehir"]
#df3.pop("Şehir")
print(df3)

print(df3.loc[2])
print(df3.iloc[1])


df4 = df3.append(df2)
print(df4)







