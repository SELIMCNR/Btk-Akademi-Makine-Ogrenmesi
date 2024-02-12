# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#ders 6: kutuphaneler yüklemesi
#Kutuphaneler
import pandas as pd  # veriler için  dataframe tablo şeklinde
import numpy as np   # sayılar büyük sayılar için
import matplotlib.pyplot as plt  # çizim içn grafiklerle

#kod bolumu
#veri yükleme
veriler=pd.read_csv("chocolate.csv")  #pd.read_csv('')
 
print(veriler)

#veri ön işleme

rating = veriler[['rating']] # tablo başlığı headerı rating olan verileri getir.
print(rating)

ratingandref=veriler[['ref','company_manufacturer']] #tablo başlığı headerı ref,company_manufacturer olan verileri getir.
print(ratingandref)


#ders 8 python nesne yönelimli programlam
#nesne yönelimli programlama python
class insan:
        boy = 180 
        def kosmak(self,b):
          return b +10

Selim = insan()
print(Selim.boy)
print(Selim.kosmak(90))            

listeler =[1,3,4] #liste

#ders 9 eksik veriler
#kütüphane eklemek
from sklearn.impute import SimpleImputer

eksikVeri = pd.read_csv('Sıralama.csv')

imputer = SimpleImputer(missing_values=np.nan,strategy="mean") # eksik verileri sayıların ortalaması ile değiştirme metodu
print(eksikVeri)
yaş =eksikVeri.iloc[:,2:5].values  #yaş değişkenine tabloda 3 ve 5  satıra kadarki değerleri ekle
print(yaş)
imputer = imputer.fit(yaş[:,2:5]) # metod ile verileri doldur
yaş[:,2:5] = imputer.transform(yaş[:,2:5]) #yaş adlı değişkene veriyi aktar
print(yaş)

#ders10 kategorik

kategorikVeri= pd.read_csv('Sıralama.csv')

ülke = kategorikVeri.iloc[:,1:2].values
print(ülke)


#Kategorik veriyi sayısal değer dönüştürme
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Veriyi oku
kategorikVeri = pd.read_csv('Sıralama.csv')

# Kategorik veriyi al
ülke = kategorikVeri.iloc[:, 1:2].values

# LabelEncoder kullanarak kategorik veriyi sayısala dönüştür
le = LabelEncoder()
ülke_encoded = le.fit_transform(ülke)

# OneHotEncoder kullanarak kategorik veriyi one-hot encode et
ct = ColumnTransformer([("Country", OneHotEncoder(), [0])], remainder='passthrough')
ülke_encoded = ct.fit_transform(ülke_encoded.reshape(-1, 1))

# Sonuçları DataFrame'e dönüştür 
#ülke dataframe
sonuc = pd.DataFrame(data=ülke_encoded,index=range(14), columns=['fr', 'tr', 'us'])
print(sonuc)

#yaş dataframe
sonuc2 = pd.DataFrame(data=yaş,index=range(14),columns=['boy','kilo','yas'])
print(sonuc2)

#cinsiyet dataframe
cinsiyet=kategorikVeri.iloc[:,-1].values
print(cinsiyet)
sonuc3=pd.DataFrame(data=cinsiyet,index=range(14),columns=['cinsiyet'])
print(sonuc3)

#dataframe birleştirme
s=pd.concat([sonuc,sonuc2],axis=1)
print(s)
s2=pd.concat([s,sonuc3],axis=1)
print(s2)

#Train ve test işlemleri
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=0)

