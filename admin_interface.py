"""
Requirements:
 	pip3 install flask

Usage:
	- From the project home directory export the environment variable.
		export FLASK_APP=admin_interface.py 
	- Start the local app from the command line:
		flask run
"""

from flask import Flask, request,render_template
from admin import update_cron, git_pull, git_push


PATH_OF_GIT_REPO = '.'
COMMIT_MESSAGE = 'admin settings updated'
UPDATE_NB_FILE = '.github/workflows/update-nb.yaml'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_30min')
def update_30min():
	CRON_SETTING = '*/30 * * * *'
	update_cron(CRON_SETTING)
	git_pull()
	git_push()
	return render_template('updated.html')

@app.route('/update_hourly')
def update_hourly():
	CRON_SETTING = '0 * * * *'
	update_cron(CRON_SETTING)
	git_pull()
	git_push()
	return render_template('updated.html')
	
@app.route('/update_2h')
def update_2h():
	CRON_SETTING = '0 */2 * * *'
	update_cron(CRON_SETTING)
	git_pull()
	git_push()
	return render_template('updated.html')

@app.route('/update_daily')
def update_daily():
	CRON_SETTING = '0 1 * * *'
	update_cron(CRON_SETTING)
	git_pull()
	git_push()
	return render_template('updated.html')

@app.route('/update_weekly')
def update_weekly():
	CRON_SETTING = '5 8 * * 0'
	update_cron(CRON_SETTING)
	git_pull()
	git_push()
	return render_template('updated.html')

app.run()
