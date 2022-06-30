from tabnanny import check
import pandas as pd
import os

def give_index(data) :
    data = data.sort_values(by=['event_id'])
    checked_id = []
    required_index = []
    for index in data.index :
        percentage_threshold = 0.1
        event_id = data['event_id'][index]
        country = data['country'][index]
        if index > 0 :
            previous_country = data['country'][index-1]
        if event_id not in checked_id or country != previous_country :  
            filter_out_df = data[(data['event_id'] == event_id) & (data['country']==country)]
            reportable_df = filter_out_df[filter_out_df['percentage'] < percentage_threshold] 
            checked_id.append(event_id)
            if not reportable_df.empty :
                for i in range(len(filter_out_df)) :
                    required_index.append(index+i)
    return required_index


def give_updated_df(index_information) :
    additional_column = []
    for row in range(len(data)) :
        if row in index_information :
            additional_column.append('reportable')
        else :
            additional_column.append('Not Reportable')
    data['additional_column'] = additional_column
    return data


if __name__ == '__main__' :
    # give the path where the files are present - The same path will be used for storing outputfile
    directory_path = '/Users/peddababuasapu/Documents/usha'
    os.chdir(directory_path)
    data = pd.read_csv('usha_data.csv')
    required_df = give_updated_df(give_index(data))
    print(required_df)