
################ Data cleaning the Iris dataset #################
# from sklearn import datasets
import sklearn
import pandas as pd

# load iris dataset
iris = sklearn.datasets.load_iris()
# Since this is a bunch, create a dataframe
iris_df=pd.DataFrame(iris.data)
iris_df['class']=iris.target

iris_df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
#### ===> TASK 1: here - add two more lines of the code to find the number and mean of missing data
cleaned_data = iris_df.dropna(how="all", inplace=True) # remove any empty lines
print("Number of missing data in the dataset:")
print(iris_df.isnull().sum()) # count the number of missing data
print("Mean of the dataset:")
print(iris_df.mean()) # calculate the mean of the data



iris_X=iris_df.iloc[:5,[0,1,2,3]]
print(iris_X)

### TASK2: Here - Write a short readme to explain above code and how we can calculate the corrolation amoung featuers with description
# The code above is used to clean the iris dataset. 
# The code first loads the iris dataset and then creates a dataframe from it. 
# The code then drops any empty lines in the dataset and calculates the number of missing data in the dataset. 
# The code then calculates the mean of the dataset. 
# The code then selects the first five rows and the first four columns of the dataset and prints it. 
# The code can be used to calculate the correlation among features by using the corr() function. 
# The corr() function calculates the correlation between each pair of features in the dataset. 
# The correlation values range from -1 to 1. A value of 1 indicates a perfect positive correlation, a value of -1 indicates a perfect negative correlation, and a value of 0 indicates no correlation between the features. 
# The correlation values can be used to identify relationships between the features in the dataset. 
# For example, if two features have a high positive correlation, it means that they tend to increase or decrease together. 
# If two features have a high negative correlation, it means that they tend to move in opposite directions. 
# The correlation values can be used to identify patterns in the data and to make predictions about future data points.

print("Correlation among features:")
print(iris_df.corr()) # calculate the correlation among features