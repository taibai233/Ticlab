import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'it is a very hard to guess str'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	DUTTIC_MAIL_SUBJECT_PREFIX = '[Duttic]'
	DUTTIC_MAIL_SENDER = 'Duttic Admin <dut_tic2016@163.com>'
	DUTTIC_ADMIN = os.environ.get('DUTTIC_ADMIN')


	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.163.com'
	MAIL_PORT = 25
	MAIL_USE_TLS = False
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or 'dut_tic2016'
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or '2016duttic'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data_dev.sqlite')

class TestingConfig(Config):
	Testing = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data_test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {	'development' : DevelopmentConfig,
			'testing' : TestingConfig,
			'production' : ProductionConfig,
			'default' : DevelopmentConfig
		}
	
	