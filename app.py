'''

new api key 42iq1nn6wamvl9jp5yyc6lwa
new secret  asezyq0dxr 

'''

from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import requests

app = Flask(__name__)
app.secret_key = "secret key"
app.config["MONGO_URI"] = "mongodb://localhost:27017/movies"
mongo = PyMongo(app)

@app.route('/Item', methods=['POST'])
def item():
    apikey = '42iq1nn6wamvl9jp5yyc6lwa'
    item_search = request.form['item_search']
    r = requests.get('https://openapi.etsy.com/v2/listings/active?api_key='+apikey+'&s='+item_search)
    json_object = r.json()

    items = json_object['Search']

    for item in items:
        title = item['Title']
        state = item['State']
        image = item['Image']
        listing_id = item['Listing_id']

    #return json_object
    #return str(items)
    return render_template('item.html', item=item)

@app.route('/info', defaults={'id': '559139843'})
@app.route('/info/<id>', methods=['POST','GET'])
def info(id):
    apikey = '42iq1nn6wamvl9jp5yyc6lwa'
    item_search = id
    r = requests.get('https://openapi.etsy.com/v2/listings/active?api_key='+apikey+'&i='+item_search)
    json_object = r.json()

    title = json_object['Title']
    description = json_object['Description']
    image = json_object['Image']
    Price = json_object['Price']

    #return json_object
    return render_template('info.html', id=id, image=image, title=tile, description=description, price=price)


'''

#to be used when basket system is added 

@app.route('/delete/<id>', methods=['POST'])
def delete_movie(id):
    mongo.db.Items.delete_one({'_id': id})
    resp = 'Movie removed successfully!'
    return resp

@app.route('/Watched/<id>', methods=['POST'])
def Watched_movie(id):
    mongo.db.Items.update({'_id': id},{'$set':{'watched': 'true'}})
    resp = 'Movie set to watched successfully!'
    return userFavs

@app.route('/unwatch/<id>', methods=['POST'])
def unwatch_movie(id):
    mongo.db.Items.update({'_id':id},{'$set':{'watched': 'false'}})
    return userFavs()

@app.route('/userFavs')
def userFavs():
    favMovies = mongo.db.Items.find()
    return render_template('Items.html', favMovies=favMovies)

'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/infosearch')
def infosearch():
	return render_template('info-search.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')



