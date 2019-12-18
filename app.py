'''
new api key 42iq1nn6wamvl9jp5yyc6lwa
new secret  asezyq0dxr 


summary so far;
items on display - good
searchbar not specific -
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

    items = json_object['results']

    for item in items:
        title = item['title']
        state = item['state']
        description = item['description']
        price = item['price']
    return render_template('Item.html', items=items )



@app.route('/info', defaults={'id': ''})
@app.route('/info/<id>', methods=['POST','GET'])
def info(id):
    apikey = '42iq1nn6wamvl9jp5yyc6lwa'
    item_search = id
    r = requests.get('https://openapi.etsy.com/v2/listings/active?api_key='+apikey+'&i='+item_search)
    json_object = r.json()

    info = json_object['results']

    for item in info:
        title = item['title']
        state = item['state']
        listing_item = item['listing_id']



    #return json_object
    return render_template('info.html', item=item)

####
#to be used when basket system is added 

#wip 
#######################################################

@app.route('/basket/<id>', methods=['POST'])
def delete_item(id):
    mongo.db.Items.delete_one({'_id': id})
    resp = 'Item removed from basket!'
    return resp

@app.route('/basket/<id>', methods=['POST'])
def add_item(id):
    mongo.db.Items.update({'_id': id},{'$set':{'added': 'true'}})
    resp = 'Item added to basket'
    return userFavs

############################################################


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/infosearch')
def infosearch():
	return render_template('info-search.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')