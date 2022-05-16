import os
import pandas as pd

# the output of transform function is the input for this
file_main_name = 'one.csv'
file_to_search_name = 'two.csv'

file_main = pd.read_csv(file_main_name)
file_to_search =  pd.read_csv(file_to_search_name)

print(file_main)
print("#" * 100)
print(file_to_search)