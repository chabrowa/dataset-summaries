from approach.config.imports import *
from tabulate import tabulate

class Statistics(object):

    def __init__(self, dataset):
        self.dataset = dataset

    def printDatasetStats(self):
        print "<----------- DATASET STATISTICS ----------->"
        print "Dataset: " + str(self.dataset.name)
        print "Number of columns: " + str(self.dataset.noColumns)
        print "Number of rows: " + str(self.dataset.noRows)
        print "Number of numerical columns: " + str(len(self.dataset.columns['numerical']))
        print "Number of textual columns: " + str(len(self.dataset.columns['textual']))
        print ""

    def printDatasetStatsTabular(self):
        print "DATASET STATISTICS"
        print (tabulate([
                ['Dataset', self.cutDatasetName(str(self.dataset.name))],
                ['Number of columns', str(self.dataset.noColumns)],
                ['Number of rows', str(self.dataset.noRows)],
                ['Number of numerical columns', str(len(self.dataset.columns['numerical']))],
                ['Number of textual columns', str(len(self.dataset.columns['textual']))]
                ], tablefmt="plain", numalign="right"))
        print ""

    def printNumericalStats(self):
        print "<----------- NUMERICAL STATISTICS --------->"
        counter = 1
        for numColumn in self.dataset.columns['numerical']:
            print "Column " + str(counter) + ": "
            print "\tMin: " + str(numColumn.minVal)
            print "\tMax: " + str(numColumn.maxVal)
            print "\tMedian: " + str(numColumn.median)
            print "\tAverage: " + str(numColumn.average)
            counter += 1
        print ""

    def printNumericalStatsTabular(self):
        print "NUMERICAL STATISTICS"
        counter = 1
        table = []
        for numColumn in self.dataset.columns['numerical']:
            shortName = numColumn.name
            if len(numColumn.name) > 30:
                shortName = numColumn.name[:30]+'...'
            table.append(['Column Index:', numColumn.index + 1, 'Header:', shortName, 'Min:', str(numColumn.minVal), 'Max:', str(numColumn.maxVal), 'Median:', str(numColumn.median), 'Average:',  str(numColumn.average)])
            counter += 1

        print (tabulate(table, tablefmt="plain", numalign="right"))
        print ""

    def printHeadersStats(self):
        print "HEADER STATISTICS"
        counter = 1
        table = []
        for h in self.dataset.header.values:
            table.append([str(counter), h.replace('\n', ' ')])
            counter += 1

        print (tabulate(table, tablefmt="plain", numalign="right", headers=["Column", "Header"] ))
        print ""

    def printSubjectColumn(self):
        print "SUBJECT COLUMN"
        print "First column containing texutal information is assumed to be subject column "
        print "If other column or more column give better overview of the whole table please change"
        print (tabulate([
                ['Index:', str(self.dataset.columns['textual'][0].index)],
                ['Header:', str(self.dataset.columns['textual'][0].name)],
                ['Top 10:', 'TODO'],
                ['Bottom 10:', 'TODO']
                ], tablefmt="plain", numalign="right"))
        print ""



    def cutDatasetName(self, datasetName):
        temp = datasetName.rfind("/")
        fileName = datasetName[temp+1:]
        return fileName
