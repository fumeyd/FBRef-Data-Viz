import csv
import matplotlib.pyplot as plt 

class dataViz: 
    def __init__(self, csvData):
        self.rows = []
        self.cols = []
        self.data = self.getData(csvData)

    def getData(self, csvData):

        with open(csvData, encoding='utf8') as csv_file:
            data = csv.reader(csv_file)
            
            # get rows
            for i in range(1):
                for row in data:
                    self.rows.append(row)
            # get cols
            for i in range(len(self.rows[0])):
                curr_col = []
                for row in self.rows:
                    curr_col.append(row[i])
                self.cols.append(curr_col)

        return data

    def getColumn(self, colName):
        for cols in self.cols:
            if cols[0] == colName:
                return cols 
            
    def getRow(self, teamName):  
        for row in self.rows:
                if row[1] == teamName:
                    return row

    def mapDataToSquad(self, data, squads):
        map = {}

        for i in range(len(data)):
            map[squads[i]] = float(data[i])

        map = dict(sorted(map.items(),key=lambda x:x[1],reverse=False))

        return map

    def getPlotMap(self, xData, yData, squads):
        plotMap = {}
        
        xMap = self.mapDataToSquad(xData, squads)
        yMap = self.mapDataToSquad(yData, squads)

        for xKey in xMap:
            plotMap[xKey] = [xMap[xKey]]

        for yKey in yMap:
            plotMap[yKey].append(yMap[yKey])

        return plotMap

    def remAlphaBs(self, data):
        for i in data:
            try:
                i = float(i)
            except:
                data.remove(i)

        return data

    def visualise(self, squads, d, xLabel, yLabel):
        fig = plt.figure(figsize=(15,15))
        plt.axis('equal')

        plt.xlabel(xLabel)
        plt.xticks([])
        plt.ylabel(yLabel)
        plt.yticks([])
        ax = fig.add_subplot()

        xData = d[xLabel]
        yData = d[yLabel]
        squadIdx = 0;

        plotMap = self.getPlotMap(xData, yData, squads)
        squads = list(plotMap.keys())

        for squad, data in plotMap.items():
            ax.plot([data[0]], [data[1]], 'ro')

        for xy in plotMap.values():
            ax.annotate('(%s)' % squads[squadIdx], xy=xy, textcoords='data')
            squadIdx += 1

        plt.savefig('GD_vs_xGD.png')
        
        ax.grid()
        plt.show()
        
    