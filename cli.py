import os
import sys
import six
import json
import colored
from colored import stylize
import argparse
from alarm import startup
import threading
import subprocess 
import time
from edit import readtasks

parser = argparse.ArgumentParser()
parser.add_argument("--add", help = "Add a task")
parser.add_argument("--rem", help = "Remove a task")
parser.add_argument("--view", help = "View all tasks") #Add verbose mode
parser.add_argument("--edit", help = "Edit a task")
parser.add_argument("--alarm", help = "Set reminder for an already added task", nargs = 3, metavar = ('task id', 'time in hh:mm', 'text'))
args = parser.parse_args()

#Start alarm. NOTE: Currently buggy
"""
DETACHED_PROCESS = 0x00000008
pid = subprocess.Popen(["pythonw", "alarm.py"], creationflags = subprocess.CREATE_NEW_CONSOLE)
"""

add = None
remove = None
view = None
alarm = None
edit = None
alarm_time = -1
alarm_text = ""
add_dict = True

if args.add:
	add = args.add
	try:
		add = json.loads(add)
	except:
		add_dict = False

if args.rem:
	remove = int(args.rem)

if args.view:
	if args.view.lower() != "all":
		view = int(args.view)
	else:
		view = args.view.lower()

if args.alarm:
	alarm = int(args.alarm[0])
	alarm_text = args.alarm[2]
	alarm_time = args.alarm[1]

if args.edit:
	edit = int(args.edit)

def log(string, color, font="slant", figlet=False):
	print(stylize(string, colored.fg(color)))

if not os.path.isfile("tasks.json"):
	log("----Creating initial configuration----", "light_green")
	tasks = {"taskcount":0,"todo":{}}
	tasks = json.dumps(tasks)
	with open("tasks.json", "w") as f:
		f.write(tasks)
	log("----CLI configuration done----", "light_green")

def getContentType(answer, conttype):
	return answer.get("content_type").lower() == conttype.lower()

def main():

	"""
	There are 2 possibilities: add with single arg, that is the name
	add with a dict specifying everything to add. Not advised, better way is to add just
	a task and then edit it via --edit key
	"""

	if add is not None:

		with open("tasks.json","r") as f:
			tasklist = f.read()

		tasklist = json.loads(tasklist)
		tasks = tasklist['taskcount']

		new_task = {}
		if add_dict:
			new_task = add
		else:
			new_task['name'] = add
		
		tasklist['todo'][tasks] = new_task
		tasklist['taskcount'] = tasks + 1
		tasklist = json.dumps(tasklist)

		with open("tasks.json","w") as f:
			f.write(tasklist)
		log("Task added!", "green_1")
		sys.exit(0)

		with open("tasks.json","w") as f:
			f.write(tasklist)
		log("Task added!", "green_1")
		sys.exit(0)

	if view is not None: #Add verbose mode for all task details

		with open("tasks.json","r") as f:
			tasklist = f.read()
		tasklist = json.loads(tasklist)

		tasks = tasklist['todo']
		count = 0
		for k, v in tasks.items():
			log(str(k) + " : " + v['name'], "cyan_1")
			count += 1
			if isinstance(view, int) and view == count:
				break
		sys.exit(0)

	if remove is not None:

		rem = remove
		with open("tasks.json","r") as f:
			tasklist = f.read()
		tasklist = json.loads(tasklist)

		if rem > tasklist['taskcount'] - 1:
			log("You do not have such a task currently!", "red_1")
			sys.exit(0)

		new_list = {}
		count = 0

		for k, v in tasklist['todo'].items():
			if str(k) == str(rem):
				pass
			else:
				new_list[count] = v
				count += 1

		tasklist['taskcount'] = tasklist['taskcount'] - 1
		tasklist['todo'] = new_list
		tasklist = json.dumps(tasklist)

		with open("tasks.json","w") as f:
			f.write(tasklist)

		log("Task removed!", "indian_red_1d")
		sys.exit(0)
	
	if alarm is not None:

		log("Sorry, this service is undergoing revision >_<", "cyan_3")
		sys.exit(0)

		with open("tasks.json","r") as f:
			tasklist = f.read()
		tasklist = json.loads(tasklist)

		if alarm > tasklist['taskcount'] - 1:
			log("You do not have such a task currently!", "red_1")
			sys.exit(0)
		
		for k, v in tasklist['todo'].items():
			if str(k) == str(alarm):
				tasklist['todo'][k]['alarm'] = {"time" : alarm_time, "desc" : alarm_text}
				log("Alarm added!", "cyan_3")
		
		tasklist = json.dumps(tasklist)
		with open("tasks.json","w") as f:
			f.write(tasklist)
		sys.exit(0)
	
	if edit is not None:

		with open("tasks.json","r") as f:
			tasklist = f.read()
		tasklist = json.loads(tasklist)

		if edit > tasklist['taskcount'] - 1:
			log("You do not have such a task currently!", "red_1")
			sys.exit(0)
		
		readtasks(edit)

if __name__=="__main__":
	main()
