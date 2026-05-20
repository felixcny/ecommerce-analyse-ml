import pandas as pd

df_orders = pd.read_csv('data/orders.csv')
df_customers = pd.read_csv('data/customers.csv')
df_products = pd.read_csv('data/products.csv')


# supprime doublons
df_orders = df_orders.drop_duplicates()
df_customers = df_customers.drop_duplicates()
df_products = df_products.drop_duplicates()

# gestion de l'age manquant dans customers
median_age = df_customers['age'].median()
df_customers['age'] = df_customers['age'].fillna(median_age)

# bon format des dates
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'], errors='coerce')
df_customers['signup_date'] = pd.to_datetime(df_customers['signup_date'], errors='coerce')

# supprime ligne qui posait pb
df_orders = df_orders.dropna(subset=['order_date'])

# standarisation des noms de caté
df_products['category'] = df_products['category'].str.lower().str.strip()


# fusion des dataset
df_merged = pd.merge(df_orders, df_customers, on='customer_id', how='left')
df_merged = pd.merge(df_merged, df_products, on='product_id', how='left')

#  cree colonne revenu
df_merged['revenue'] = df_merged['quantity'] * df_merged['unit_price']

# mise a l'échelle jour et mois
df_merged['order_day_of_week'] = df_merged['order_date'].dt.day_name() 
df_merged['order_month'] = df_merged['order_date'].dt.month

# petite verif
print("\n--- APERÇU DU DATASET FINAL NETTOYÉ ---")
print(df_merged.head())
print("\n--- INFOS DU DATASET FINAL ---")
df_merged.info()

# sauvegarde du dataset
df_merged.to_csv('data/clean_dataset.csv', index=False)
print("\n✅ Fichier 'clean_dataset.csv' sauvegardé")