from approach.config.imports import *

class NumericalColumn(object):

    def __init__(self, name, values, index):
        self.name        = name
        self.values      = values
        self.cleanValues = self.getCleanValues()
        self.minVal      = self.getMinValue()
        self.maxVal      = self.getMaxValue()
        self.median      = self.getMedian()
        self.average     = self.getAverage()
        self.index       = index
        #self.dataType   =

    def getMinValue(self):
        for val in self.cleanValues:
            if 'minVal' in locals():
                if minVal > val:
                    minVal = val
            else:
                minVal = val
        return minVal

    def getMaxValue(self):
        for val in self.cleanValues:
            if 'maxVal' in locals():
                if maxVal < val:
                    maxVal = val
            else:
                maxVal = val
        return maxVal

    def getAverage(self):
        return np.average(self.cleanValues)

    def getMedian(self):
        return np.median(self.cleanValues)

    def getCleanValues(self):
        cleanNumerical = []
        otherValues    = []
        for val in self.values.values:
            if not self.isNan(val):
                if self.isNumber(val):
                    cleanNumerical.append(float(val.replace(',','')))
                else:
                    otherValues.append(val)

        return cleanNumerical


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
