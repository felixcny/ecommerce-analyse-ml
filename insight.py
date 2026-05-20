import pandas as pd
import duckdb

df = pd.read_csv('data/clean_dataset.csv')

print("-"*50)
print(" REPONSES QUESTION BUSINESS")
print("-"*50)

# categorie avec le plus de revenue
q1 = duckdb.query("""
    SELECT category, SUM(revenue) AS revenue_total 
    FROM df 
    GROUP BY category 
    ORDER BY revenue_total DESC 
    LIMIT 1
""").df()
print(f"\n1. TOP CATÉGORIE : '{q1['category'][0].title()}' avec {q1['revenue_total'][0]:,.2f} $")


# ville avec plus de ventes
q2 = duckdb.query("""
    SELECT city, SUM(revenue) AS total_revenu 
    FROM df 
    GROUP BY city 
    ORDER BY total_revenu DESC 
    LIMIT 1
""").df()
print(f"\n2. TOP VILLE : '{q2['city'][0]}' avec {q2['total_revenu'][0]:,.2f} $")


# produit le plus vendu
q3 = duckdb.query("""
    SELECT product_id, brand, SUM(quantity) AS qte 
    FROM df 
    GROUP BY product_id, brand 
    ORDER BY qte DESC 
    LIMIT 3
""").df()
print("\n3. PRODUITS LES PLUS VENDUS (Top 3) :")
for index, row in q3.iterrows():
    print(f" Produit {row['product_id']} de {row['brand']} : {row['qte']} unités")


# panier moyen
q4 = duckdb.query("""
    SELECT SUM(revenue) / COUNT(DISTINCT order_id) as pm
    FROM df
""").df()
print(f"\n4. PANIER MOYEN : {q4['pm'][0]:,.2f} $ par commande")


# jour de la semaine avc le plus de vente
q5 = duckdb.query("""
    SELECT order_day_of_week, SUM(revenue) AS total_revenue 
    FROM df 
    GROUP BY order_day_of_week 
    ORDER BY total_revenue DESC 
    LIMIT 1
""").df()
print(f"\n5. TOP JOUR DE LA SEMAINE : '{q5['order_day_of_week'][0]}' avec {q5['total_revenue'][0]:,.2f} $")

print("-"*50)