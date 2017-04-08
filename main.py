from flask import Flask, abort
from socket import *
import ast, json, pprint, sys
from thread import start_new_thread

coreData = []
serverPort = 8989
MAX = 65535
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"

def udpserver():
    try:
        while 1:
            message, clientAddress = serverSocket.recvfrom(MAX)
            print "Client Connected : " + str(clientAddress) + " \nsays : " + message
            print "-----------------------------------------------------------------------"
            serverSocket.sendto("200 OK", clientAddress)
            data = ast.literal_eval(message)
            coreData.append(data)
            pp = pprint.PrettyPrinter(indent=1)
            pp.pprint(coreData)
            print "\n"

    except KeyboardInterrupt:
        print('\n\nOPERATION HAS BEEN CANCELED!\n')
        sys.exit()

app = Flask(__name__)

@app.route('/node', methods=['GET'])
def semua():
    return json.dumps(coreData)

@app.route('/node/<int:node_id>', methods=['GET'])
def satu(node_id):
    node = None
    for n in coreData :
        if n["id"] == node_id :
            node = n
    if node :
        return json.dumps(node)
    else :
        abort(404)

if __name__=='__main__':
    start_new_thread(udpserver ,())
    app.run(debug=True, use_reloader=False, host="192.168.10.1", port=7777)
