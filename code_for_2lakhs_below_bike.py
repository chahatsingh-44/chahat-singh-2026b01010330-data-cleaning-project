import numpy as np
import pandas as pd

df = pd.read_csv("india_bike_sales_cleaned.csv")

# 1. clean and convert price column to numeric (handles commas/text safely)
price_clean = (
    df["Total_On_Road_Amount_INR"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("₹", "", regex=False)
    .str.strip()
)
df["Total_On_Road_Amount_INR"] = pd.to_numeric(price_clean, errors="coerce")

# 2. filter for bikes strictly below 2 lakhs (200,000 INR) using NumPy/pandas
bikes_below_2lakh = df[
    np.isfinite(df["Total_On_Road_Amount_INR"])
    & (df["Total_On_Road_Amount_INR"] < 200000)
].copy()

# 3. save the filtered data to a new CSV file
bikes_below_2lakh.to_csv("bikes_below_2_lakhs.csv", index=False)

print("Filtered shape:", bikes_below_2lakh.shape)
print(bikes_below_2lakh[["Sale_ID", "Total_On_Road_Amount_INR"]].head())
df.info()