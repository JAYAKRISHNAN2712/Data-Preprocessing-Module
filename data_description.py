import pandas as pd

class Data_Description:
    tasks = ['\n1.1.Show the columns',
    '2.Describe column or dataset ',
    '3.Display the dataset'
    ]
    def __init__(self,data):
        self.data = data
    def Display_Dataset(self):
        while True:
            try:
                rows=int(input("Enter Number of rows(>0)\n"))
                if rows == -1:
                    break
                if rows <= 0:
                    print("No: of rows in +ve")
                    continue
                print(self.data.head(rows))
            except ValueError:
                print("Enter Integer Value")
                continue
            break
        #None
    def showColumns(self):
        for column in self.data.columns:
            print(column)
    def Describe(self):
        while True:
            for task in self.tasks:
                print(task)
            while True:
                try:
                    choice = int(input("What you want to do???\n"))
                except ValueError:
                    print("Enter Integer Value")
                    continue
                break
            if choice == -1:
                break
            elif choice == 1:
                self.showColumns()
                while True:
                    try:
                        desc_column = input("Enter the column")
                        print(self.data[desc_column])
                    except KeyError:
                        print("Column not present...")
                        continue
                    break
            elif choice == 2:
                print(self.data.describe())
            elif choice == 3:
                self.Display_Dataset()
            else:
                print("Incorrect Choice")
                continue
            if input("Do you want you continue [Y/N] ???").lower() == 'y':
                continue
            else:
                break
                    
                