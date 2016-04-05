#!/usr/bin/env python
from __future__ import print_function

import cgi
from subprocess import Popen, PIPE
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)
        elif ctype == 'text/xml':
            length = int(self.headers.getheader('content-length'))
            postvars = urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        baseurl = postvars.get('url')
        suite = postvars.get('suite')
        xml = postvars.get('data')

        if not baseurl:
            self.wfile.write('you need to specify url!  e.g.  url=http://example.com')
            return
        else:
            baseurl = baseurl[0]

        if not suite:
            self.wfile.write('you need to specify a suite!  e.g.  suite=TestSuite')
            return
        else:
            suite = suite[0]

        if not xml:
            self.wfile.write('you need to specify the xml project!  e.g. curl --data-urlencode @/path/to.xml')
            return
        else:
            xml = xml[0]

        f = open('/tmp/soapui-project.xml', 'w')
        print(xml, file=f)
        f.close()
        p = Popen(['/opt/SoapUI/bin/testrunner.sh',
                   '-s"%s %s"' % (baseurl, suite),
                   '/tmp/soapui-project.xml'], stdin=PIPE, stdout=PIPE, stderr=PIPE, bufsize=-1)
        try:
            output, error = p.communicate()
            self.wfile.write(output)
            self.wfile.write(error)
        except Exception as e:
            self.wfile.write(e)


def run(server_class=HTTPServer, handler_class=S, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
