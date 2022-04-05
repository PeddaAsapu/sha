import sys
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def append_func(list,row_data) :
    output_df = pd.DataFrame()
    df = pd.DataFrame(columns=['id', 'security','security_type','name', 'nsi'])
    series = pd.Series(list, index = df.columns)
    df = df.append(series, ignore_index=True)
    merged = pd.merge(row_data,df)
    output_df = output_df.append(merged)

    return output_df


def transform(datafile) :

    data = pd.read_csv(datafile, chunksize=1)
    final_output_df = pd.DataFrame()
    row = 0
    for each_row in data : 
        try :
            offeree_list = [each_row['id'][row],each_row['offereesec'][row],'offeree',each_row['offereename'][row],each_row['offereensi'][row]]
            offeror_list = [each_row['id'][row],each_row['offerorsec'][row],'offeror',each_row['offerorname'][row],each_row['offerornsi'][row]]     
            final_output_df = final_output_df.append(append_func(offeree_list,each_row)).append(append_func(offeror_list,each_row))
            row += 1
        except :
            e = sys.exc_info()
            print(str(e))

    return final_output_df.to_csv('surya.csv')


if __name__ == '__main__':
    transform('data.csv')