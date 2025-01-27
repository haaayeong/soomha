from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

 # mysql 연결
  app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:1234@localhost:3306/soomha',
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SQLALCHEMY_EHCO=True
  )

  # 플라스크와 sql알케미 연결
  db.init_app(app)
  Migrate(app, db)
  
  @app.route('/')
  def test():
    return '테스트 성공'
  
  return test