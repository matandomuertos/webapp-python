from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = '\x11\xa0\x96\xb3\xc7U/\x87\xbc\xc3'

	from .pages import pages

	app.register_blueprint(pages, url_prefix='/')

	return app