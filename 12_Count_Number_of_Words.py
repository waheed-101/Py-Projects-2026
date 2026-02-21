# counts the number of words in a DataFrame column using Pandas.

import pandas as pd 

# Sample DataFrame
data = {
    "Sentences": [
        "Python is amazing",
        "I love data science",
        "Count words in a column",
        "GitHub is great for projects",
        "Hello world"
    ]
}

df = pd.DataFrame(data)

# Count words in each row of the column
df["Word_Count"] = df["Sentences"].apply(lambda x: len(str(x).split()))

# Total word count
total_words = df["Word_Count"].sum()

print(df)
print(f"\nTotal Word Count: {total_words}")