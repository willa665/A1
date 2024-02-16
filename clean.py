import pandas as pd

def clean_data(input1, input2, output):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    df3 = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    df3.drop('id', axis=1, inplace=True)
    df3.dropna(inplace=True)

    job = df3['job'].str.contains('insurance|Insurance', case=False)
    df4 = df3[job]
    df4 = df4[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]
    df4.reset_index(drop=True, inplace=True)
    df4.to_csv(output, index=False)

if __name__ == "__main__":
    # Specify the file paths
    input1 = r"/Users/lelewang/Desktop/Course2/7035AI/Assignment1/respondent_contact.csv"
    input2 = r"/Users/lelewang/Desktop/Course2/7035AI/Assignment1/respondent_other.csv"
    output = r"/Users/lelewang/Desktop/Course2/7035AI/Assignment1/respondent_cleaned.csv"

    # Call the clean_data function
    clean_data(input1, input2, output)

# Print the shape of the output file
    output_df = pd.read_csv(output)
    num_rows, num_columns = output_df.shape
    print("Shape of the output file: ", num_rows, "rows", num_columns, "columns")
