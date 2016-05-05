import csv
from pyshorteners import Shortener
import urllib

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end-3]
    except ValueError:
        return ""

with open('map.tsv', 'w') as tsvFile:
    spamwriter = csv.writer(tsvFile, delimiter='\t')
    spamwriter.writerow(['Name','Lat','Long'])



    with open('Sheet1.tsv', 'rb') as csvFile:
        reader = csv.reader(csvFile, delimiter='\t')
        for row in reader:
        
            s = row[5]
        
            latLong = find_between(s,"@","/data").split(",")
        
               
            spamwriter.writerow([row[0],latLong[0],latLong[1]])






csvFile.close()
tsvFile.close() # you can omit in most cases as the destructor will call it
