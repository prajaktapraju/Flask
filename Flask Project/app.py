from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:praju123@localhost:5432/result"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Result(db.Model):
    __tablename__ = 'result'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(25))
    email= db.Column(db.String(50))
   
def __init__(self, name, email, password):
            self.name = name
            self.email= email
          

def __repr__(self):
        return f"<result {self.name}>"

  
@app.route('/')
def hello():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)