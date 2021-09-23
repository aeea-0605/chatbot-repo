from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class NaverMovie(db.Model):
    """
    NaverMovie Class : MySQL DB의 naver_moive 테이블과 세션을 연결해주는 Class
    """

    __tablename__ = "naver_movie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    link = db.Column(db.Text)
    rate = db.Column(db.Float)
    genre = db.Column(db.Text)
    score = db.Column(db.Float)
    view = db.Column(db.Float)
    director = db.Column(db.Text)
    actor = db.Column(db.Text)
    crawled_time = db.Column(db.Text)

    def __init__(self, title, link, rate, genre, score, view, director, actor, crawled_time):
        self.title = title
        self.link = link
        self.rate = rate
        self.genre = genre
        self.score = score
        self.view = view
        self.director = director
        self.actor = actor
        self.crawled_time = crawled_time


    def __repr__(self):
        return f"<Movie {self.title}, {self.genre}, {self.rate}>"


db.create_all()