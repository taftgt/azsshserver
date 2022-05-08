from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import cgi
import sys
import json
import subprocess
class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        inputArg1 = form.getvalue("jsonvm")
        print(inputArg1)
        myJSON = json.loads(inputArg1)
        #timerTMUX = "tmux new-session -d 'bash /root/www/timer
.sh'"
        #subprocess.call(["/bin/bash", "-c",timerTMUX])
        ip1 = myJSON[0]['PublicIP']
        print(ip1)
        print('tunnelip1')
        tunIP1 = "tmux new-session -d 'sshpass -p Ferozataftgt8
8 ssh -o StrictHostKeyChecking=no radium@"+ip1+" -R9050:localho
st:5555 -N'"
        print(tunIP1)
        subprocess.call(["/bin/bash", "-c",tunIP1])
        ip2 = myJSON[1]['PublicIP']
        print(ip2)
        print('tunnelip2')
        tunIP2 = "tmux new-session -d 'sshpass -p Ferozataftgt8
8 ssh -o StrictHostKeyChecking=no radium@"+ip2+" -R9050:localho
st:5555 -N'"
        print(tunIP2)
        subprocess.call(["/bin/bash", "-c",tunIP2])
        ip3 = myJSON[2]['PublicIP']
        print(ip3)
        print('tunnelip3')
        tunIP3 = "tmux new-session -d 'sshpass -p Ferozataftgt8
8 ssh -o StrictHostKeyChecking=no radium@"+ip3+" -R9050:localho
st:5555 -N'"
        print(tunIP3)
        subprocess.call(["/bin/bash", "-c",tunIP3])
        myRespon = "<html><body><h1>POST Request " +ip1+ip2+ip3
 + " Received!</h1></body></html>"
        self.wfile.write(bytes(myRespon, "utf-8"))
def run(server_class=HTTPServer, handler_class=MyServer):
    server_address = ('', 17612)
    httpd = server_class(server_address, handler_class)
    print('server running at 17612')
    httpd.serve_forever()
run()
