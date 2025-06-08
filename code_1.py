import pandas as pd
import os

def create_dataframe():
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [22, 25, 22, 28, 35]
    }
    df = pd.DataFrame(data)
    return df

def save_dataframe(df):
    if not os.path.exists("data"):
        os.makedirs("data")
    df.to_csv("data/data.csv", index=False)
    print("data.csv saved in data folder")

def process_data():
    df = pd.read_csv("data/data.csv")  # Read the saved file
    
    # Correct filtering using Pandas
    filtered_df = df[df["Age"] > 25]  

    # Save filtered data
    filtered_df.to_csv("data/filtered_people.csv", index=False)
    print("filtered_people.csv saved in data folder")
    
    return filtered_df

if __name__ == '__main__':
    df = create_dataframe()
    save_dataframe(df)
    filtered_df = process_data()
    print(filtered_df)