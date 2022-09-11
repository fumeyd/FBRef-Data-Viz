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

    # def visualise(self, xList, yList):
    def visualise(self, squads, d, xLabel, yLabel):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        ax.plot(xLabel, yLabel, 'ro', data=d)
        # plt.plot(xList, yList, 'ro')

        xData = d[xLabel]
        yData = d[yLabel]
        squadIdx = 1;

        for xy in zip(xData,yData):
            ax.annotate('(%s)' % squads[squadIdx], xy=xy, textcoords='data')
            squadIdx += 1

        plt.savefig('xA_vs_A.png')
        
        ax.grid()
        plt.show
        

def main():
    data = {};
    viz = dataViz('fbref_squad_passing.csv')

    map = viz.colNameMap(); 

    xAData = viz.getColumn('A-xA')
    AData = viz.getColumn('Ast')
    squads = viz.getColumn('Squad')

    filtered_xA = viz.remAlphaBs(xAData);
    filtered_A = viz.remAlphaBs(AData)

    data['A-xA'] = filtered_xA
    data['Ast'] = filtered_A

    # viz.visualise(filtered_xA, filtered_A);
    viz.visualise(squads, data, 'A-xA', 'Ast')
    # print(titles)

if __name__ == "__main__":
    main()

    