"""
Requirements:
 	pip3 install gitpython

Usage:
	- Run from the command line:
		python3 admin.py --update_hourly
			- Changes update frequency to once every hour.
		python3 admin.py --update_daily
			- Changes update frequency to once every day.
		python3 admin.py --update_weekly
			- Changes update frequency to once every week.
		python3 admin.py --update_10min
			- Changes update frequency to update every 10 minutes.
"""

from git import Repo
import git 
import yaml
import argparse


PATH_OF_GIT_REPO = '.'
COMMIT_MESSAGE = 'admin settings updated'
UPDATE_NB_FILE = '.github/workflows/update-nb.yaml'


def update_cron(cron_setting):
	print('Updating cron settings ...')
	with open(UPDATE_NB_FILE, 'r') as text_file:
		update_nb = text_file.readlines()
		cron_line = update_nb[3]
		cron_index = cron_line.index('cron:')
		print('Previous setting: ', cron_line)
		new_line = cron_line[:cron_index+6] + " " + "'" + str(cron_setting) + "'" + "\n"
		print("Changing to: ", new_line)
		update_nb[3] = new_line

	with open(UPDATE_NB_FILE, 'w') as f:
		f.writelines(update_nb)


def git_pull():
	repo = git.cmd.Git(PATH_OF_GIT_REPO)
	print('Pulling the newest app version from GitHub...')
	repo.pull()


def git_push():
    try:
	    repo = Repo(PATH_OF_GIT_REPO)
	    repo.git.add(update=True)
	    print('Commiting changes to GitHub...')
	    repo.index.commit(COMMIT_MESSAGE)
	    origin = repo.remote(name='origin')
	    origin.push()
    except:
        print('Some error occured while pushing the code')    


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--update_30min',  action='store_true')
	parser.add_argument('--update_hourly',  action='store_true')
	parser.add_argument('--update_2h',  action='store_true')
	parser.add_argument('--update_daily',  action='store_true')
	parser.add_argument('--update_weekly',  action='store_true')
	parser.add_argument('--update_10min',  action='store_true')
	args = parser.parse_args()
	if args.update_hourly:
		CRON_SETTING = '0 * * * *'
	elif args.update_daily:
		CRON_SETTING = '0 1 * * *'
	elif args.update_weekly:
		CRON_SETTING = '5 8 * * 0'
	elif args.update_10min:
		CRON_SETTING = '*/10 * * * *'
	elif args.update_30min:
		CRON_SETTING = '*/30 * * * *'
	elif args.update_2h:
		CRON_SETTING = '0 */2 * * *'
	
	
	update_cron(CRON_SETTING)
	git_pull()
	git_push()


if __name__ == "__main__": 
	main()