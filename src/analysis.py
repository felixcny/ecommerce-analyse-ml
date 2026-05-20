import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

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

print("\nProduit le plus vendu :")
print(df.groupby("product_id")["quantity"].sum().sort_values(ascending=False).head())

print("\nPanier moyen :")
print(df["revenue"].mean())

print("\nRevenue par jour de la semaine :")
print(df.groupby("order_day_of_week")["revenue"].sum().sort_values(ascending=False))

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

# =========================
# Revenue par catégorie
# =========================

category_revenue = df.groupby("category")["revenue"].sum()

plt.figure(figsize=(8,5))
category_revenue.plot(kind="bar")

plt.title("Revenue par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("Revenue")

plt.tight_layout()
plt.savefig("visuals/revenue_by_category.png")

plt.show()

# =========================
# Revenue au fil du temps
# =========================

df["order_date"] = pd.to_datetime(df["order_date"])

revenue_time = df.groupby("order_date")["revenue"].sum()

plt.figure(figsize=(10,5))
revenue_time.plot()

plt.title("Revenue au fil du temps")
plt.xlabel("Date")
plt.ylabel("Revenue")

plt.tight_layout()
plt.savefig("visuals/revenue_over_time.png")

plt.show()

# =========================
# Machine Learning : prédire le revenue
# =========================

ml_df = df[["quantity", "city", "category", "age", "revenue"]]

ml_df = pd.get_dummies(ml_df, columns=["city", "category"])

X = ml_df.drop("revenue", axis=1)
y = ml_df["revenue"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n=== Résultats Machine Learning ===")
print("MAE :", mean_absolute_error(y_test, y_pred))
print("R² :", r2_score(y_test, y_pred))