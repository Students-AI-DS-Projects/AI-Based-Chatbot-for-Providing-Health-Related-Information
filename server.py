from flask import Flask, render_template, request, jsonify, make_response
from train import chat
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def ind531expage():
	if request.method == "POST":

		print(request.form.get('name'))
		return render_template("index.html")
	return render_template("index.html")

@app.route("/entry", methods=['POST'])
def entry():
	req = request.get_json()
	print(req)
	res = make_response(jsonify({"name":"{}.".format(chat(req)),"message":"OK"}), 200)
	return res


if __name__ == "__main__":
	app.run(debug=True)
