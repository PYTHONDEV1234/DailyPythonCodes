from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import jokes

def set_headers(handler, status=200, content_type="application/json"):
    handler.send_response(status)
    handler.send_header("Content-type", content_type)
    handler.end_headers()

def handle_get(request, parsed_path):
    if parsed_path.path == '/jokes':
        query = parse_qs(parsed_path.query)
        joke_id = query.get('id', [None])[0]
        if joke_id:
            joke_id = int(joke_id)
            joke = jokes.find_joke(joke_id)
            if joke:
                set_headers(request)
                request.wfile.write(json.dumps(joke).encode())
            else:
                set_headers(request, 404)
                request.wfile.write(json.dumps({"error": "Joke not found"}).encode())
        else:
            jokes_list = jokes.get_all_jokes()
            set_headers(request)
            request.wfile.write(json.dumps(jokes_list).encode())
    else:
        set_headers(request, 404)
        request.wfile.write(json.dumps({"error": "Not found"}).encode())

def handle_post(request):
    if request.path == '/jokes':
        content_length = int(request.headers['Content-Length'])
        post_data = request.rfile.read(content_length)
        new_joke = json.loads(post_data)
        added_joke = jokes.add_joke(new_joke)
        set_headers(request, 201)
        request.wfile.write(json.dumps(added_joke).encode())
    else:
        set_headers(request, 404)
        request.wfile.write(json.dumps({"error": "Not found"}).encode())

# def handle_put(request, parsed_path):
#     if parsed_path.path.startswith('/jokes/'):
#         try:
#             joke_id = int(parsed_path.path.split('/')[-1])
#             content_length = int(request.headers['Content-Length'])
#             put_data = request.rfile.read(content_length)
#             joke_data = json.loads(put_data)
#             updated_joke = jokes.update_joke(joke_id, joke_data)
#             if updated_joke:
#                 set_headers(request)
#                 request.wfile.write(json.dumps(updated_joke).encode())
#             else:
#                 set_headers(request, 404)
#                 request.wfile.write(json.dumps({"error": "Joke not found"}).encode())
#         except ValueError:
#             set_headers(request, 400)
#             request.wfile.write(json.dumps({"error": "Invalid joke ID"}).encode())
#     else:
#         set_headers(request, 404)
#         request.wfile.write(json.dumps({"error": "Not found"}).encode())

def handle_delete(request, parsed_path):
    if parsed_path.path.startswith('/jokes/'):
        try:
            joke_id = int(parsed_path.path.split('/')[-1])
            deleted_joke = jokes.delete_joke(joke_id)
            if deleted_joke:
                set_headers(request)
                request.wfile.write(json.dumps({"message": "Joke deleted"}).encode())
            else:
                set_headers(request, 404)
                request.wfile.write(json.dumps({"error": "Joke not found"}).encode())
        except ValueError:
            set_headers(request, 400)
            request.wfile.write(json.dumps({"error": "Invalid joke ID"}).encode())
    else:
        set_headers(request, 404)
        request.wfile.write(json.dumps({"error": "Not found"}).encode())

def handle_request(request):
    parsed_path = urlparse(request.path)
    if request.command == 'GET':
        handle_get(request, parsed_path)
    elif request.command == 'POST':
        handle_post(request)
    # elif request.command == 'PUT':
    #     handle_put(request, parsed_path)
    elif request.command == 'DELETE':
        handle_delete(request, parsed_path)
    else:
        set_headers(request, 405)
        request.wfile.write(json.dumps({"error": "Method not allowed"}).encode())

def run(server_class=HTTPServer, port=8500):
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            handle_request(self)

        def do_POST(self):
            handle_request(self)

        def do_PUT(self):
            handle_request(self)

        def do_DELETE(self):
            handle_request(self)

    server_address = ('', port)
    httpd = server_class(server_address, RequestHandler)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()


# curl -X GET http://localhost:8500/jokes
# curl -X GET 'http://localhost:8500/jokes?id=1'
# curl -X POST http://localhost:8500/jokes -H 'Content-Type: application/json' -d '{"joke": "Why don'\''t skeletons fight each other? They don'\''t have the guts."}'
# curl -X DELETE http://localhost:8500/jokes/1




# 5XX - Server Side problem
# 4XX - Client Side errors 
# 3XX - Redirection 
# 2XX - Success 