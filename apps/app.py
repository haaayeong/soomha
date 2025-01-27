from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

  app.config.from_mapping(
    # mysql 연결
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:1234@localhost:3306/soomha',

    # SQLAlchemy가 변경 사항 추적하지 않도록 함.
    SQLALCHEMY_TRACK_MODIFICATIONS = False,

    # SQLAlchemy가 실행하는 SQL 쿼리를 콘솔에 출력하게 함.
    SQLALCHEMY_EHCO=True
  )

  # 플라스크와 sql알케미 연결
  db.init_app(app)
  Migrate(app, db)
  
  @app.route('/')
  def test():
    return '테스트 성공'
  
  return app