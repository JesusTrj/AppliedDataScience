# Work Methodology
First Machine Learning problem, related to multivariable time series forecasting. Will be using a dataset found in [Kaggle](https://www.kaggle.com/datasets/szrlee/stock-time-series-20050101-to-20171231?resource=download), where stocks prices are located between 2006 and 2018, will be trying to forecast the value of the stock in the future. In the future, it may be interesting to use some API to use real time series data.

The solution will consist of eight main activities, with several task within each one. The following will represent the Minimum Valuable Product (MVP).

1. Data Cleaning & Formatting 
* After analysing the csv files provided, for the EDA will be using the [compiled stocks file](https://github.com/JesusTrj/AppliedDataScience/tree/main/stock_forecasting/stock_data/Compiled), then for the ML model training will be using the individual stock files in the following [link](https://github.com/JesusTrj/AppliedDataScience/tree/main/stock_forecasting/stock_data/Individual).
2. Exploratory Data Analysis  
Aggregation window features wont be needed in this solution, since the architecture doesnt involve DB or Real Time services. For this solution, data will be stored and worked with locally.
* [Aggregation Window. Part 1](https://towardsdatascience.com/real-time-aggregation-features-for-machine-learning-part-1-ec7337c0a504)
* [Aggregation Window. Part 2](https://towardsdatascience.com/real-time-aggregation-features-for-machine-learning-part-2-fe9fd42522c0)
3. Feature Engineering and selection  
After analyzing the features available in the Dataset, in conclusion, PCA wont be performed, since the information available is pretty limited. PCA inst necesary for this solution, nevertheless, below there will be some documentation for following projects.
* [Intro to Feature Engineering for Time Series forecasting](https://medium.com/data-science-at-microsoft/introduction-to-feature-engineering-for-time-series-forecasting-620aa55fcab0#:~:text=Feature%20engineering%20efforts%20mainly%20have,as%20a%20supervised%20learning%20problem.)
* [PCA](https://towardsdatascience.com/using-principal-component-analysis-pca-for-machine-learning-b6e803f5bf1e)
4. Compare several machine learning models on a performance metric
* [AutoTS ©Google](https://github.com/AutoViML/Auto_TS)
5. Perform hyperparameter tuning on the best model
* [Hyperparameter Grid Search](https://joaquinamatrodrigo.github.io/skforecast/0.4.3/quick-start/introduction-forecasting.html)
6. Evaluate the best model on the testing set
7. Interpretation
8. Conclutions

For further information visit: [Towards Data Science - A complete machine learning walk through in Python](https://towardsdatascience.com/a-complete-machine-learning-walk-through-in-python-part-one-c62152f39420)

**This scope and project approach can be modified, adding or substracting tasks as needed.**
