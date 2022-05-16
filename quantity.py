import pandas as pd

"""
Facts:
File one.csv - wont have any duplicate data
two.csv - will have duplicate ISIN values.
Each existing row in two.csv will have L or S as distinguished.
"""

file_main_name = 'one.csv'
file_to_search_name = 'two.csv'
# giving the same name as input file, As you need the file to be replaced
output_filename = file_main_name

def count_quantity(file_main_name, file_to_search_name) :
    """
    Doesn't return anything.
    takes two csv file names in csv format.
    for each isin value in first file, checks the total quantity in second file and stores the values in 
    first file.
    """
    file_main = pd.read_csv(file_main_name)
    file_to_search =  pd.read_csv(file_to_search_name)
    required_data=[]
    for each_isin in file_main['ISIN'] :
        quantity_data = {
            "ISIN" : each_isin
        }
        df_to_check = file_to_search[file_to_search['ISIN'] == each_isin] 
        sum_of_long = df_to_check[df_to_check['Long_Short_indicator'] == 'L']['quantity'].sum()
        sum_of_short = df_to_check[df_to_check['Long_Short_indicator'] == 'S']['quantity'].sum()
        quantity_data['quantity_long'] = sum_of_long
        quantity_data['quantity_short'] = sum_of_short
        required_data.append(quantity_data)
        # we can achieve the same result by the below two steps as well, But I don't recommend.
        #file_main[file_main['ISIN'] == each_isin]['quantity_long'] = sum_of_long
        #file_main[file_main['ISIN'] == each_isin]['quantity_short'] = sum_of_short
    quantity_df = pd.DataFrame(required_data)
    df_final = pd.merge(file_main, quantity_df, on="ISIN")
    # REPLACE ID field with any index field
    df_final = df_final.set_index('ID')
    df_final.to_csv(output_filename)

#calling the Function
count_quantity(file_main_name, file_to_search_name)