from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/dev/metrics', methods = ['POST', 'GET'])
def route():
    if (request.method == 'POST') :
        print("request made")
        print(request.values)
        print(request.get_json())
    else :
        print(request.args)
    return Response("{'a':'b'}", status=200, mimetype='application/json')

@app.route('/', methods = ['POST', 'GET'])
def hello():
    return '''
    <html>
        <head>
            <title>Test</title>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
'''