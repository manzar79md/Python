'''import pandas as pd
data={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df=pd.DataFrame(data)
print(df)


import matplotlib.pyplot as plt
year=[2014,2015,2016,2017,2018,2019]
englishpassper=[39,117,98,54,28,15]
ippassper=[90,60,33,66,99,84]
plt.plot(year,englishpassper,color="green",linewidth=3,label="English pass%")
plt.plot(year,ippassper,color="blue",linewidth=3,label="IP pass%")
plt.xlabel('Year')
plt.ylabel('Pass performance')
plt.legend()
plt.show()'''


import pandas as pd
df=pd.DataFrame({"Rollno":[1,2,3,4],"Name":['Arun','Deepti','Mohit','Sakhi'],"Age":[18,16,14,15]})
print(df)
M=[68,77,55,80]
df["Marks"]=M
print(df)

'''
import matplotlib.pyplot as plt
plt.bar([1,3,6,7,9],[5,2,7,8,2],label="Example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6],label="Example two",color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Epic Graph\n Another line! Whoa')
plt.show()


import pandas as pd
df=pd.DataFrame({"Rollno":[1,2,3,4,5,6],"Name":['Arun','Deepti','Mohit','Sakhi','Sruthi','Ishan'],"Age":[18,16,14,15,17,16]})
df.head(3)
df.head(1)
df.tail(3)
df.tail(1)
print(df)

import matplotlib.pyplot as plt
average_age_of_population=[10,20,20,40,40,40,40]
bins=[10,15,20,25,30,35,40,45,50]
plt.hist(average_age_of_population,bins,histtype='bar',rwidth=0.9,color="black")
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()


import pandas as pd
df=pd.DataFrame({"Rollono":[1,2,3,4],"Name":['Arun','Deepti','Mohit','Sakhi'],"Age":[18,16,14,15]})
print(df)
df.rename(columns={"Rollno":"rollno","Name":"name","Age":"age"})
print(df)


import matplotlib.pyplot as plt
import pandas as pd
girls_gr=[89,90,70,89,100,80,90,100,80,34]
boys_gr=[30,29,49,48,100,48,38,45,20,30]
df=pd.DataFrame({"Girls Grade":pd.Series(girls_gr),"Boys Grade":pd.Series(boys_gr)},columns=["Girls Grade", "Boys Grade"])
df.plot.scatter(x="Boys Grade", y="Girls Grade", color="red")
plt.title("Girls v/s Boys")
plt.show()

import pandas as pd
df=pd.DataFrame({"Rollono":[1,2,3,4],"Name":['Arun','Deepti','Mohit','Sakhi'],"Age":[18,16,14,15]})
print(df)
M=[68,77,55,80]
df["Marks"]=M
df["Remarks"]=['Nan','Nan','Nan','Nan']
print(df)

import pandas as pd
df=pd.DataFrame({"Rollono":[1,2,3,4],"Name":['Arun','Deepti','Mohit','Sakhi'],"Age":[18,16,14,15]})
print(df)
M=[68,77,55,80]
df["Marks"]=M
df["Remarks"]=['Nan','Nan','Nan','Nan']
print(df)
df.pop('Remarks')
print(df)
df.drop('Age'=80)
print(df)'''
