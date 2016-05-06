#WardHarvest

##Requirements:
- python
- py-shortners (https://github.com/ellisonleao/pyshorteners) [version 0.6.0+] 
- unicodecsv


##Usage:
You will need a file Sheet1.tsv. Sheet1.tsv is a tsv file, that follows the pattern as outlined in Example.tsv (notes are optional)


conductHarvest.py: This runs all of the files and is generally all that needs to be done to be ready for the harvest.

makeSheets.py: Each row in Sheet1.tsv will become a table in a generted HTML document. Printing the HTML document will create a good document for passing out while conducting a ward harvest.

gpsStamp.py: This creates map.tsv. map.tsv can be inported into mapping software so the assignments can be done geographically.

makeSignup.py: This creates an HTML document so you can keep track of who was assigned to each house.

##Known Bugs/Limitations

- If Google changes its URL structure, gpsStamp.py will not be able to pull GPS locations from the URL and will fail.
- utf-8 support is implimented, but not tested
