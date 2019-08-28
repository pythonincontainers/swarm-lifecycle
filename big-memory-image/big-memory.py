from flask import Flask
import numpy


app = Flask(__name__)

size = 100*1024*1024

a = numpy.arange(1, size, dtype=int)

@app.route('/')
def big_mem():
    global a
    message = '<h1>Here is Big Memory v1</h1>\n'
    message += '<h2>Current memory usage: '+str(a.nbytes/(1024*1024))+' MB</h2>'
    message += '<h2> Array element with index '+str(size-2)+' is '+str(a.item(size-2))+'</h2>'
    return message

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
