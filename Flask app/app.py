#step 1 import flask
from flask import Flask, send_file
import base64

#step 2: instantiate Flask class

app = Flask(__name__) #__name__ means it is going to take the name of the file so that execute the app, the file will be named whatever you name it

#step 4: setting up your routes (logic of your app)
# '@' -> called a decorator - modifies/adds to your functions
@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/inventory')
def inventory():
    return 'This is the inventory'

@app.route('/animal/<pet>') #dynamic url
def which_pet(pet): 
    if pet == 'cat':
        return 'Meow'
    elif pet == 'dog':
        return 'Woof'
    
#Send an image
@app.route('/image/<id>')
def serve_img(id):
    #going to try something when going to the link, and if it doesn't work, i will return you an error "404"
    try:
        img_path = f'{id}.png'
        return send_file(img_path, mimetype="image/png")
    except FileNotFoundError:
        return("", 404)

#send a file with other JSON payloads
@app.route('/image/other/<page>')
def image_others(page):
    try:
        img_path = f'{page}.png'
        with open(img_path, 'rb') as img: #serving out images as byte instead of picture, need encoding (translation)
            file_encoded = base64.b64encode(img.read())
        response = {
            'byte' : str(file_encoded),
            'metadata' : "This is just metadata"
        }
        return(response, 200)
    except FileNotFoundError:
        return('', 404)


#Step 3 : At the end of the code - running the app
if __name__ == "__main__":
    app.run()

