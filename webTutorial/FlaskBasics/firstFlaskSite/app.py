from flask import Flask,redirect,url_for,request,render_template,make_response

app = Flask(__name__)

#example to use html template
@app.route('/')
def hello_template():
	#Templates needs to be in templates(exact name) folder
	return render_template('template_example.html')

#example to use html template with passing data to template
@app.route('/new/<username>')
def new(username):
	return render_template('template_example.html',name = username)

#example to open url
@app.route('/demo')
def demo():
	return 'demo page'

#example to open url with data
@app.route('/profile/<name>')
def profileName(name):
	return 'this profile is %s' % name +'\'s got it'

#example to open url with int data type
@app.route('/profile/<int:id>')
def profileId(id):
	return 'this profile identity is %d' % id

#example to open url with float data type
@app.route('/balance/<float:bal>')
def balanceAmount(bal):
	return 'this accounts bal is %f' % bal

#example to switch url based on input
@app.route('/admin')
def hello_admin():
	return 'hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'hello guest %s' % guest

@app.route('/user/<name>')
def hello_user(name):
	if name=='admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest',guest=name))

#example to use login.html to show dynamic welcome page
@app.route('/sucess/<name>')
def success(name):	
	return 'Welcome %s' %name

@app.route('/login',methods=['POST','GET'])
def login():
	if(request.method == 'POST'):
		userName = request.form['nm']
		return redirect(url_for('success',name=userName))
	else:
		userName = request.args.get('nm')
		return redirect(url_for('success',name=userName))

#example to use javascript
@app.route('/sayHi')
def hello_js():
	#Templates needs to be in templates(exact name) folder
	return render_template('hello.html')

#example to use from to collect data and display it on seprate page
@app.route('/student')
def student_details():
	#Templates needs to be in templates(exact name) folder
	return render_template('student.html')

@app.route('/result',methods=['POST','GET'])
def student_result():
	if(request.method == 'POST'):
		result = request.form
		return render_template('result.html',result = result)

#example to use cookies
@app.route('/cookie')
def cookie_demo():
	return render_template('index.html')

@app.route('/setcookie',methods=['POST','GET'])
def cookie_set():
	if(request.method == 'POST'):
		userNm = request.form["nm"]
	
	resp = make_response(render_template('readcookie.html'))
	resp.set_cookie('userName',userNm)

	return resp

@app.route('/getcookie')
def cookie_get():
	name = request.cookies.get('userName')
	return '<h1> Hello'+name+'</h1>'

if(__name__== '__main__'):
	app.run()

