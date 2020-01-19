from flask import Flask, render_template, url_for, request, send_file
from write_url import write_url

app = Flask(__name__)

f = open('unique_count.txt', 'r')
unique_count = int(f.read())
f.close()

@app.route('/', methods=['POST', 'GET'])
def index():
	global unique_count
	if request.method == 'POST':
		countup = True
		new_url = request.form['url']
		countup = write_url(new_url)
		if countup:
			unique_count += 1
			f = open('unique_count.txt', 'w')
			f.write(str(unique_count))
			f.close()
	return render_template('index.html', unique_count = unique_count)

@app.route('/geturls')
def urlfile():
	return send_file('urls.txt')