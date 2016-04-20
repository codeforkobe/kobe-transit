all: kobe_subway_gtfs.zip

kobe_subway_gtfs.zip: opendata dbpedia/geocoder.json
	mkdir -p kobe_subway_gtfs
	python3 subway_gtfs.py

dbpedia/geocoder.json:
	python3 geocoder.py

opendata:
	wget -N -P kobe_opendata -i opendata_url.txt
