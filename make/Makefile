.PHONY: clean all

crime.zip:
	curl -o crime.zip 'https://www2.census.gov/library/publications/2011/compendia/usa-counties/zip/CRM.zip'

unziped.shp: crime.zip
	unzip crime.zip
	touch unziped.shp

unzip: unziped.shp

clean:
	rm - 