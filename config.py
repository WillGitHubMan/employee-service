from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = '12qwaszx'
app.config['MYSQL_DATABASE_DB'] = 'classicmodels'
app.config['MYSQL_DATABASE_HOST'] = 'database-1.c91pqs84sn4o.ap-southeast-2.rds.amazonaws.com'
mysql.init_app(app)