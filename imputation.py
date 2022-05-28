import pandas as pd
from data_description import Data_Description 

class Imputation:
    tasks = [
        '\n1.Show Number of Null values',
        '2.Remove columns',
        '3.Fill Null Values with mean',
        '4.Fill Null Values with median',
        '5.Fill Null Values with mode',
        '6.Display the dataset'
        ]
    def __init__(self,data):
        self.data = data
        
    def showColumns(self):
        for column in self.data.columns:
            print(column)
            
    def Count_Null_Values(self):
        print("\n Null Values in Each Column")
        for column in self.data.columns.values:
            print(column,"   :   ",self.data[column].isna().sum())
            
    def Remove_Columns(self):
        self.showColumns()
        while(1):
            columns = input("\nEnter the column you want to drop\n")
            
            if columns == -1:
                break
            
            choice = input("\nAre you sure(y/n)")
            if choice == 'y' or choice == 'Y':
                try:
                    self.data.drop(columns,inplace = True,axis = 1)
                except KeyError:
                    print("\nOne or more Columns are not present...please try again!!!")
                    continue
                print("\nDropping of Desired Column is Done!!!!")
                break
            else:
                print("\nNot Deleting...............")
                
        return self.data
    def Fill_Null_Mean(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column\n")
            
            if column == -1:
                break
            try:
                 col = self.data[column]
                 self.data[column].fillna(col.mean(),inplace = True)
                 print("Displaying the "+column)
                 print(self.data[column])
            except KeyError:
                print("\nColumn not present in dataset....Please Try Again....")
                continue
            break
        return self.data
    
    def Fill_Null_Median(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column")
            
            if column == -1:
                break
            try:
                 col = self.data[column]
                 self.data[column].fillna(col.median(),inplace = True)
            except KeyError:
                print("\nColumn not present in dataset....Please Try Again....")
                continue
            break
        return self.data 

    def Fill_Null_Mode(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column")
            
            if column == -1:
                break
            try:
                 col = self.data[column]
                 self.data[column].fillna(col.mode(),inplace = True)
            except KeyError:
                print("\nColumn not present in dataset....Please Try Again....")
                continue
            break
        return self.data
    
    def Display_Dataset(self):
        Data_Description.Display_Dataset(self)
        
    def Describe(self):
        while True:
            for task in self.tasks:
                print(task)
            while True:
                try:
                    choice = int(input("How do you want to Impute(Enter -1 to QUIT)???\n"))
                except ValueError:
                    print("Enter Integer Value (1-6)\n")
                    continue
                break
            if choice == -1:
                break
            elif choice == 1:
                self.Count_Null_Values()
            elif choice == 2:
                self.Remove_Columns()
            elif choice == 3:
                self.Fill_Null_Mean()
            elif choice == 4:
                self.Fill_Null_Median()
            elif choice == 5:
                self.Fill_Null_Mode()
            elif choice == 6:
                self.Display_Dataset()
                
            print("\n Do you want to continue Imputation(y/n)!!!!!!!!\n")
            choice = input()
            if choice == 'y' or choice == 'Y':
                continue
            else:
                break
        return self.data

