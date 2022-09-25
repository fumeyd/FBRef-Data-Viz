import csv
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.cbook as cbook

class dataViz: 
    def __init__(self, csvData):
        self.data = csvData

    def getData(self):
        with open(self.data, encoding='utf8') as csv_file:
            data = csv.reader(csv_file)
        
        return(data)

    def getTitleColumns(self):
        with open(self.data, encoding='utf8') as csv_file:
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
        with open(self.data, encoding='utf8') as csv_file:
            csv_reader = csv.reader(csv_file)
            colIdx = colNameMap.get(colName)
            for row in csv_reader:
                colsData.append(row[colIdx])
        
        return(colsData)

    def mapDataToSquad(self, data, squads):
        map = {}

        for i in range(len(data)):
            map[squads[i]] = float(data[i])

        map = dict(sorted(map.items(),key=lambda x:x[1],reverse=False))

        return(map)

    def getRow(self, teamName):  
        with open(self.data, encoding='utf8') as csv_file: 
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

    def visualise(self, squads, d, xLabel, yLabel):
        fig = plt.figure(figsize=(10,10))
        plt.axis('equal')

        plt.xlabel(xLabel)
        plt.xticks([])
        plt.ylabel(yLabel)
        plt.yticks([])
        ax = fig.add_subplot()
        plotMap = {}

        xData = d[xLabel]
        yData = d[yLabel]
        squadIdx = 0;

        xMap = self.mapDataToSquad(xData, squads)
        yMap = self.mapDataToSquad(yData, squads)

        for xKey in xMap:
            plotMap[xKey] = [xMap[xKey]]

        for yKey in yMap:
            plotMap[yKey].append(yMap[yKey])

        squads = list(plotMap.keys())

        for squad, data in plotMap.items():
            ax.plot([data[0]], [data[1]], 'ro')

        for xy in plotMap.values():
            ax.annotate('(%s)' % squads[squadIdx], xy=xy, textcoords='data')
            squadIdx += 1

        plt.savefig('GD_vs_xGD.png')
        
        ax.grid()
        plt.show()
        

def main():
    data = {};
    # viz = dataViz('fbref_squad_passing.csv')
    viz = dataViz('fbref_xGD.csv')

    xData = viz.getColumn('xGD')
    yData = viz.getColumn('GD')
    squads = viz.getColumn('Squad')
    squads.remove('Squad')

    filtered_x = viz.remAlphaBs(xData);
    filtered_y = viz.remAlphaBs(yData)

    data['xGD'] = filtered_x
    data['GD'] = filtered_y

    # viz.visualise(filtered_xA, filtered_A);
    viz.visualise(squads, data, 'xGD', 'GD')

if __name__ == "__main__":
    main()

    