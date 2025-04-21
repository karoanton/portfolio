import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


consent = pd.read_csv('Matomo Analytics Report - Have given consent.csv')
zero_sec = pd.read_csv('Matomo Analytics Report - zero sec segment.csv')


# Inspect 'consent' database
print(consent.head())
print(consent.info())


# Add "Consent" column
consent["Consent"] = 'y'


# Inspect 'zero sec' database
print(zero_sec.head())
print(zero_sec.info())


# Delete 'zero sec - ' from 'zero sec' database headings
zero_sec.columns = zero_sec.columns.str.lstrip('zero sec -')
print(zero_sec.info())


# Transform "Actions/Visit" column in 'zero sec' to float
zero_sec['Actions/Visit'] = zero_sec['Actions/Visit'].apply(lambda x: float(x))
print(zero_sec.info())


# Add "Consent" column
zero_sec["Consent"] = 'n'


# Add new rows featuring new data
consent.loc[len(consent)] = ['31-Mar', '06-Apr', 25, 20, '3:23', 98, 13, 3.9, 85, 'y']
consent.loc[len(consent)] = ['07-Apr', '13-Apr', 9, 9, '4:44', 45, 10, 5, 42, 'y']
zero_sec.loc[len(zero_sec)] = ['31-Mar', '06-Apr', 148, 148, '0:00', 148, 1, 1, 148, 'n']
zero_sec.loc[len(zero_sec)] = ['07-Apr', '13-Apr', 87, 87, '0:00', 87, 1, 1, 87, 'n']


# Join 'consent' and 'zero sec' databases
analytics = pd.concat([consent, zero_sec], ignore_index=True)
print(analytics.head())
print(analytics.info())


# Create bar plot showing unique visitors over time
sns.set_theme()
sns.catplot(data=analytics, kind='bar', x='Start Date', y='Unique Visitors', hue='Consent')
plt.title('Unique Visitors Distribution')
x_labels = ['Dec', 'Jan', 'Feb', 'Mar', 'Apr']
x_ticks = np.arange()
ax = plt.subplot()
ax.set_xticks()
plt.show()
