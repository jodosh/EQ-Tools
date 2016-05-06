import unicodecsv as csv
from pyshorteners import Shortener
import urllib
import io

startHTML00 = u"<html>\n<head>\n<meta charset=\"UTF-8\">\n<title>Ward Harvest</title>\n<style type=text/css>\ntable.gridtable {\nfont-family: verdana,arial,sans-serif;\nfont-size:11px;\ncolor:#333333;\nborder-width: 1px;\n"
startHTML01 = u"border-color: #666666;\nborder-collapse: collapse;\nwidth:95%;\nmargin-top:10px;\n}\ntable.gridtable th {\nborder-width: 1px;\npadding: 8px;\nborder-style: solid;\nborder-color: #666666;\n"
startHTML02 = u"background-color: #dedede;\n}\ntable.gridtable td {\nborder-width: 1px;\npadding: 8px;\nborder-style: solid;\nborder-color: #666666;\nbackground-color: #ffffff;\nwidth: 25%;\n}\n"
startHTML03 = u"table.gridtable tr:nth-child(even) {\nfont-weight: bold;\nfont-size:16px;\n}\n</style>\n<style type=\"text/css\">\ntable { page-break-inside:avoid }\ntr    { page-break-inside:avoid; page-break-after:avoid }\n"
startHTML04 = u"</style>\n</head>\n<body>\n"

endHTML = u"</table></body>"

tableStart = u"<table class=gridtable>\n<tr><td>Last Name</td><td>First Name(s)</td><td>Address</td><td>Phone Number</td></tr>\n"


f = io.open('sheets.html', mode='w', encoding='utf-8')

f.write(startHTML00)
f.write(startHTML01)
f.write(startHTML02)
f.write(startHTML03)
f.write(startHTML04)


with open('Sheet1.tsv', 'rb') as csvFile:
        reader = csv.reader(csvFile, delimiter='\t')
        for idx,row in enumerate(reader):
        
                try:
                    assign = row[6]  #assignedTo
                except IndexError:
                    assign = 'null'


		url = row[5]
		print(url)
		shortener = Shortener('Tinyurl', timeout=9000)
		shortURL = shortener.short(url)

		URL = shortener.qrcode().replace("120x120","220x220")
		
		FILENAME = str(idx)
		FILENAME += ".png"

		urllib.urlretrieve(URL, filename=FILENAME)
	
		
		tableMiddle = u"<tr><td>"
		tableMiddle += row[0] #Last Name
		tableMiddle += u"</td><td>"
		tableMiddle += row[1] #First Name
		tableMiddle += u"</td><td>"
		tableMiddle += row[2] #Address
		tableMiddle += u"</td><td>"
		tableMiddle += row[3] #Phone
		tableMiddle += u"</td></tr>\n<tr><td>"
		tableMiddle += shortURL #Should Be Short URL
		tableMiddle += u"</td><td><img src=\""
		tableMiddle += FILENAME # Should Be QR Filename
		tableMiddle += u"\" /></td>\n"
		tableEnd = u"<td colspan=2 valign=top><input type=\"checkbox\"> Made Contact<br>\n<input type=\"checkbox\"> Interested in Contact<br>\n<input type=\"checkbox\"> Moved?<br>\n"
		tableEnd += row[4] #Notes
		tableEnd += u"</td></tr><tr> <td colspan=\"4\" valign=\"top\">Assigned to:"
		tableEnd += assign
		tableEnd += u"</td></tr></table>\n"
		
		f.write(tableStart)
		f.write(tableMiddle)
		f.write(tableEnd)
		
		

		

f.write(endHTML)




csvFile.close()
f.close() # you can omit in most cases as the destructor will call it
