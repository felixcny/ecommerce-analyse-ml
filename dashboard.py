import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="E-Commerce Analytics", layout="wide")
st.title(" Dashboard : Ecommerce Analysis")
st.markdown("---")

@st.cache_data
def load_data():
    data = pd.read_csv('data/clean_dataset.csv')
    data['order_date'] = pd.to_datetime(data['order_date'])
    return data

df = load_data()

# KPI principaux
total_revenue = df['revenue'].sum()
total_orders = df['order_id'].nunique()
pm = total_revenue / total_orders
total_customers = df['customer_id'].nunique()

# affiche KPI
col1, col2, col3, col4 = st.columns(4)
col1.metric("Chiffre d'Affaires Total", f"{total_revenue:,.0f} $")
col2.metric("Nombre de Commandes", f"{total_orders}")
col3.metric("Panier Moyen (AOV)", f"{pm:,.2f} $")
col4.metric("Clients Uniques", f"{total_customers}")

st.markdown("---")

# nos graphiques
chart_col1, chart_col2 = st.columns(2)

# barc chart rvenue par cate
with chart_col1:
    st.subheader("Revenu par Catégorie")
    rev_cat = df.groupby('category')['revenue'].sum().sort_values(ascending=True)
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    rev_cat.plot(kind='barh', color='skyblue', ax=ax1, edgecolor='black')
    ax1.set_xlabel("Revenu ($)")
    ax1.set_ylabel("")
    st.pyplot(fig1)

# pie chart methode paimeent
with chart_col2:
    st.subheader("Méthodes de Paiement")
    pm_counts = df['payment_method'].value_counts()
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    pm_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'orange', 'lightcoral'], startangle=140, ax=ax2)
    ax2.set_ylabel("")
    st.pyplot(fig2)

# line chart revenue dans le temps
st.subheader("Évolution Mensuelle des Revenus")
# Création d'une colonne formatée pour n'afficher que l'année et le mois
df['month_year'] = df['order_date'].dt.to_period('M').astype(str)
rev_time = df.groupby('month_year')['revenue'].sum()

fig3, ax3 = plt.subplots(figsize=(12, 4))
rev_time.plot(kind='line', marker='o', color='purple', linewidth=2, ax=ax3)
ax3.set_xlabel("Mois")
ax3.set_ylabel("Revenu ($)")
ax3.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig3)