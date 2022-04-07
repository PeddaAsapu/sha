import glob
import os
import pandas as pd

# the output of transform function is the input for this
input_file_name = 'filename.csv'
reference_data = pd.read_csv(input_file_name)
reference_isin_list = reference_data['security'].unique().tolist()

def search_files(filename) :
    output_df = pd.DataFrame()
    output_filename = 'output_file.csv'
    data = pd.read_csv(filename)
    for each_isin in reference_isin_list :
        row = data[data['security'] == each_isin]
        output_df = pd.concat([row, output_df])
    if os.path.exists(output_filename) :
        output_df.to_csv(output_filename, mode='a', index=False, header=False)     
    else :
        output_df.to_csv(output_filename,index=False)        


if __name__ == '__main__' :

    # give the path where the files are present - The same path will be used for storing outputfile
    directory_path = '/Users/peddababuasapu/Documents/usha/files'
    os.chdir(directory_path)

    files = files = [file for file in glob.glob('Vg_ibor*.csv')]
    if files : [search_files(each_file) for each_file in files]