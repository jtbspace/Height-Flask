from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
app=Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgress123@localhost/Height_Weight'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://bdxnnnatrcygpy:05d807990e4e7d399d280817c8916e6d3b8727575915717e6d0e9f905359b394@ec2-18-233-137-77.compute-1.amazonaws.com:5432/d575mgp6dn2csj?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)
    weight_= db.Column(db.Integer)

    def __init__(self,email_,height_,weight_):
        self.email_=email_
        self.height_=height_
        self.weight_=weight_
    

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        weight=request.form["weight_name"]

        if db.session.query(Data).filter(Data.email_ == email).count()== 0:
            data=Data(email,height,weight)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            average_weight=db.session.query(func.avg(Data.weight_)).scalar()
            average_weight=round(average_weight,1)
            # print(average_height,average_weight)
            count= db.session.query(Data.height_).count()
            send_email(email, height,weight,average_height,average_weight,count)

            return render_template("success.html")
    return render_template('index.html',text="Looks like we've got something similar from this email!")
        
if __name__=="__main__":
    app.debug=True
    app.run()