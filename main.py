import pandas as pd
from data_description import Data_Description
from data_input import Data_Input
from imputation import Imputation
from download import Download
from ENCODING import Categorical
from feature_scaling import Feature_Scaling

class Preprocessor:
    tasks = [
        '1.Data Description',
        '2.Handling Null Values',
        '3.Encoding Categorical Data',
        '4.Feature Scaling of the Dataset',
        '5.Download the modified dataset'
        ]
    
    def __init__(self):
        self.data = Data_Input().Input_Dataset()
    
    def preprocessorMain(self):
        while True:
            print("******* Tasks *******")
            for task in self.tasks:
                print(task)
            while True:    
                try:
                    choice = int(input(" How you want to pre-process the data????\n"))
                except ValueError:
                    print("Integer value required.Try Again......")
                    continue
                break
            if choice == -1:
                exit()
            
            elif choice == 1:
                Data_Description(self.data).Describe()
                
            elif choice == 2:
                self.data = Imputation(self.data).Describe()
                
            elif choice == 3:
                self.data = Categorical(self.data).Describe()
                
            elif choice == 4:
                self.data = Feature_Scaling(self.data).Describe()
                
            elif choice == 5:
                Download(self.data).Dataset_download()
                
            else:
                print("Entered Wrong Choice.....Try Again\n")
                continue
            break
        return 
    

ob = Preprocessor()
ob.preprocessorMain()
                