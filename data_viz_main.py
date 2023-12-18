import data_viz as dataViz

def main():
    data = {}

    viz = dataViz.dataViz('fbref_xGD_v2.csv')

    xData = viz.getColumn('xGD')
    yData = viz.getColumn('GD')

    squads = viz.getColumn('Squad')
    squads.remove('Squad')

    filtered_x = viz.remAlphaBs(xData)
    filtered_y = viz.remAlphaBs(yData)

    data['xGD'] = filtered_x
    data['GD'] = filtered_y


    viz.visualise(squads, data, 'xGD', 'GD')

if __name__ == "__main__":
    main()


