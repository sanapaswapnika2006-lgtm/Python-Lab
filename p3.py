
import pandas as pd
import os

# Read CSV file
filename = input("Enter CSV file name: ")

if not os.path.exists(filename):
    print("File not found! Check the file name.")
else:
    try:
        df = pd.read_csv(filename)

        print("\nOriginal Dataset:")
        print(df)

        print("\nRows and Columns:", df.shape)

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nSummary Statistics:")
        print(df.describe(include="all"))

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Find numerical columns
        numeric_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        if numeric_columns:
            print("\nNumerical Columns:", numeric_columns)

            column = input("Enter column name to filter: ")

            if column in numeric_columns:
                value = float(input("Enter minimum value: "))

                filtered = df[df[column] >= value]

                print("\nFiltered Dataset:")
                print(filtered)

                filtered.to_csv("cleaned_data.csv", index=False)
                filtered.to_csv(
                    "cleaned_data.tsv",
                    sep="\t",
                    index=False
                )

                print("\nExport successful!")
                print("Created cleaned_data.csv")
                print("Created cleaned_data.tsv")
            else:
                print("Invalid column name.")
        else:
            print("No numerical columns found.")

    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")

    except Exception as e:
        print("Error:", e)
