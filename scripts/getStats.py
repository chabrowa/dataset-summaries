from approach.Dataset import Dataset
from approach.Statistics import Statistics

from approach.config.paths import *
from approach.config.imports import *

d = Dataset(path)
stats = Statistics(d)

stats.printDatasetStatsTabular()
stats.printNumericalStatsTabular()
stats.printHeadersStats()
stats.printSubjectColumn()
