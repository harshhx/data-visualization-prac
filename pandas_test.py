import pandas as pd
import numpy as np

pokemon = dict(Pokemon_Height=np.random.randint(100, 300, 5), Pokemon_Weight=np.random.randint(200, 600, 5), Pokemon_Power=np.random.randint(400, 800, 5))
table = pd.DataFrame(pokemon)
print(table.head())
table.to_csv("pokemon_data.csv",index=False)
fromCSV = pd.read_csv("pokemon_data.csv")
print(fromCSV.head())
print(fromCSV.shape)

