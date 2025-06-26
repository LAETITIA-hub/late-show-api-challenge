import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:newpassword123@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret"  # Change in production
    JWT_ACCESS_TOKEN_EXPIRES = False  # Disable token expiration for testing
    JWT_CSRF_CHECK_FORM = False  # Disable CSRF for API endpoints

config = Config()