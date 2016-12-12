import requests
import json
import sys

count = 0
term = ""
query_length = len(sys.argv)

if query_length > 1:
	for x in range(1,query_length):
		term = term + " " + sys.argv[x]

	term = term.strip()

	url = "http://api.duckduckgo.com/?q=" + term + "&format=json&pretty=1"

	r = requests.get(url)
	data = r.content

	json_data = json.loads(str(data))

	count = len(json_data["RelatedTopics"])

	if count == 0:
		print "No meaning found for this term."
	elif count == 1:
		print json_data["RelatedTopics"][0]["Text"]
	else:
		count = 3 if count >= 3 else count
		print "The term %s may refer to " %term
		for x in xrange(0,count):
			print str(x+1) + " : " + json_data["RelatedTopics"][x]["Text"]
else:
	print "Please enter a term to search for its meaning."