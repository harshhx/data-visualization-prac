import seaborn
import matplotlib.pyplot as plt


# df = seaborn.load_dataset("tips")
# df_corr = df.corr()

flights = seaborn.load_dataset("flights")
flight_pivot = flights.pivot_table(index="month",columns="year",values="passengers")


# seaborn.barplot(x= "sex" , y="total_bill", data=df)
# seaborn.countplot(x="time", data = df)
# seaborn.boxplot(x="day" , y="total_bill",data=df,hue="sex")
# seaborn.violinplot(x="day",y="total_bill",data=df,hue="sex",split=True)
# seaborn.displot(df["total_bill"],kde=True)
# seaborn.kdeplot(df["total_bill"])
# seaborn.jointplot(x="total_bill" , y = "tip",data=df,kind="hex")
# seaborn.pairplot(df,hue="sex")
# seaborn.heatmap(df_corr,annot=True)
seaborn.heatmap(flight_pivot,cmap="coolwarm")
plt.show()
