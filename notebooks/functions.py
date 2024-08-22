#def replace_nulls_conditionally(df, columns, threshold=10, other_value='Unknown'):
    
    df2 = df.copy()
    
  1)  for column in columns:
         null_count = df[column].isna().sum()
         if null_count < threshold:
             top_value = df2[column].mode()[0]
             df2[column] = df2[column].fillna(top_value)
         else:
             df2[column] = df2[column].fillna(other_value)
             
    return df2

        # null_count = df[column].isna().sum()
        # if null_count < threshold:
            # top_value = df[column].mode()[0]
            # df[column] = df[column].replace(np.nan, top_value)
        # else:
            # df[column] = df[column].replace(np.nan, other_value)
        # return df 
df = replace_nulls_conditionally(df, ['maternal_self', 'finbar','compend','sh_covered'])
print("\nUpdated DataFrame:")
display(df)

2)def get_countries_in_oceania(df):
    """
    Retrieve countries where the continent is Oceania.

    Parameters:
    df (DataFrame): A pandas DataFrame containing country and continent data.

    Returns:
    list: A list of countries located in Oceania.
    """
    # Use boolean indexing to filter the DataFrame
    return df[df['Continent'] == 'Oceania']['Country'].tolist()

# Get and print the list of countries in Oceania
oceania_countries = get_countries_in_oceania(df)
print("Countries in Oceania:")
print(oceania_countries)

3)def filter_by_country(df, country_list):
    """
    Filter the DataFrame to include only rows where the 'Country' column matches a value in the provided country list.
    
    
    country_list (list): A list of countries to fi\lter the DataFrame by.
    
    Returns:
    pd.DataFrame: A DataFrame containing only the rows where the 'Country' matches a value in the country list.
    """
    filtered_df = df[df['Country'].isin(country_list)]
    return filtered_df

# List of countries to filter by
countries_to_filter = ['Norway', 'Greece','France','Germany','United States','Brazil','Colombia','Japan','New Zealand','Pakistan','Ghana','Cameroon']

# Call the function with the DataFrame and the list of countries
filtered_df = filter_by_country(df, countries_to_filter)

# Display the filtered DataFrame
display(filtered_df)