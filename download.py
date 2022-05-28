import pandas as pd

class Download:
    def __init__(self,data):
        self.data = data
        
    def Dataset_download(self):
        download_dataset = {}
        for column in self.data.columns.values:
            download_dataset[column] = self.data[column]
        
        filename = input("Enter the file name do you want?(Press -1 to go back)")
        if filename == "-1":
            return
        filename = filename+".csv"
        pd.DataFrame(self.data).to_csv(filename,index = False)
        
        print("CONGRATULATIONS...... It's done!!!!!")
        
        if input("Do you want to exit now?[Y/N]").lower() == 'y':
            print("Exiting.....")
            return
        else:
            return
        