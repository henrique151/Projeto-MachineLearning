import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")
df.plot(kind="scatter", x="diametro", y="preco")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza")
st.divider()

diamentro = st.number_input("Digite o tamanho do diâmetro da pizza: ")

if diamentro:
    preco_previsto = modelo.predict([[diamentro]])[0][0]
    st.write(
        f"o valor da pizza com diâmetro de {diamentro:.2f} cm é de R${preco_previsto:.2f}.")


