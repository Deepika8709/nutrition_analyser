import pandas as pd
df = pd.read_csv("nutrients_csvfile.csv")

print ("\n Total Foods :", len(df))
print(df.sort_values("Protein",ascending=False).head(10)[["Food","Protein"]])
print(df.sort_values("Protein").head(10)[["Food", "Protein"]])
#convert numeric columns
df["Protein"] = pd.to_numeric(df["Protein"], errors="coerce")
df["Calories"] = pd.to_numeric(df["Calories"], errors="coerce")
#Drop rows with missing values in important columns
df = df.dropna(subset=["Protein", "Carbs", "Fiber", "Calories"])
print("\n Top 10 protein foods")
high_protein_20 = df[df["Protein"] > 20]
print(high_protein_20[["Food", "Protein"]].head(10))

print("\nTop 10 Fiber foods")
high_fiber = df.sort_values("Fiber", ascending=False).head(10)
print(high_fiber[["Food", "Fiber"]])

print("\nBest protein food per calorie")
df["Protein_per_cal"] = df["Protein"] / df["Calories"]
best_protein_per_cal = df.sort_values("Protein_per_cal", ascending=False)
print(best_protein_per_cal[["Food", "Protein_per_cal"]].head(10))


# Print highcarb foods
df["Fat"] = pd.to_numeric(df["Fat"], errors="coerce")
df["Carbs"] = pd.to_numeric(df["Carbs"], errors="coerce")
df["highcarbs"] = (df["Fat"] + df["Carbs"])
High_sug = df.sort_values("highcarbs", ascending=False)
print(High_sug[["Food", "highcarbs"]].head(10))

print( "\n *********Analysis complete*********")