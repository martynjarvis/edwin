from edwin import EDWIN

app = EDWIN()

@app.response("test")
def hello_world():
    print "Hello World!"

app.run()
