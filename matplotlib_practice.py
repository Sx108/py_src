import matplotlib.pyplot as plt

foods = ['Meat','Banana','Avocados','Sweet Potatoes','Spinach','Watermelon','Coconut Water','Beans','Legumes','Tomato']
calories = [250,130,140,120,20,20,10,50,40,19]
potassium = [40,55,20,30,40,32,10,26,25,20]
fat = [8,5,3,6,1,1.5,0,2,1.5,2.5]

#LINE GRAPH
'''
plt.figure(figsize=(15,8),dpi=200)
plt.title('FOOD CHART')
plt.plot(foods,calories,label='Calories',marker='o',linestyle='dashed',linewidth=2,color='blue',markerfacecolor='blue',markersize=10)
plt.plot(foods,potassium,label='Potassium',marker='v',linestyle='dotted',linewidth=2,color='red',markerfacecolor='red',markersize=10)
plt.plot(foods,fat,label='Fat',marker='x',linestyle='dashdot',linewidth=2,color='green',markerfacecolor='green',markersize=10)
plt.legend()
plt.xlabel('Foods')
plt.ylabel('per 1000gm')
plt.savefig('food_chart.png')
plt.show()
'''

#BAR GRAPH

plt.figure(figsize=(15,8),dpi=200)
plt.bar(foods,calories, label='Calories',color='blue',width=0.5)
#plt.barh(foods,calories,label='Calories',color='blue') #BARH : HORIZONTAL BARS
plt.bar(foods,potassium,label='Potassium',color='red',width=0.5)
plt.bar(foods,fat,label='Fat',color='green',width=0.5)
plt.xlabel('Foods')
plt.ylabel('per 1000gm')
plt.title('FOOD CHART')
plt.legend()
plt.show()


#HISTOGRAM
#plt.hist(calories,bins='auto',label='Calories',color='blue',histtype='bar')
#plt.show()


#SCATTERPLOT
#JUST CHANGE FROM PLT.BAR TO PLT.SCATTER
'''
plt.figure(figsize=(15,8),dpi=200)
plt.title('FOOD CHART')
plt.xlabel('Foods')
plt.ylabel('per 1000gm')
plt.scatter(foods,calories,label='Calories',color='blue',marker='h')    # h : HEXAGON
plt.scatter(foods,potassium,label='Potassium',color='red',marker='p')   # p : PENTAGON
plt.scatter(foods,fat,label='Fat',color='green',marker='s')             # s : SQUARE
plt.legend()
plt.savefig('food_chart_scatterplot.png')
plt.show()
'''

#PIEGRAPH
'''
clrs = ['r','g','b','c','m','y','pink','purple','orange']
plt.figure(figsize=(15,8),dpi=200)
plt.title('PIEGRAPH OF FOOD CHART')
plt.pie(calories,labels=foods,colors=clrs,startangle=90,shadow=False,radius=1.2,explode=(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1),autopct='%1.1f%%')
plt.legend()
plt.savefig('pie_chart.png')
plt.show()
'''