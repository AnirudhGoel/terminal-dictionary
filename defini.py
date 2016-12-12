import requests
import json

count = 0
term = raw_input("Enter the term to get it's meaning : ")

url = "http://api.duckduckgo.com/?q=" + term + "&format=json&pretty=1"

r = requests.get(url)
data = r.content

json_data = json.loads(str(data))

count = len(json_data["RelatedTopics"])

if count == 0:
	print "No meaning found for this word."
elif count == 1:
	print json_data["RelatedTopics"][0]["Text"]
else:
	count = 3 if count >= 3 else count
	print "The word %s may refer to " %term
	for x in xrange(0,count):
		print str(x+1) + " : " + json_data["RelatedTopics"][x]["Text"]