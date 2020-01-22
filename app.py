import os
from http.server import HTTPServer, BaseHTTPRequestHandler #Built into the python HTTP library, handles the HTTP requests


class Serv(BaseHTTPRequestHandler):                     #Declare class that handles the serving of the content

    def do_GET(self):
        if self.path == '/':                            #Check path, if it's /, index page
            self.path = '/app.html'
        try:
            file_to_open = open(self.path[1:]).read()   #Try to open app.html
            self.send_response(200)                     #reply success code
        except:
            file_to_open = "File not found"             #Error opening file
            self.send_response(404)                     #reply file not found code
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))  #Write contents of file to screen (utf-8 encoding)


httpd = HTTPServer((int(os.environ.get("PORT", 5000))), Serv)
httpd.serve_forever()
