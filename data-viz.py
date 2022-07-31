import csv
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.cbook as cbook

class dataViz: 
    def __init__(self, csvData):
        self.data = csvData

    def getData(self):
        with open(self.data) as csv_file:
            data = csv.reader(csv_file)
        
        return(data)

    def getTitleColumns(self):
        with open(self.data) as csv_file:
            csv_reader = csv.reader(csv_file)
            for i in range(1):
                for row in csv_reader:
                    return row
 
    def colNameMap(self):
        dict = {};
        columns = self.getTitleColumns()
        idx = range(0, len(columns))
        for i in range(len(idx)):
            dict[columns[i]] = idx[i]

        return dict

    def getColumn(self, colName):
        colNameMap = self.colNameMap()
        colsData = []
        with open(self.data) as csv_file:
            csv_reader = csv.reader(csv_file)
            colIdx = colNameMap.get(colName)
            for row in csv_reader:
                colsData.append(row[colIdx])
        
        return(colsData)

    def getRow(self, teamName):  
        with open(self.data) as csv_file: 
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if teamName in row:
                    return(row)

    def remAlphaBs(self, data):
        for i in data:
            try:
                i = float(i)
            except:
                data.remove(i)

        return(data)

    def visualise(self, xList, yList):
        # cbookFile = cbook.open_file_cm(self.data, mode='r')

        fig, ax = plt.subplots(1, 1)
        for i in range(len(xList)):
            ax.plot(xList[i], yList[i])
        
        plt.show
        

def main():
    
    viz = dataViz('fbref_squad_passing.csv')
    teamRow = viz.getRow('Arsenal')

    map = viz.colNameMap(); 
    xAData = viz.getColumn('A-xA')
    AData = viz.getColumn('Ast')
    filtered_xA = viz.remAlphaBs(xAData);
    filtered_A = viz.remAlphaBs(AData)

    viz.visualise(filtered_xA, filtered_A);
    # print(titles)

if __name__ == "__main__":
    main()

    