import httplib, urllib, json

def semua():
	conn = httplib.HTTPConnection('192.168.10.1:7777')
	conn.request("GET", "/node")
	response = conn.getresponse()
	resp = json.loads(response.read())
	print "id\t", "temp\t", "hum\t", "smoke\t", "carbon\t", "timestamp\t"
	print "-----\t", "-----\t", "-----\t", "-----\t", "-----\t", "-----\t"
	for id in resp :
		print id["id"], "\t", id["temp"], "\t", id["hum"], "\t", id["smoke"], "\t", id["carbon"], "\t", id["timestamp"]

def satu(node_id):
	conn = httplib.HTTPConnection('192.168.10.1:7777')
	conn.request("GET", "/node/"+str(node_id))
	response = conn.getresponse()
	if response.status == 200 :
		id = json.loads(response.read())
		print "id\t", "temp\t", "hum\t", "smoke\t", "carbon\t", "timestamp\t"
		print "-----\t", "-----\t", "-----\t", "-----\t", "-----\t", "-----\t"
		print id["id"], "\t", id["temp"], "\t", id["hum"], "\t", id["smoke"], "\t", id["carbon"], "\t", id["timestamp"]
	elif response.status == 404 :
		print "Node tidak ditemukan"
	else :
		print "Error"

semua()
print "\n"
satu(1)
print "\n"
satu(10)
print "\n"
satu(20)
print "\n"
