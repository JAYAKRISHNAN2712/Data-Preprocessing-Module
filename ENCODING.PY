import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from data_description import Data_Description

class Categorical:
    
    tasks = [
        '1.Show Categorical Column',
        '\n2.Performing One Hot Encoding',
        '\n3.Show the dataset'
        ]
    
    def __init__(self,data):
        self.data = data
        
    def Display_Categorical_Column(self):
        print('{0: <20}'.format("Categorical Column")+'{0: <5}'.format("Unique Values"))
        for column in self.data.select_dtypes(include = 'object'):
            print('{0: <20}'.format(column)+'{0: <5}'.format(self.data[column].nunique()))
            
    def Categorical_Encoding(self):
        categorical_columns = self.data.select_dtypes(include = 'object')
        while True:
            column = input("Which Column do you want to One-Hot Encode?(Press -1 to go back)\n")
            if column == -1:
                break
            if column in categorical_columns:
                self.data = pd.get_dummies(data=self.data,columns = [column])
                print("One Hot Encoding is done......")
                
                choice = input("Do you wanna to encode any another categorical column [Y/N] \n")
                if choice == 'y' or choice == 'Y':
                    continue
                else:
                    self.Display_Categorical_Column()
                    break
            else:
                print("Wrong Column Name....Try Again\n")
            break
        return self.data
    def Describe(self):
        while True:
            print("******* Tasks *********")
            for task in self.tasks:
                print(task)
                
            while True:
                try:
                    choice = int(input("What You Want to do???(Press -1 to go back)\n"))
                except ValueError:
                    print("Integer Value Required.Try Again.....")
                    continue
                break
            if choice == -1:
                break
            
            elif choice == 1:
                self.Display_Categorical_Column()
                
            elif choice == 2:
                self.Display_Categorical_Column()
                self.Categorical_Encoding()
                
            elif choice == 3:
                Data_Description.Display_Dataset(self)
                
            else:
                print("Wrong Value Entered!!!! Try Again")
        return self.data
    
       
        