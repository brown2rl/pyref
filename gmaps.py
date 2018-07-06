import googlemaps
import csv

gmaps = googlemaps.Client(key='AIzaSyCFJMw1cIgPiF7sNnNTLk7jhOhA0ayECR4')

location='41.8339025,-88.0128431'
types='lawyer'
radius='50000'
ids=[]
places=[]

results=gmaps.places("art",location, radius)

for res in results['results']:
  ids.append(res['place_id'])

for i in ids:
  result=gmaps.place(i)
  res=result['result']
  #print(res)
  place={'name':res['name'],'address':res['formatted_address'],'phone':res['international_phone_number']}
  places.append(place)

ids=[]

f = open('places.txt', 'w')
for place in places:
  f.write(str(place['name'])+' '+str(place['address'])+' '+str(place['phone'])+'\n'+'\n')
f.close()
