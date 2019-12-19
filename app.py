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
	r = requests.get('https://openapi.etsy.com/v2/listings/active?api_key='+apikey+'&q='+item_search)
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
	r = requests.get('https://openapi.etsy.com/v2/listings/active?api_key='+apikey+'&q='+item_search)
	json_object = r.json()


	
	for i in range(50):
		if json_object['results'][i]['listing_id'] == item_search:
			return json_object['results'][i][listing_id]
			info = json_object['results']
	
	'''
	#return str(info) 
	#if item_search in info[i]['listing_id']:
	title = info['title']
	state = info['state']
	listing_id = info['listing_id']
	#return json_object
	return render_template('info.html', title=title, state=state,listing_id=listing_id)
	'''




#to be used when basket system is added 
#wip 
#######################################################
'''
@app.route('/basket/<id>', methods=['POST'])
def delete_item(id):
	mongo.db.Items.delete_one({'_id': id})
	resp = 'Item removed from basket!'
	return resp
'''


@app.route('/basket/<id>', methods=['POST'])
def add_item(id):
	mongo.db.Items.update({'_id': id},{'$set':{'added': 'true'}})
	resp = 'Item added to basket'
	return userFavs

############################################################



@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, port=5000, host='127.0.0.1')
