# Wild Forest Fire System Prediction using Neural Networks <br>
Meteorological Data - Stational Model<br>
Axel Daniela Campero Vega <br>
Department of Computer Science <br>
Golisano College of Computing and Information Sciences <br>
Rochester Institute of Technology <br>
Rochester, NY 14623, USA - 2023 <br>
ac6887@g.rit.edu <br>

## Introduction
The development of artificial intelligence and Machine Learning has promoted the studies and data analysis to forecast the occurrence of forest fires. Machine learning algorithms are applied, modified or created to understand the complex interplay of multiple variables associated with wildfires [1]. The most used algorithms are neural networks, gradient boosting, k-nearest neighbors. However, no "best method" has been established for analyzing this problem. The works reviewed adopt specific development models, require high-capacity computing stations, use of specialized software, and extensive user coding experience. <br>

This part of the project uses meteorological data from NASA POWER - DATA ACCESS VIEWER in order to get historical data of temperature, atmospheric pressure and relative humidity to build a seasonal model of each one of these variables. The model will be achieved using Random Forest prediction, which is a tool from machine learning. This valuable information will later be taken into account in the prediction and early warning system to mitigate the effect of forest fires in Bolivia. <br>

## I. METEOROLOGICAL DATA ACQUISITION

The meteorological data of temperature, atmospheric pressure and relative humidity will be obtained from NASA POWER - DATA ACCESS VIEWER [2]. This NASA satellite platform https://power.larc.nasa.gov/data-access-viewer/, provides high-quality climate and solar energy data, useful for research. The output format can be cvs, NetCDF or others. Data is available from January 1981 to date and has all the locations searched. Annual data was downloaded to train the machine learning system and find the regression. It is possible to select a specific location on the map, time periods and the type of data to download. For the model, we download the temperature, atmospheric pressure and relative humidity data. <br>
SENAMHI [3] data will also be taken into account; The National Meteorology and Hydrology Service of Bolivia, which provides meteorological information at the national level and is used as a source of comparison and complementation of the data obtained from NASA (LARC Satellite). Historical records are available for years and the format is csv. Atmospheric pressure and relative humidity data will be taken. <br>

## II. ANALYSIS OF THE BEHAVIOR OF TEPERATURE, ATMOSPHERIC PRESSURE AND RELATIVE HUMIDITY
Temperature, Atmospheric pressure and relative humidity also have a great influence on the probability of generating a forest fire. These factors will be analyzed using the data described in section Data Acquisition, which includes a data set from 1982 to the current date. The analysis consists of performing a regression on the data using machine learning techniques that can better adapt to the behavior of this data. These regressions will serve to create an annual behavior model and make a prediction based on the day of the year for which the query is made. <br>

### A.	REGRESION
RANDOM FOREST REGRESSION
For this type of data, random forest was used, which is one of the machine learning and automatic learning strategies. Random forest algorithm is a supervised learning algorithm uses ensemble learning methods for regression [4]. It represents a set of hierarchical decision rules in tree form, where each node in the tree represents a specific decision or test, and each branch represents the result of that test. Decision trees are used for classification and regression problems. <br>
<p align="center">
  <img width="229" alt="image" src="https://github.com/AxelCamperoVega/Wild-Forest-Fire-System-Prediction-using-Random-Forest-for-Meteorological-Data---Seasonal-Model/assets/43591999/af9368b4-36dc-457e-a68b-1b154f348107">
  <br>Random Forest Regression
</p>
 

This technique includes:<br>
•	Nodes: A decision tree consists of three types of nodes; Root node (first decision); Internal nodes (tests or decisions); Leaf nodes (final decisions or classification labels)<br>
•	Branches: Each internal node has branches that extend to other nodes. Each branch is associated with a test or decision.<br>
•	Features: In each internal node, a test is performed on a specific feature. This test divides the data set into two or more subsets. <br>
When used to classify data, leaf nodes represent the class labels to which an example is assigned. In regression problems, leaf nodes represent numerical or continuous values. Decision trees are built using machine learning algorithms that seek to find the best features and optimal split points to minimize impurity (in the case of classification) or error (in the case of regression) in the leaf nodes. <br> 
One of the advantages of decision trees is their ease of interpretation since you can easily follow the decision path from the root to a leaf node to understand how decisions are made. One possible problem is over fitting. This occurs when the tree over fits the training data and does not generalize well to new data. <br>
To develop the model, the results of the regressions were compared using Linear Regression with polynomial of order 10, Random Forest and Neural Networks. Based on the results obtained, Random Forest was chosen, as it has the lowest RMSE and models the behavior of relative humidity and atmospheric pressure more adequately.

### B.	PROGRAM
The program starts by loading meteorological data for the location. The annual data is recovered with the detail of each day from the year 2017 to 2023, which is enough for training and test using Random Forest. Once the date for which you want to make the estimate has been entered, the program performs an internal conversion of the date to the day (numerical variable that for each year has 365 days), the program generates a data table where the real value is seen and the value estimated by the regression. The program also generates the model accuracy value and the scatterplot of the real data and the regression trend line. In addition, the program calculates the RMSE value. Once the calculation is finished, the program displays a menu and asks if we want to make a prediction for a specific day and as a result it shows us the table with the real value of the database for that day and the value of the prediction. The program repeats the same steps for each province (10 provinces or clusters were defined). <br>
This result generates a model of annual behavior for atmospheric pressure and temperature that will be part of the fire probability function along with the location factor and the seasonality factor.<br>

**Special Python libraries used:**
•	**PolynomialFeatures from sklearn.preprocessing:** It is a scikit-learn class used to generate polynomial features from a set of existing features. It is useful for creating polynomial regressions, which can model nonlinear relationships between variables. <br>
•	**LinearRegression from sklearn.linear_model:** It is a scikit-learn class that implements linear regression. It is used to model linear relationships between independent and dependent variables. This technique is appropriate when the relationship between the variables is linear. <br>
•	**sklearn.metrics r2_score:** It is a metric used to evaluate the quality of a regression model. It represents the proportion of the variance in the dependent variable that is predictable from the independent variables. An R^2 score close to 1 indicates a good model fit. <br>
•	**train_test_split from sklearn.model_selection:** It is a scikit-learn function used to split a data set into training and test sets. This is essential to evaluate model performance on unseen data and avoid overfitting. <br>
•	**RandomForestRegressor from sklearn.ensemble:** It is a scikit-learn class that implements regression using the Random Forests method. Random Forests are a set of decision trees that are combined to make more accurate and robust predictions compared to a single decision tree.<br>
•	**MLPRegressor from sklearn.neural_network:** It is a scikit-learn class that implements regression using artificial neural networks (ANN). Neural networks are machine learning models inspired by the human brain and are used to model complex, non-linear relationships between variables. <br>

### C.	OUTPUT
The program ask for the parameters. Example: Consulting for the date May 5, 2021 will generate the following:
 <br>

**Input the Year** (2018-2022):2021  <br>
1- January, 2- February, 3- March, 4- April, 5- May, 6- June  <br>
7- July, 8- August, 9- September, 10- October,11- November,12- December <br>
**Please, enter the number of the month:** 5 <br>
**Input a day of the month:** 5 <br>
Output:  <br>
**The correspondent day from 2018-2022 is:  1221.0 <br>
The Relative Humidity is: 25.34859999999997 <br>
Accuracy:  96.59924463098486 % <br>
Temperature (Farenheith): 91.75399999999979 <br>
Accuracy:  97.73992366997707 % <br>
Atmospheric Pressure: 98.94729999999969 <br>
Accuracy:  96.860277806636 % <br>
End of the Program** <br>

And generates the following table, which is exported to excel:  <br>
**DAY  HUMR      TEMP   PRES_ATM** <br>
**1    27.090467  88.190500  98.352400** <br>
**2    27.102233  87.603267  98.363700** <br>
**3    26.892833  88.006633  98.430500** <br>
**4    26.256833  89.092000  98.444600** <br>
**5    25.934800  91.352767  98.433300** <br>
..     ...        ...        ...        ... <br>
**361    25.838367  89.099867  98.594833** <br>
**362    26.379467  89.032833  98.606300** <br>
**363    25.576867  90.706133  98.612800** <br>
**364    25.117767  94.431833  98.650000** <br>
**365    25.078567  92.785800  98.650000** <br>

**[365 rows x 4 columns]** <br>
And generates the following plots:  <br>
<p align="center">
  <img width="336" alt="image" src="https://github.com/AxelCamperoVega/Wild-Forest-Fire-System-Prediction-using-Random-Forest-for-Meteorological-Data---Seasonal-Model/assets/43591999/65fa656f-8f37-47aa-a59d-26b72376f56f">
  <br> Random Forest Prediction Vs. Real data for five years (2018 – 2023)
</p>
 

Real data is shown in blue and prediction in red. The figures show the seasonal behavior of these variables. Therefore, it is possible to get a model for one year. <br>
The program also show the model predicted for each variable in the period of one year: <br>

**Atmospheric Pressure**
•	Bolivia is a geographically diverse country and atmospheric pressure can vary greatly [2]. Atmospheric pressure is important because it defines the amount of available oxygen that will act as an “oxidant” in a forest fire. The greater the amount of oxygen, the greater the probability of a fire breaking out. This is the reason why it is considered a factor of great influence in the prediction model <br>
•	Atmospheric pressure is inversely proportional to the height above sea level and in Bolivia, geographical regions can vary between 300m to 4,000m above sea level. Therefore, this parameter is very important in the probability function of a fire event. Due to the great geographical diversity of Bolivia, these values can vary significantly. Because the prediction model is disaggregated by zone (clusters), data from the 10 defined zones have been collected. The figure shows the evolution of annual atmospheric pressure as an example for the province “Ixiamas”. The records are from 2022. Similar data is available for the 10 clusters. <br>
<p align="center">
  <img width="371" alt="image" src="https://github.com/AxelCamperoVega/Wild-Forest-Fire-System-Prediction-using-Random-Forest-for-Meteorological-Data---Seasonal-Model/assets/43591999/8f715329-474f-47ef-ae7b-dc675eabbafa">
  <br>Atmospheric Pressure behavior prediction for Ixiamas (year 2022)
</p>

 

•	The data used to describe this behavior is stored in the system database for further processing or data mining. On the other hand, in the development of the model, these data will be used to develop a regression function that describes its behavior as a function of time (annual) and will be incorporated into the model. <br>

#### Relative Humidity
•	As in the previous case, a great variation in this factor is observed depending on the area or cluster. Relative humidity is important because forest fires are more likely to occur when relative humidity is low, that is, when the air is dry. This parameter is variable and has a seasonal behavior. Figure shows its average annual behavior for the cluster Ixiamas, which is one of the ten clusters.  <br>
<p align="center">
  <img width="370" alt="image" src="https://github.com/AxelCamperoVega/Wild-Forest-Fire-System-Prediction-using-Random-Forest-for-Meteorological-Data---Seasonal-Model/assets/43591999/c2f786c4-fdd7-424c-8960-919a596ad28a">
  <br>Relative Humidity annual behavior for Ixiamas – Bolivia (2022)
</p>


•	These data will be used to incorporate them into the model, performing a regression to describe their annual temporal behavior and will also be saved for future consultations in the project database.
Temperature. <br>
•	As in the previous case, a great variation in this factor is observed depending on the area or cluster. Temperature is important because forest fires are more likely to occur when temperature is high. This parameter is variable and has a seasonal behavior. Figure shows its average annual behavior for the cluster Ixiamas, which is one of the ten clusters. <br>
<p align="center">
  <img width="349" alt="image" src="https://github.com/AxelCamperoVega/Wild-Forest-Fire-System-Prediction-using-Random-Forest-for-Meteorological-Data---Seasonal-Model/assets/43591999/83a68769-c036-4938-8e8d-78daaf1d651d">
<br>  Temperature annual behavior for Ixiamas – Bolivia (2022)
</p>

•	The data used to describe this behavior is stored in the system database for further processing or data mining. On the other hand, in the development of the model, these data will be used to develop a regression function that describes its behavior as a function of time (annual) and will be incorporated into the model. <br>

**References**  <br>
<sup><sub>[1] Predicting Forest Fires in Madagascar. Jessica Edwards, Manana Hakobyan, Alexander Lin and Christopher Golden. School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA
https://projects.iq.harvard.edu/files/cs288/files/madagascar_fires.pdf </sub></sup><br>

<sup><sub>[2] https://power.larc.nasa.gov/data-access-viewer/ <br>

<sup><sub>[3] https://senamhi.gob.bo/index.php/inicio <br>

<sup><sub>[4] Weather prediction Using Random Forest Method Aravind M1 ,Thilak S2 ,Vigneshwaran B3 ,Dr.J.B.Jona4 
</sub></sup>
