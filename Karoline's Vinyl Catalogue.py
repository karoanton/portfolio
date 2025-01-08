import pandas as pd


catalogue = pd.read_csv("Karoline's Vinyl Catalogue.csv")
print(catalogue.head())
print(catalogue.info())


# Deletes "Unnamed: 0" and so on columns
catalogue = catalogue.drop(catalogue.columns[[0, 1, 2]], axis=1)
catalogue = catalogue.reset_index()
print(catalogue.info())

catalogue.to_csv("Karoline's Vinyl Catalogue.csv", index=False)
