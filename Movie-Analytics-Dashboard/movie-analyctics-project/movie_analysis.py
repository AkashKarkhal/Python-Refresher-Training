import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

pd.set_option("display.max_columns", None)

engine = create_engine(
    "mysql+pymysql://root:cfg%4012345678@localhost/alpacino_db"
)

df = pd.read_sql("SELECT * FROM movies", engine)

df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["Metascore"] = pd.to_numeric(df["Metascore"], errors="coerce")
df["Relese Date"] = pd.to_datetime(df["Relese Date"], errors="coerce")

print("\n" + "=" * 60)
print("MOVIE ANALYTICS REPORT")
print("=" * 60)

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nMissing Values")
print(df.isnull().sum())

print("\nMovie Types")
print(df["Type"].value_counts())

print("\nTop 10 Directors")
print(df["Director"].value_counts().head(10))

print("\nTop 10 Countries")
print(df["Country Origin"].value_counts().head(10))

print("\nTop 10 Genres")
print(df["Genre"].value_counts().head(10))

print("\nTop 10 Languages")
print(df["Languages"].value_counts().head(10))

print("\nRating Statistics")
print("Average Rating :", round(df["Rating"].mean(), 2))
print("Highest Rating :", df["Rating"].max())
print("Lowest Rating  :", df["Rating"].min())

print("\nMetascore Statistics")
print("Average Metascore :", round(df["Metascore"].mean(), 2))
print("Highest Metascore :", df["Metascore"].max())
print("Lowest Metascore  :", df["Metascore"].min())

print("\nTop Rated Movies")
top_movies = df.sort_values("Rating", ascending=False)
print(top_movies[["Title", "Rating"]].head(10))

df["Year"] = df["Relese Date"].dt.year

sns.set_style("whitegrid")

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Type", palette="Set2")
plt.title("Movies vs Series")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
df["Genre"].value_counts().head(10).plot(
    kind="bar",
    color="royalblue"
)
plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
df["Director"].value_counts().head(10).plot(
    kind="bar",
    color="darkorange"
)
plt.title("Top 10 Directors")
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df["Rating"], bins=15, kde=True, color="green")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

yearly_movies = df["Year"].value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.plot(
    yearly_movies.index,
    yearly_movies.values,
    marker="o",
    linewidth=2,
    color="crimson"
)
plt.title("Movies Released By Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.show()

top_countries = df["Country Origin"].value_counts().head(10)

plt.figure(figsize=(10, 8))
plt.pie(
    top_countries.values,
    labels=top_countries.index,
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Top Countries Distribution")
plt.tight_layout()
plt.show()

rating_genre = (
    df.groupby("Genre")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
rating_genre.plot(
    kind="bar",
    color="purple"
)
plt.title("Top Genres By Average Rating")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n" + "=" * 60)

df.to_excel("alpacino_movies.xlsx", index=False)

print("Excel file created successfully")