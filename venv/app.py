from flask import Flask # import class Flask from flask package.import
from routes import initialise_routes

app = Flask (__name__) # create a flask object with name of Module

initialise_routes(app)

#the route ( decorator is used to tell the flash object which
#URL endpoint should trigger our function
#@app.route('/')
#def index ():
#    return "Hello World"

#app.add_url_rule('/', 'index', index)

#def db():
#    return "Hello DB Grads"

#app.add_url_rule('/api/db/', 'db', db) # URL_endpoint, function name as string, function

if __name__ == "__main__":
    app.run(debug=True)