from approach.config.imports import *

class TextualColumn(object):

    def __init__(self, name, values, index):
        self.name     = name
        self.values   = values
        self.index    = index
        self.entities = self.getEntities()


    def getEntities(self):
        for val in self.values:
            pass
            #print "----"
            #print val
            #self.getValueTypes(val)

    def getValueTypes(self, value):
        response = commands.getstatusoutput('curl http://model.dbpedia-spotlight.org/en/annotate  \
          --data-urlencode "text=' + str(value) + '" \
          --data "confidence=0.05" \
          -H "Accept: application/json"')

        #print response
        return response

#curl http://model.dbpedia-spotlight.org/en/annotate  \
#          --data-urlencode "text= London" \
#          --data "confidence=0.05" \
#          -H "Accept: application/json"
#{"@text":" London","@confidence":"0.05","@support":"0","@types":"","@sparql":"","@policy":"whitelist","Resources":[{"@URI":"http://dbpedia.org/resource/London","@support":"158140","@types":"Schema:Place,DBpedia:Place,DBpedia:PopulatedPlace,DBpedia:Settlement,Schema:City,DBpedia:City","@surfaceForm":"London","@offset":"1","@similarityScore":"0.9994158799798495","@percentageOfSecondRank":"1.8932490094221479E-4"}]}%



#curl http://model.dbpedia-spotlight.org/en/annotate  \
#          --data-urlencode "text= London Paris Warsaw Berlin" \
#          --data "confidence=0.05" \
#          -H "Accept: application/json"
#{"@text":" London Paris Warsaw Berlin","@confidence":"0.05","@support":"0","@types":"","@sparql":"","@policy":"whitelist","Resources":[
#{"@URI":"http://dbpedia.org/resource/London","@support":"158140","@types":"Schema:Place,DBpedia:Place,DBpedia:PopulatedPlace,DBpedia:Settlement,Schema:City,DBpedia:City","@surfaceForm":"London","@offset":"1","@similarityScore":"0.9998290434181605","@percentageOfSecondRank":"4.9449711720715715E-5"},
#{"@URI":"http://dbpedia.org/resource/Paris","@support":"75243","@types":"Schema:Place,DBpedia:Place,DBpedia:PopulatedPlace,DBpedia:Settlement","@surfaceForm":"Paris","@offset":"8","@similarityScore":"0.9998857975883089","@percentageOfSecondRank":"9.955121707960375E-5"},
#{"@URI":"http://dbpedia.org/resource/Warsaw","@support":"24328","@types":"Schema:Place,DBpedia:Place,DBpedia:PopulatedPlace,DBpedia:Settlement","@surfaceForm":"Warsaw","@offset":"14","@similarityScore":"0.9997845593129328","@percentageOfSecondRank":"8.375981261832549E-5"},
#{"@URI":"http://dbpedia.org/resource/Berlin","@support":"46739","@types":"Schema:Place,DBpedia:Place,DBpedia:PopulatedPlace,DBpedia:Region,Schema:AdministrativeArea,DBpedia:AdministrativeRegion","@surfaceForm":"Berlin","@offset":"21","@similarityScore":"0.9988508756148783","@percentageOfSecondRank":"0.0010975783094931807"}]}%
