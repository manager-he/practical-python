import urllib.request
# BUSAPI: SPXkfKLjvAwkYfFxiMBMy3sxH
# https://www.ctabustracker.com/dev-account
u = urllib.request.urlopen('http://www.ctabustracker.com/bustime/api/v2/getpredictions?key=SPXkfKLjvAwkYfFxiMBMy3sxH&rt=22&stpid=14791')

from xml.etree.ElementTree import parse
doc = parse(u)

for pt in doc.findall('.//pt'):
    print(pt.text)
    
    
# Sears tower

bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while bill_thickness * num_bills < sears_height:
    print(day, num_bills, bill_thickness*num_bills)
    day += 1
    num_bills *= 2
    
