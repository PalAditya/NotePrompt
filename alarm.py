import plyer
import json
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os

def startup():
	os.system("python cli.py")

#Assumption: Alarms are stored in HH:mm format. No dates allowed so far
def viewjobs():

	current_time = str(datetime.datetime.now().strftime("%H:%M"))
	print("Apsscheduler worleed " + current_time)

	with open("tasks.json","r") as f:

		tasklist = f.read()
		tasklist = json.loads(tasklist)
		tasks = tasklist['todo']

		for v in tasks.values():
			print(v)
			if v.get('alarm') is not None and str(v['alarm']['time']) == current_time:
				plyer.notification.notify(v['name'], v.get('alarm').get('desc'), timeout = 10)


scheduler = BackgroundScheduler()
job = scheduler.add_job(viewjobs, 'interval', minutes = 1)
scheduler.start()
#time.sleep(3600*24)
