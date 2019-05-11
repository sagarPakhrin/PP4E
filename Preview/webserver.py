import os,sys

from http.server import HTTPServer, CGIHTTPRequestHandler
webdir = "."
port = 80
os.chdir(webdir)
srvaddr = ("",port)
srvrobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
