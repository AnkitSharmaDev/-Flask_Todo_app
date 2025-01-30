from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
 
db=SQLAlchemy(app)

# create database
class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self) -> str: #method
        return f"{self.sno} - {self.title}"

@app.route("/") 
def hello_world():
    todo=Todo(title="First Todo",desc="Start investing in the world")
    db.session.add(todo)
    db.session.commit()
    alltodo=Todo.query.all()
    print(alltodo)
    return render_template('index.html',alltodo=alltodo) #to use ninjatempleate
    # return "<p>Hello, World!</p>"



@app.route("/show")
def products():
    return "<p>Products Page</p>"
 


if __name__=="__main__":
    app.run(debug=True)