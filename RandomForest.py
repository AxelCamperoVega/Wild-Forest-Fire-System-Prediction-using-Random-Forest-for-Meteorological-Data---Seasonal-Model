# Fire Forest Prediction for Bolivia
# Axel Daniela Campero Vega
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
print ("")

# date arrangements
print("{:^60}".format("Input the date"))
menus= int(input("Input the Year (2018-2022):"))
while menus != 0:            # menu for the year
    if menus == 2018:
        w = 0
        break
    elif menus == 2019: # we add the days according the date selected
        w = 365
        break
    elif menus == 2020:
        w = 730
        break
    elif menus == 2021:
        w = 1096
        break
    elif menus == 2022:
        w = 1461
        break
    else:
        print("Please enter other date")
menu = print('')
# Select the month
menu= int(input("1- January, 2- February, 3- March, 4- April, 5- May, 6- June \n7- July, 8- August, 9- September, 10- October,11- November,12- December\n"
                "Please, enter the number of the month: "))
while menu != 0:
    if menu == 1:               # For each value of the menue
        q1 = float(input('Input the day: '))
        break
    elif menu == 2:
        q = float(input('Input the day: '))
        q1 = 31 + q            # Adding the days
        break
    elif menu == 3:             # Reapeating for all clusters
        q = float(input('ingrese el dia correspondiente: '))
        q1 = 59 + q
        break
    elif menu == 4:
        q = float(input('Input the day: '))
        q1 = 90 + q
        break
    elif menu == 5:
        q = float(input('Input the day: '))
        q1 = 120 + q
        break
    elif menu == 6:
        q = float(input('Input the day: '))
        q1 = 151 + q
        break
    elif menu == 7:
        q = float(input('Input the day: '))
        q1 = 181 + q
        break
    elif menu == 8:
        q = float(input('Input the day: '))
        q1 = 212 + q
        break
    elif menu == 9:
        q = float(input('Input the day: '))
        q1 = 243 + q
        break
    elif menu == 10:
        q = float(input('Input the day: '))
        q1 = 273 + q
        break
    elif menu == 11:
        q = float(input('Input the day: '))
        q1 = 304 + q
        break
    elif menu == 12:
        q = float(input('Input the day: '))
        q1 = 334 + q
        break
    else:
        print("Input anothe number")
menu = print('')
DIA = w + q1

# al final sumamos los dias del año escogido con el mes y dia
print('The correspondent day from 2018-2022 is: ',DIA )
print('')

# Leer datos desde un archivo CSV

#datos = pd.read_csv('D:\RIT Dic2022/Proyecto de grado/7 Presiony Temperatura/Regresion Presion y Humedad/EXCEL/Pailon.csv',sep=';')

datos = pd.read_csv('D:/Axel 2024/RIT Dic2022/Proyecto de grado/7 Presiony Temperatura/Regresion Presion y Humedad/RandomForest/EXCEL/Pailon.csv',sep=';')

# Obtener la variable independiente (X) y la variable dependiente (y)
x = datos.iloc[:,0:1].values
y = datos.iloc[:,1].values

# Dividir los datos en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2)

# Crear el modelo de regresión con Bosques Aleatorios
modelo = RandomForestRegressor(n_estimators=300, random_state=42)
# Entrenar el modelo con los datos de entrenamiento
modelo.fit(x_train, y_train)
# Realizar predicciones en el conjunto de prueba
predicciones = modelo.predict(x_test)

#realizamos el mismo codigo para la temperatura
x1 = datos.iloc[:,0:1].values
y1 = datos.iloc[:,2].values
x_train1, x_test1, y_train1, y_test1 = train_test_split(x1, y1, test_size= 0.2)
modelo1 = RandomForestRegressor(n_estimators=300, random_state=42)
modelo1.fit(x_train1, y_train1)
predicciones1 = modelo1.predict(x_test1)

x2 = datos.iloc[:,0:1].values
y2 = datos.iloc[:,3].values
x_train2, x_test2, y_train2, y_test2 = train_test_split(x2, y2, test_size= 0.2)
modelo2 = RandomForestRegressor(n_estimators=300, random_state=42)
modelo2.fit(x_train2, y_train2)
predicciones2 = modelo2.predict(x_test2)

# Realizar la predicción para el valor ingresado por el usuario
variabled = modelo.predict([[DIA]])
# Mostrar el resultado de la variable dependiente
print("The Relative Humidity is:", variabled[0])
print('Accuracy: ',modelo.score(x_train, y_train)*100,'%')

variabled1 = modelo1.predict([[DIA]])
print("Temperature (Farenheith):", variabled1[0])
print('Accuracy: ',modelo1.score(x_train1, y_train1)*100,'%')

variabled2 = modelo2.predict([[DIA]])
print("Atmospheric Pressure:", variabled2[0])
print('Accuracy: ',modelo2.score(x_train2, y_train2)*100,'%')
print("")
print("")
print("")
print("")
print("")
print("")
# Plotting the Relative Humidity
plt.subplot(3,1,1)
x_grid = np.arange(min(x_test),max(x_test),0.1)
x_grid = x_grid.reshape(len(x_grid),1)
plt.scatter(x_test,y_test)
plt.plot(x_grid, modelo.predict(x_grid), color='red', label = 'HUMEDAD RELATIVA',linewidth =2)
plt.title('Plotting the three variables')
plt.ylabel('Relative Humidity')
plt.tick_params(labelsize=7)

# Plotting Temp
plt.subplot(3,1,2)
x_grid1 = np.arange(min(x_test1),max(x_test1),0.1)
x_grid1 = x_grid1.reshape(len(x_grid1),1)
plt.scatter(x_test1,y_test1)
plt.plot(x_grid1, modelo1.predict(x_grid1), color='orange', label = 'TEMPERATURA',linewidth =2)
plt.ylabel('Temperature')
plt.tick_params(labelsize=7)

# Plotting Atmospheric Pressure
plt.subplot(3,1,3)
x_grid2 = np.arange(min(x_test2),max(x_test2),0.1)
x_grid2 = x_grid2.reshape(len(x_grid2),1)
plt.scatter(x_test2,y_test2)
plt.plot(x_grid2, modelo2.predict(x_grid2), color='green', label = 'Atmospheric Pressure',linewidth =2)
plt.xlabel('Days')
plt.ylabel('Atmospheric Pressure')
plt.tick_params(labelsize=7)

plt.show()

# Relative Humidity
pruebas = x[-365:]
pred2022 = modelo.predict(pruebas.reshape(-1,1))
datos1 = pd.read_csv('D:/Axel 2024/RIT Dic2022/Proyecto de grado/7 Presiony Temperatura/Regresion Presion y Humedad/RandomForest/EXCEL/Pailon.csv',sep=';')
l = datos1.iloc[:,0].values
m = datos1.iloc[:,1].values
# Graficar las funciones
plt.figure(figsize=(10, 5))
plt.plot(l, m, color= 'red' ,label='Real data')  # Graficar la primera función
plt.plot(l, pred2022, color = 'yellow', label='Predicted')  # Graficar la segunda función
plt.xlabel('Days')
plt.ylabel('Relative Humidity')
plt.title('Real Vs. Predicted Copmparison')
plt.legend()  
plt.grid(True)  # Grid
plt.show()

# Temperature
pruebas1 = x1[-365:]
pred1_2022 = modelo1.predict(pruebas1.reshape(-1,1))
mm = datos1.iloc[:,2].values
# Graficar las funciones
plt.figure(figsize=(10, 5))
plt.plot(l, mm, color= 'brown' ,label='Real data')  # Graficar la primera función
plt.plot(l, pred1_2022, color = 'orange', label='Predicted')  # Graficar la segunda función
plt.xlabel('Days')
plt.ylabel('Temperature - Farenheith')
plt.title('Real data Vs. Prediction comparison')
plt.legend()  # Mostrar leyenda con etiquetas
plt.grid(True)  # Mostrar cuadrícula en el gráfico
plt.show()

# Atmospheric Pressure
pruebas2 = x2[-365:]
pred2_2022 = modelo2.predict(pruebas2.reshape(-1,1))
mmm = datos1.iloc[:,3].values
# Graficar las funciones
plt.figure(figsize=(10, 5))
plt.plot(l, mmm, color= 'blue' ,label='Real Data')  # Graficar la primera función
plt.plot(l, pred2_2022, color = 'green', label='Predicted')  # Graficar la segunda función
plt.xlabel('Days')
plt.ylabel('Atmospheric Pressure')
plt.title('Real Data Vs. Prediction Comparison')
plt.legend()  # Mostrar leyenda con etiquetas
plt.grid(True)  # Mostrar cuadrícula en el gráfico
plt.show()

data1 = {'DIA': l, 'HUMR': pred2022, 'TEMP': pred1_2022, 'PRES_ATM': pred2_2022}
df1 = pd.DataFrame(data1)
print(df1)
df1.to_excel('PAILON DATOS OBTENIDOS2022.xlsx', index = False)
