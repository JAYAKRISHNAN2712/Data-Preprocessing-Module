import pandas as pd
from data_description import Data_Description
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Feature_Scaling:
    
    tasks = [
        '1.Perform Normalization (using MinMax Scaler)',
        '2.Perform Standardization (using Standard Scaler)',
        '3.Show the Dataset'
        ]
    
    normalization_tasks = [
        '1.Perform Normalization for selective columns',
        '2.Perform Normalization for whole Dataset',
        '3.Show the Dataset'
        ]
    standardization_tasks = [
        '1.Perform Standardization for selective columns',
        '2.Perform Standardization for whole datset'
        '3.Show the Dataset'
        ]
    
    def __init__(self,data):
        self.data = data
        
    def Normalization(self):
        while True:
            print("\n Normalization Tasks")
            
            for task in self.normalization_tasks:
                print(task)
                
            while True:
                
                try:
                    choice = int(input("How do you want to perform Normalization(Press -1 to go back)????\n"))
                except ValueError:
                    print("Please....Enter the Integer Value")
                    continue
                break
            
            if choice == -1:
                break
            
            elif choice == 1:
                columns = input("Please Enter the name of those column(s) for which you want to perform Normalization(Press -1 to Go back)!!!!!!\n").split(" ")
                
                if columns == -1:
                    break
                
                for column in columns:
                    try:
                        min_value = self.data[column].min()
                        max_value = self.data[column].max()
                        self.data[column] = (self.data[column] - min_value)/(max_value - min_value)
                    except:
                        print("Sorry!!! Not Possible.......\n")
                    print("Normalization Done!!!!!")
                    
            elif choice == 2:
                try:
                    for column in self.data.columns:
                        min_value = self.data[column].min()
                        max_value = self.data[column].max()
                        self.data[column] = (self.data[column] - min_value)/(max_value - min_value)
                except:
                    print("String columns are present....\n")
                print("Normalization Done!!!!!")
            
            elif choice == 3:
                Data_Description.Display_Dataset(self)
                
            else:
                print("You Pressed the long key.....Try again !!!!!!")
                continue
        return
    
    def Standardization(self):
        while True:
            print("\n Standization Tasks...\n")
            
            for task in self.standardization_tasks:
                print(task)
                
            while True:
                try:
                    choice = int(input("How do you want to standardize???(Press -1 to go back)"))
                except ValueError:
                    continue
                break
            
            if choice == -1:
                break
            
            elif choice == 1:
                columns = input("Please Enter the name of those column(s) for which you want to perform Standardization(Press -1 to Go back)!!!!!!\n").split(" ")
                
                if columns == -1:
                    break
                
                for column in columns:
                    try:
                       mean = self.data[column].mean()
                       std_dev = self.data[column].std()
                       self.data[column] = (self.data[column] - mean)/(std_dev)
                    except:
                        print("Sorry!!! Not Possible.......\n")
                        
                    print("Standardization Done!!!!!")
                    
            elif choice == 2:
                
                try:
                    for column in self.data.columns:
                        mean = self.data[column].mean()
                        std_dev = self.data[column].std()
                        self.data[column] = (self.data[column] - mean)/(std_dev)
                        
                except:
                    print("String Columns are Present.....\n")
                    
                print("Standardization Done!!!!!")
                
            elif choice == 3:
                Data_Description.Display_Dataset(self)
                
            else:
                print("\n You Pressed Wrong Value....Try Again!!!!!")
                continue
        return 
    
    def Describe(self):
        while True:
            
            print("Showing Columns present in Dataset.....\n")
            Data_Description.showColumns(self)
            print("\n")
            for task in self.tasks:
                print(task)
            choice = int(input("What you want to do????(Press -1 to go back)\n"))
                
            if choice == -1:
                break
            
            elif choice == 1:
                self.Normalization()
                
            elif choice == 2:
                self.Standardization()
                
            elif choice == 3:
                Data_Description.Display_Dataset(self)
                
            else:
                print("\n You Pressed Wrong Value.....Try Again!!!!!")
                
            ans = input("Do you want to continue Feature Scaling [y/n] !!!!!!\n")
            if ans == 'y' or ans == 'Y':
                continue
            else:
                return self.data
        return self.data
        

        
                        
                
                
                    
                    
        
                
                        
                
            
                
                
        