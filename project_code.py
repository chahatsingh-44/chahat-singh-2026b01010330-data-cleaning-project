import numpy as np
import pandas as pd

df = pd.read_csv("india_bike_sales_unclean_10k.csv")

df.info()
# 1. remove duplicates
df = df.drop_duplicates()

# 2. clean extra spaces in text columns
text_cols = [
    "State","District","Company","Bike_Model",'Segment',"Color", "Payment_Mode",
]
for col in text_cols:
  df[col] = df[col].astype(str).str.strip().replace("nan", np.nan)

# 3. convert numeric columns 
num_cols = [
    "Engine_CC","Units_Sold","Ex_Showroom_Price_INR","Discount_INR","Total_On_Road_Amount_INR","Customer_Age",
]
for col in num_cols:
  df[col] = (
      df[col]
      .astype(str)
      .str.replace(r"[^\d.]", "", regex=True)
      .replace("", np.nan)
  )
  df[col] = pd.to_numeric(df[col], errors="coerce")

# 4. convert date column
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"], errors="coerce")

# 5. handle missing values simply
df["Discount_INR"] = df["Discount_INR"].fillna(0) # Assume 0 if missing
df = df.dropna(subset=["Sale_ID", "Units_Sold", "Total_On_Road_Amount_INR"])

# 6. save cleaned file and check result
df.to_csv("india_bike_sales_cleaned.csv", index=False)
print("Final shape:", df.shape)
print(df.info())