all: kobe_subway_gtfs.zip

kobe_subway_gtfs.zip: opendata dbpedia/subway.json
	mkdir -p kobe_subway_gtfs
	python3 subway_gtfs.py

dbpedia/subway.json:
	python3 geocoder.py

opendata:
	wget -N -P kobe_opendata -i opendata_url.txt

clean:
	-rm kobe_subway_gtfs.zip dbpedia/subway.json
	-rm -rf kobe_subway_gtfs transitfeed

test: kobe_subway_gtfs.zip
	git clone https://github.com/google/transitfeed
	PYTHONPATH=transitfeed python ./transitfeed/feedvalidator.py --extension=extensions.googletransit -o CONSOLE kobe_subway_gtfs.zip
