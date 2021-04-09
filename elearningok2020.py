#-.-coding:utf-8-*-
#2020. évben e-learningokért pontot kapott felhasználók napi lebontásba
import pandas as pd
import matplotlib.pyplot as plt


kepzes2019="https://raw.githubusercontent.com/tobibaby/kepzesek/main/elearning2019.csv" #a forrás hozzáadás
kepzes2020="https://raw.githubusercontent.com/tobibaby/kepzesek/main/elearning2020.csv" #a forrás hozzáadás

df2019=pd.read_csv(kepzes2019)  #az adatok hozzárendelése a változóhoz
df2020=pd.read_csv(kepzes2020)

#print(df2020)

ax = plt.gca() #ax definiálása, hogy a három vonal külön színezhető legyen.



#--------------------------------------------------Adatok kiválasztása egyenként és színezése

#df2019.plot(kind='line',x='NAP',y='OVF', color="red",ax=ax )
df2019.plot(kind='line',y='RVTV',label="RVTV 2019", color="red",ax=ax)


#df2020.plot(kind='line',x='NAP',y='OVF', color="red" ,ax=ax) 
df2020.plot(kind='line',y='RVTV',label="RVTV 2020", color="blue" ,ax=ax)
#df2020.plot(kind='line',x='NAP',y='RIASZ',color="yellow",ax=ax)
#--------------------------------------------------

#df2020.plot(kind='line',x='NAP')



plt.show() #adat megjelenítése