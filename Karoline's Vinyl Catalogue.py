import pandas as pd


catalogue = pd.read_csv("Karoline's Vinyl Catalogue.csv")
print(catalogue.head())
print(catalogue.info())


alanis = ["Alanis Morissette", "Jagged Little Pill", 1995]
beaches = ["Beaches, The", "Blame My Ex", 2023]


catalogue.loc[len(catalogue)] = alanis
print(catalogue.tail())


catalogue.loc[len(catalogue)] = beaches
print(catalogue.tail())


catalogue = catalogue.sort_values("Artist")
catalogue = catalogue.reset_index(drop=True)
print(catalogue.head(n=10))


catalogue.to_csv("Karoline's Vinyl Catalogue.csv")
