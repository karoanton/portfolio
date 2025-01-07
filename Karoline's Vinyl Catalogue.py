import pandas as pd


catalogue = pd.read_csv("Karoline's Vinyl Catalogue.csv")
print(catalogue.head())
print(catalogue.info())


catalogue = catalogue.drop("Unnamed: 0", axis=1, inplace=True)


catalogue.to_csv("Karoline's Vinyl Catalogue.csv", index=False)
