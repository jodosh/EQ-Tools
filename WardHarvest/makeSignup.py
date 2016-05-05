import csv

startHTML00 = "<html>\n<head>\n<meta charset=\"UTF-8\">\n<title>Ward Harvest Signup</title>\n<style type=text/css>\ntable.gridtable {\nfont-family: verdana,arial,sans-serif;\nfont-size:16px;\ncolor:#333333;\nborder-width: 1px;\n"
startHTML01 = "border-color: #666666;\nborder-collapse: collapse;\nwidth:95%;\nmargin-top:10px;\n}\ntable.gridtable th {\nborder-width: 1px;\npadding: 8px;\nborder-style: solid;\nborder-color: #666666;\n"
startHTML02 = "\n}\ntable.gridtable td {\nborder-width: 1px;\npadding: 8px;\nborder-style: solid;\nborder-color: #666666;\n\nwidth: 50%;\n}\n"
startHTML03 = "table.gridtable tr:nth-child(even) {\nfont-size:16px;\nbackground-color:#CCC;\n}\n</style>\n<style type=\"text/css\">\ntable { page-break-inside:avoid }\ntr    { page-break-inside:avoid; page-break-after:avoid }\n"
startHTML04 = "</style>\n</head>\n<body>\n"

endHTML = "</table></body>"

tableStart = "<table class=gridtable>\n<tr><td>Assignment</td><td>Assigned To</td></tr>\n"
tableMiddle = ""


f = open('signup.html', 'w')

f.write(startHTML00)
f.write(startHTML01)
f.write(startHTML02)
f.write(startHTML03)
f.write(startHTML04)


with open('Sheet1.tsv', 'rb') as csvFile:
    reader = csv.reader(csvFile, delimiter='\t')
    for row in reader:


		
		
		tableMiddle += "<tr><td>"
		tableMiddle += row[0] + "," + row[1] 
		tableMiddle += "</td><td>"
		tableMiddle += "&nbsp;"
		tableMiddle += "</td></tr>\n"
		
f.write(tableStart)
f.write(tableMiddle)
f.write("</table>")
		
		

		

f.write(endHTML)




csvFile.close()
f.close() # you can omit in most cases as the destructor will call it
