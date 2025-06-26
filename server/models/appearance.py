from server.app import db
from sqlalchemy import CheckConstraint

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)
    
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )