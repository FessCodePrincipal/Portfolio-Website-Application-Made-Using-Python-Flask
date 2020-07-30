from flask import Flask,url_for,render_template,request
from flask_mail import Mail, Message
import os

app=Flask(__name__)
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config.update(mail_settings)
mail = Mail(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def contact():
	name=request.form['name']
	email=request.form['email']
	phone=request.form['phone']
	message=request.form['message']
	with app.app_context():
		msg = Message(subject="Contact from "+name,sender=app.config.get("MAIL_USERNAME"),
		recipients=["festusnjuhigu@gmail.com"],
		body="Hey! My name is " + name + ".\nMy phone number is " + str(phone) + "and my email is "+email+". \nHere is my message:\n" + message)
		mail.send(msg)
		return render_template('index.html')

if __name__ == '__main__':
    app.run()