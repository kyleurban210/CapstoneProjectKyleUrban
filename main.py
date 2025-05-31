import math 
import pandas as pd
file_name = "multinli_1.0_dev_matched.jsonl"


#read whole file
data_multi = pd.read_json(file_name, lines = True) #for reading the whole file






def main():
    #printing full data

    # Read the JSONL file

    # Set pandas to display all columns   #stolen from AI
    pd.set_option('display.max_columns', None)

    # Set pandas to display all rows   #stolen from AI
    pd.set_option('display.max_rows', None)

    # Set pandas to display full string values without truncation  #Stolen from AI
    pd.set_option('display.max_colwidth', None)



    #print column names
    print(data_multi.columns)




    #get the column names to read
    columns_to_read = ['sentence1'] #panda CANNOT handle more than one column at a time



    for x in columns_to_read:

        # Read the file in chunks and keep only specific columns
        chunk_size = 1000   #I wanna mess aroound with this number
        filtered_data = []

        for chunk in pd.read_json(file_name, lines=True, chunksize=chunk_size):
            filtered_data.append(chunk[x])

        ''''# Combine all chunks into a single DataFrame
        data_filtered = pd.concat(filtered_data, ignore_index=True)
        '''

        #pritnt out le chunk of data
        print(filtered_data)





    file_path = "new_file.txt"

    with open (file_path, "w", encoding='utf-8') as file:
        file.write(str(filtered_data))

    print(data_multi.columns)


    #stolen from AI to make the pandas rows switch back to not reading a fudge ton
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_colwidth')



    


























'''
    data_as_string = data_multi.to_string()
    print (data_as_string)
    data_amended_str = " "
'''

'''
    for x in range(len(data_as_string)):
        if data_as_string[x].isalnum() or data_as_string[x] == "\n" or data_as_string[x] == " " :
           data_amended_str += data_as_string[x]


    print(data_amended_str)
'''







main()