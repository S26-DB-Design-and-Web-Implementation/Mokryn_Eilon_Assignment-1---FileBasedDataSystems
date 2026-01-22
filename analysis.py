import pandas as pd
filepath = "Air_Quality.csv"
df = pd.read_csv(filepath)

print(df.head(2)) #printing first two rows

print(df.iloc[0])#printing first row

print(df.iloc[10:20])#printing rows 10 - 19

print(df.columns)#printing column names

print(df["Measure"].head(10))#printing first 10 values of of column "Measure"

print(df[["Name", "Measure", "Geo Place Name"]].head(10))#printing first 10 rows of the three columns chosen

#How many location types are boroughs?
borough_count = (df["Geo Type Name"] == "Borough").sum()
print(borough_count)

#How many tests were done in 2005?
tests_2005 = (df["Time Period"] == "2005").sum()
print(tests_2005)

#were more tests done in 2005 or other time periods combined?

tests_not_2005 = (df["Time Period"] != "2005").sum()

if tests_2005 > tests_not_2005:
    print("More tests were done in 2005: ", tests_2005)
else:
    if tests_2005 < tests_not_2005:
        print("More tests were done in other time periods combined: ", tests_not_2005)
    else:
        print("Same amount of tests were done in 2005 and other time periods combined: ", tests_2005)

print(df["Geo Type Name"])


