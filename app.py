import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("Prédiction du Revenue E-commerce")

df = pd.read_csv("data/clean_dataset.csv")

X = df[["quantity", "unit_price", "age", "cost", "order_month"]]
y = df["revenue"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

st.subheader("Entrez les informations de la commande")

quantity = st.number_input("Quantité", min_value=1, max_value=100, value=3)
unit_price = st.number_input("Prix unitaire", min_value=0.0, value=120.0)
age = st.number_input("Âge du client", min_value=1, max_value=100, value=35)
cost = st.number_input("Coût", min_value=0.0, value=80.0)
order_month = st.number_input("Mois de commande", min_value=1, max_value=12, value=6)

if st.button("Prédire le revenue"):
    example = pd.DataFrame({
        "quantity": [quantity],
        "unit_price": [unit_price],
        "age": [age],
        "cost": [cost],
        "order_month": [order_month]
    })

    prediction = model.predict(example)

    st.success(f"Revenue prédit : {prediction[0]:.2f} €")