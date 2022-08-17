from flask import Flask 
import os

def create_app():
	app=Flask(__name__)

	app.config.from_mapping(
		FROM_EMAIL=os.environ.get('FROM_EMAIL'),
		SENDGRID_KEY=os.environ.get('SENDGRID_API_KEY'),
		SECRET_KEY=os.environ.get('SECRET_KEY')
	)
	from . import portfolio

	app.register_blueprint(portfolio.bp)
	return app