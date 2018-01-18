from approach.config.imports import *

from approach.Column import Column

class Dataset(object):

    def __init__(self, path):
        self.name      = path
        self.df        = pd.read_csv(os.path.join(path))
        self.noRows    = self.df.size
        self.noColumns = len(self.df.columns)
        self.columns   = self.getColumns()

    # def getHeaders(self):
    #     headers = []
    #     for header in self.df.columns:
    #         headers.append(header)
    #     return headers
    #
    # def printHeaders(self):
    #     for index, header in enumerate(self.headers):
    #         print str(index) + ": " + header

    def getColumns(self):
        columns = []
        for header in self.df.columns:
            #print self.df[header]
            columns.append(Column(header, self.df[header]))


        return columns
