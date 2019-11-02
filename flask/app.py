from flask import Flask,render_template,request,redirect
from pypg import helper
import json

app = Flask(__name__)

@app.route('/')
def index():
		#tables =  helper.read_tables()
		#print(type(tables),tables)
		#print(type(tables[0]),tables[0])
		#print(type(tables[0][0]),tables[0][0])
		result = helper.students_list() #result of SELECT is list
		
		#return render_template("index.html", table=tables[0][0])
		return render_template("index.html", students=result)


@app.route("/register",methods=["POST"])
def register():
		sid = request.form.get("id")
		name = request.form.get('name')
		email = request.form.get("email")

		print(f"{name}이 {email}로 가입함, {sid}")
		helper.insert("student",sid,name,email)
		
		return redirect("/")#다시 원래페이지로 redirect

@app.route("/register-rest", methods=["POST"])
def register_rest():
		sid = request.form.get("id")
		name = request.form.get('name')
		email = request.form.get("email")

		print(f"{name}이 {email}로 가입함, {sid}")
		helper.insert("student",sid,name,email)
		
		return "OK"


@app.route("/list")
def student_list():
	# TODO : GET student data from 'student' table
	result = helper.students_list() #result of SELECT is list
	return render_template("list.html",students=result)

@app.route("/list-rest")
def student_list_rest():
	# TODO : GET student data from 'student' table
	result = helper.students_list() #result of SELECT is list
	#pprint(result)#table만 
	result = json.dumps(result)#dump로 해서 string으로 변한다.
	return result


if __name__ == ("__main__"):
  # docker
  #app.run(debug=True, host='0.0.0.0', port=5090)
  # other
  app.run(debug=True)
