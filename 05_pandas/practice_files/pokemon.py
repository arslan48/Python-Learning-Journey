import pandas as pd
pokemon = ["Bulbasaur","Lvysaur","Venusaur","Charmander","Charmeleon","Charizard"]
s = pd.Series(pokemon,index=range(1,7))
print(s)