import pandas as pd
import matplotlib.pyplot as plt

# Charger le dataset
df = pd.read_csv("data/clean_dataset.csv")
# Afficher les premières lignes
print(df.head())

# Infos générales
print(df.info())

# Statistiques
print(df.describe())

# Ajouter le profit
df["profit"] = df["revenue"] - df["cost"]

print("\nChiffre d'affaires total :", df["revenue"].sum())
print("Coût total :", df["cost"].sum())
print("Profit total :", df["profit"].sum())

print("\nTop catégories par profit :")
print(df.groupby("category")["profit"].sum().sort_values(ascending=False))

print("\nTop marques par profit :")
print(df.groupby("brand")["profit"].sum().sort_values(ascending=False))

print("\nMéthodes de paiement :")
print(df["payment_method"].value_counts())

# =========================
# Graphique 1 : Revenue par ville
# =========================

city_revenue = df.groupby("city")["revenue"].sum()

plt.figure(figsize=(8,5))
city_revenue.sort_values().plot(kind="barh")

plt.title("Revenue par ville")
plt.xlabel("Revenue")
plt.ylabel("Ville")

plt.tight_layout()
plt.savefig("visuals/revenue_by_city.png")

plt.show()

# =========================
# Graphique 2 : Profit par catégorie
# =========================

category_profit = df.groupby("category")["profit"].sum()

plt.figure(figsize=(8,5))
category_profit.sort_values().plot(kind="barh")

plt.title("Profit par catégorie")
plt.xlabel("Profit")

plt.tight_layout()
plt.savefig("visuals/profit_by_category.png")

plt.show()


# =========================
# Graphique 3 : Méthodes de paiement
# =========================

payment_counts = df["payment_method"].value_counts()

plt.figure(figsize=(6,6))
payment_counts.plot(kind="pie", autopct="%1.1f%%")

plt.title("Répartition des paiements")
plt.ylabel("")

plt.tight_layout()
plt.savefig("visuals/payment_methods.png")

plt.show()