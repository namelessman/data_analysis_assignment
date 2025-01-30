
################ Data cleaning the House dataset #################
import pandas as pd
import os

# load ./House_Data.csv
house_data = pd.read_csv(os.path.abspath('') + '/week8/House_Data.csv')
# Since this is a bunch, create a dataframe
house_data_df=pd.DataFrame(house_data)

house_data_df.columns=['area_type','availability','size','society','total_sqft','bath','balcony','price','site_location']

print("Number of missing data in the dataset:")
print(house_data_df.isnull().sum()) # count the number of missing data
house_data_df.drop_duplicates(inplace=True)
house_data_df.dropna(inplace=True) # remove any empty lines

# check price outliers using IQR
print("Check outliers:")
Q1 = house_data_df['price'].quantile(0.25)
Q3 = house_data_df['price'].quantile(0.75)
IQR = Q3 - Q1
print("Q1: ", Q1)
print("Q3: ", Q3)
print("IQR: ", IQR)
print("Outliers: ", house_data_df[(house_data_df['price'] < (Q1 - 1.5 * IQR)) | (house_data_df['price'] > (Q3 + 1.5 * IQR))])

# remove outliers
print("Remove outliers:")
house_data_df = house_data_df[(house_data_df['price'] > (Q1 - 1.5 * IQR)) & (house_data_df['price'] < (Q3 + 1.5 * IQR))]
print(house_data_df)

# # check bath outliers using IQR
# print("Check outliers:")
# Q1 = house_data_df['bath'].quantile(0.25)
# Q3 = house_data_df['bath'].quantile(0.75)
# IQR = Q3 - Q1
# print("Q1: ", Q1)
# print("Q3: ", Q3)
# print("IQR: ", IQR)
# print("Outliers: ", house_data_df[(house_data_df['bath'] < (Q1 - 1.5 * IQR)) | house_data_df['bath'] > (Q3 + 1.5 * IQR)])

# # check bath balcony using IQR
# print("Check outliers:")
# Q1 = house_data_df['balcony'].quantile(0.25)
# Q3 = house_data_df['balcony'].quantile(0.75)
# IQR = Q3 - Q1
# print("Q1: ", Q1)
# print("Q3: ", Q3)
# print("IQR: ", IQR)
# print("Outliers: ", house_data_df[(house_data_df['balcony'] < (Q1 - 1.5 * IQR)) | house_data_df['balcony'] > (Q3 + 1.5 * IQR)])