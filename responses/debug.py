from main import app


@app.response("test")
def hello_world():
    print "Hello World!"
