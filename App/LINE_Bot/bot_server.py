#! python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   keyfile="ssl/server-key.pem",
                                   certfile="ssl/server-cert.pem",
                                   server_side=True,
                                   ca_certs="ssl/client-cert.pem",
                                   cert_reqs=ssl.CERT_REQUIRED)
    print("Serving on port 4443")
    httpd.serve_forever()
