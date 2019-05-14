from flask import Flask,render_template,request,redirect,url_for,flash,get_flashed_messages
from bson import ObjectId
from pymongo import MongoClient
import os,requests

app = Flask(__name__)
app.secret_key = "secret key"

title = "Find all the Reviews for Your Product"
heading = "AMAZON PRODUCT"
find = "You can see the reviews after few minutes.Thank You"

client = MongoClient('10.56.137.20',27017) #host uri
db = client['Manish'] #Select the database
col = db['amazon'] #Select the collection name
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
	}

def redirect_url():
	return request.args.get('next') or \
		request.referrer or \
		url_for('index')

@app.route("/")
def index():
   return render_template('index.html',h=heading)

@app.route("/list")
def lists ():
	#Display the all Tasks
	pc = col.find()
	return render_template('index.html',t=title,h=heading,f =find)

@app.route("/action", methods=['GET','POST'])
def action():
	pc=request.values.get("name")
	r = requests.get('https://www.amazon.in/dp/product/'+pc+'',headers=headers)
	r = requests.get('https://www.amazon.in/gp/product/'+pc+'',headers=headers)
	print(r.status_code)
	if(r.status_code == 404):
		flash("Invalid ASIN Number")
	else:
	 	for doc in col.find({}):
	 		if(doc['pc'] == pc):
	 			flash("Already Exist")
	 		else:
	 			inser(pc)
			# flash("Insert Succesful")
	return redirect("/")
def inser(pc):
	col.update_one({'pc':pc},{"$set":{'pc':pc}},upsert = True)
	# flash("Insert Succesful")
	return redirect("/list")

if __name__ == "__main__":
	app.run(host = '0.0.0.0',threaded= True)
