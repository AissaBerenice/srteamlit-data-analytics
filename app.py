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

#Histograma de la clase de los pasajerons

columna = 'Pclass'

plt.figure(figsize=(8, 6))
df[columna].hist(bins=3, color='lightsteelblue', edgecolor='black')
plt.title(f'Histograma de {columna}')
plt.xlabel(columna)
plt.ylabel('Cantidad')
plt.xticks([1, 2, 3], ['Primera', 'Segunda', 'Tercera'])
plt.grid(True)
plt.show()

#Histograma de pasajeros que sobrevivieron

columna = 'Survived'

plt.figure(figsize=(8, 6))
df[columna].hist(bins=[-0.5, 0.5, 1.5], color='steelblue', edgecolor='black', align='mid')
plt.title(f'Histograma de {columna}')
plt.xlabel(columna)
plt.ylabel('Cantidad')
plt.xticks([0, 1], ['No', 'Sí'])
plt.grid(True)
plt.show()

#Histograma del sexo de los pasajeros

columna = 'Sex'

plt.figure(figsize=(8, 6))
df[columna].hist(bins=[-0.5, 0.5, 1.5], color='royalblue', edgecolor='black', align='mid')
plt.title(f'Histograma de {columna}')
plt.xlabel(columna)
plt.ylabel('Cantidad')
plt.xticks(['male', 'female'])
plt.grid(True)
plt.show()

#Histograma de la edad de los pasajerons

columna = 'Age'

plt.figure(figsize=(8, 6))
df[columna].hist(bins=20, color='cornflowerblue', edgecolor='black')
plt.title(f'Histograma de {columna}')
plt.xlabel(columna)
plt.ylabel('Cantidad')
plt.grid(True)
plt.show()

#Histograma de pasajeros con hermanos abordo

columna = 'SibSp'

plt.figure(figsize=(8, 6))
df[columna].hist(bins=[-0.5, 0.5, 1.5], color='cadetblue', edgecolor='black', align='mid')
plt.title(f'Histograma de {columna}')
plt.xlabel(columna)
plt.ylabel('Candidad')
plt.xticks([0, 1], ['No', 'Sí'])
plt.grid(True)
plt.show()

#Histograma de pasajeros con padres abordo

columna = 'Parch'

plt.figure(figsize=(8, 6))
df[columna].hist(bins=[-0.5, 0.5, 1.5], color='lightblue', edgecolor='black', align='mid')
plt.title(f'Histograma de {columna}')
plt.xlabel(columna)
plt.ylabel('Candidad')
plt.xticks([0, 1], ['No', 'Sí'])
plt.grid(True)
plt.show()

#Histograma del costo de su boleto

columna = 'Fare'

plt.figure(figsize=(8, 6))
df[columna].hist(bins=20, color='cornflowerblue', edgecolor='black')
plt.title(f'Histograma de {columna}')
plt.xlabel(columna)
plt.ylabel('Costo')
plt.grid(True)
plt.show()

#Puerto en que embarcaron los pasajeros (C = Cherbourg; Q = Queenstown; S = Southampton)

columna = 'Embarked'

plt.figure(figsize=(8, 6))
df[columna].hist(bins=3, color='lightskyblue', edgecolor='black')
plt.title(f'Histograma de {columna}')
plt.xlabel(columna)
plt.ylabel('Cantidad')
plt.xticks(['C', 'Q', 'S'], ['Cherbourg', 'Queenstown', 'Southampton'])
plt.grid(True)
plt.show()
