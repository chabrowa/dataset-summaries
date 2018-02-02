from approach.config.imports import *

from approach.NumericalColumn import NumericalColumn
from approach.TextualColumn import TextualColumn
from approach.Headers import Headers

class Dataset(object):

    def __init__(self, path):
        self.name             = path
        self.df               = pd.read_csv(os.path.join(path))
        self.noRows           = self.df.size
        self.noColumns        = len(self.df.columns)
        self.columns          = self.getColumns()
        self.header           = Headers(self.df.columns)

    def getColumns(self):
        columns = {}
        columns['numerical'] = []
        columns['textual']   = []

        counter = 0
        for header in self.df.columns:
            columnType = self.getColumnType(self.df[header])
            #print columnType
            if columnType == 0:
                columns['numerical'].append(NumericalColumn(header, self.df[header], counter))
            else:
                columns['textual'].append(TextualColumn(header, self.df[header], counter))
            counter += 1

        return columns

    def getColumnType(self, column):
        numerical, textual, total = 0, 0, 0

        for val in column:
            if not self.isNan(val):

                if self.isNumber(val):
                #if val.isdigit():
                    #print "we are here"
                    numerical = numerical + 1
                else:
                    textual = textual + 1
                total = total + 1

        #print "numerical: " + str(numerical) + "; textual: " + str(textual)

        #if numerical == 0 and textual == 0:
            #for val in column:
                #print str(type(float(val))) + ": "+ str(val)
                #self.isNumberTest(val)
                # print val
                # if not self.isNan(val):
                #
                #     if self.isNumber(val):
                #         print "number"
                #     #if val.isdigit():
                #         #print "we are here"
                #         numerical = numerical + 1
                #     else:
                #         print 'text'
                #         textual = textual + 1
                #     total = total + 1
                # else:
                #     print "nan"
                # print "--------------"

        if numerical > textual:
            return 0
        else:
            return 1


    def isNumber(self, value):
        try:
            value = value.replace(',','')
            value = value.replace('.','')
            value = float(value)
            return True
        except Exception, e:
            return False

    def isNan(self, value):
        try:
            value = float(value)
            if math.isnan(value):
                return True
            else:
                return False
        except ValueError, e:
            return False
