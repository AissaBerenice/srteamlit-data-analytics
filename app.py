import streamlit as st
import pandas as pd

st.title("Esto es un titulo")
st.header("Esto es un header")
st.markdown("*Markdown Italiks*")

df = pd.read_csv("train.csv")
st.dataframe(df) 

clase1 = df[(df["Pclass"] == 1)]
clase2 = df[(df["Pclass"] == 2)]
clase3 = df[(df["Pclass"] == 3)]

st.title("Representacion Grafica de Clases ")

categories = ['Primera Clase', 'Segunda Clase', 'Tercera Clase']
values = [len(clase1), len(clase2), len(clase3)]

plt.pie(values, labels=categories, autopct='%1.1f%%', startangle= 90)
plt.axis('equal') 
plt.title('Pie Chart Example')
plt.show()
