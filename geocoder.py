#coding:UTF-8
import re
import json
from SPARQLWrapper import SPARQLWrapper,JSON

geo = dict()
sparql = SPARQLWrapper("http://ja.dbpedia.org/sparql")
sparql.setQuery('''
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
PREFIX dbp-ja: <http://ja.dbpedia.org/resource/>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT distinct ?name, ?lat, ?lon WHERE {
  ?s rdfs:label ?name;
  geo:lat ?lat ;
  geo:long ?lon .
  { ?s dbpedia-owl:servingRailwayLine dbp-ja:神戸市営地下鉄西神・山手線 .}
   union
  { ?s dbpedia-owl:servingRailwayLine dbp-ja:神戸市営地下鉄海岸線 .}
}
''')
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
	m = re.match(r"^(?P<name>.*?)駅?( \(.*\))?$", result["name"]["value"])
	name = m.groupdict()["name"]
	geo[name] = dict([(k, v["value"]) for k,v in result.items()])

# fill temporary unavaliable values
with open("dbpedia/subway_helper.json") as fp:
	geo.update(json.load(fp))

with open("dbpedia/subway.json", "w", encoding="UTF-8") as fp:
	json.dump(geo, fp, indent=2, ensure_ascii=False)
