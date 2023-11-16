import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["İsim","Soyisim","SSN","Test1","Test2","Test3",
                  "Test4","Final","Sonuç"]
print(notlar)
print(type(notlar))
print(notlar.head())
print(notlar.tail())
print(notlar["Final"])
print(notlar.iloc[2])

print(notlar[1:10])


# Indexing and Slicing

print(notlar.loc[:,"İsim"])
print(notlar.loc[:5, "İsim"])
print(notlar.loc[:5, "İsim":"Test4"])
print(notlar.loc[:5, ["İsim","Soyisim","Test4"]])


# FİLTER

films = pd.read_csv("imdb_1000.csv")
print(films.columns)
print(films.head())
print(films["title"].head())
print(films.title.head())
print(films[["title","star_rating"]].head())
print(films[:9][["title","star_rating"]].head())
print(films[(films["star_rating"]>=8.5)&(films["star_rating"]<=9.0)][["title","star_rating"]])

# QUERY

print(films.query("star_rating>=9.0 & star_rating<=9.2")[["title","star_rating"]])


# GROUPBY

print(films.star_rating.mean())
print(films.groupby("genre").star_rating.mean())

# DROP
print(films.drop("content_rating",axis=1).head().columns)
films = films.drop("actors_list",axis=1)
print(films)
    

film = films.drop(2,axis=0)
print(films)

rowsToDrop = [0,1,2,3,4,5,6,7,8]
films = films.drop(rowsToDrop,axis=0)
print(films)


# MİSSİNG DATA

url = "http://bit.ly/uforeports"

data = pd.read_csv(url)
print(data[["City","Colors Reported","Shape Reported","State","Time"]].head())
print(data.columns)

print(data.isnull().head(100))
print(data.notnull().head(100))
print(data.isnull().sum())
print(data[data.City.isnull()])


# DROPNA

print(data.shape)
#data = data.dropna()
#data = data.dropna(subset=["City","Colors Reported"],how="any")


#FİLLNA

data["Shape Reported"].fillna(value="Belirsiz", inplace=True)
print(data["Shape Reported"].value_counts(dropna=False))
print(data.shape)



# STRİNG METHODS

import pandas as pd

data1 = {
    "id": [1,2,3,4],
    "ad": ["Engin","Derin","Salih","Mehmet"],
    "soyad": ["Demiroğ","Demiroğ","Demiroğ","Kaya"]
    }

data2 = {
    "id": [1,3,4,7],
    "ad": ["Ayşe","Ali","Ahmet","Cemal"],
    "soyad": ["Demiroğ","Demiroğ","Demiroğ","Kaya"]
    }

data1Df = pd.DataFrame(data1)
data2Df = pd.DataFrame(data2)

print(data1Df)
print(data2Df)


print(pd.merge(data1Df,data2Df, on="id",how ="inner"))
print(pd.merge(data1Df,data2Df, on ="id",how="left"))
print(pd.merge(data1Df,data2Df, on ="id",how="right"))

# CONCAT

print(pd.concat([data1Df,data2Df],axis =1))























