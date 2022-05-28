from os import path
import sys
import pandas as pd

class Data_Input:
    
    # Extensions supported by this project
    supported_file_extension = ['.csv',]
    
    # Function to convert column names in lowercase
    def convert_to_lowercase(self,df):
        df.columns = df.columns.str.lower()
        return df
    # Function that take any dataset from input file and convert it into dataframe
    def Input_Dataset(self):
        try:
            filename,file_extension = path.split("C:\\Users\\HP\\Datasets\\archive\\exoTrain\.csv")
            if file_extension == "":
                raise SystemExit("Provide the file extension")
            if file_extension not in self.supported_file_extension:
                print("file name : ",filename,"\n")
                print("file extension : ",file_extension)
                raise SystemExit("File extension not supportable")
        except IndexError:
            raise SystemExit("Provide the dataset with name and extension")
        try:
            df = pd.read_csv(filename+file_extension)
        except pd.errors.EmptyDataError:
            raise SystemExit("The file is empty")
        except FileNotFoundError:
            raise SystemExit("File does'nt exit")
        df = self.convert_to_lowercase(df)
        return df
        
        