from pyspark.sql.functions import col

df1 = df.filter(col("amount") > 500)
df1.show()
df = spark.read.csv("data.csv", header=True, inferSchema=True)

df.show(10)
from pyspark.sql.functions import col

df1 = df.filter(col("amount") > 500)
df1.show()
df2 = df1.filter(col("location")=="Hyderabad")
df2.show()
df3 = df2.dropna()
df3.show()
df3 = df2.dropna()
df3.show()
df.groupBy("customer_id").sum("amount").show()
from google.colab import files
files.download("filtered_data.csv")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df["transaction_type"].value_counts().plot(kind="bar", color=["blue","orange"])
plt.title("Deposit vs Withdrawal Count")
plt.show()
df["location"].value_counts().plot(kind="bar", color="green")
plt.title("Transactions by Location")
plt.show()
plt.hist(df["amount"], bins=20, color="purple")
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()
top = df.groupby("customer_id")["amount"].sum().sort_values(ascending=False).head(10)

top.plot(kind="bar", color="red")
plt.title("Top 10 Customers by Spending")
plt.show()