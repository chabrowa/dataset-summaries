from approach.Dataset import Dataset

from approach.config.paths import *
from approach.config.imports import *

d = Dataset(path)

#print d.name
#print "Rows: " + str(d.noRows)
#print "Column: " + str(d.noColumns)
#print "Headers are: "
#print d.printHeaders()


for column in d.columns:
    #print column.name
    print column.type
