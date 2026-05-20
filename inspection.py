import pandas as pd

# Chargement des données (en supposant qu'elles sont dans le dossier 'data/' comme convenu)
df_orders = pd.read_csv('data/orders.csv')
df_customers = pd.read_csv('data/customers.csv')
df_products = pd.read_csv('data/products.csv')

# Inspection de la structure et des valeurs manquantes pour chaque DataFrame
print("--- INFO ORDERS ---")
df_orders.info()
print("\nValeurs manquantes Orders :\n", df_orders.isnull().sum())

print("\n--- INFO CUSTOMERS ---")
df_customers.info()
print("\nValeurs manquantes Customers :\n", df_customers.isnull().sum())

print("\n--- INFO PRODUCTS ---")
df_products.info()
print("\nValeurs manquantes Products :\n", df_products.isnull().sum())