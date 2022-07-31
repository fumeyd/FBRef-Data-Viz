import csv
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.cbook as cbook

class dataViz: 
    def __init__(self, csvData):
        self.data = csvData 

    def getData(self):
        with open(self.data) as csv_file:
            data = csv_file.read()
        
        return(data)

    def getTitleColumns(self):
        with open(self.data) as csv_file:
            csv_reader = csv.reader(csv_file)
            for i in range(0):
                for row in csv_reader:
                    return row

    def getRow(self, teamName):  
        with open(self.data) as csv_file: 
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if teamName in row:
                    return(row)

    def visualise(self):
        csvFile = 'C:/Users/kwaks/OneDrive - Ashesi University/Personal Work Stuff/fbref-data-viz/fbref_squad_passing.csv'
        cbookFile = cbook.open_file_cm(csvFile, mode='r')
        
        # refinedData = (cbook.open_file_cm(csvFile, mode='r')['Prog']
        # .view(np.recarray))
        
        fig, ax = plt.subplots()
        

def main():
    
    viz = dataViz('fbref_squad_passing.csv')
    titles = viz.getTitleColumns()
    teamRow = viz.getRow('Arsenal')
    viz.visualise();

    print(titles)

if __name__ == "__main__":
    main()

    