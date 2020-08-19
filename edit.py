import json
import colored
from colored import stylize
from pyautogui import typewrite

def log(string, color, font="slant", figlet=False):
	print(stylize(string, colored.fg(color)), end = " ")

def readtasks(task_id):

	with open("tasks.json","r") as f:
		tasklist = f.read()
	
	tasklist = json.loads(tasklist)
	tasks = tasklist['todo']

	for k, v in tasks.items():
		if str(k) != str(task_id):
			continue
		log("-------------- Editing Task: " + v['name'] + " ---------------", "spring_green_3a")
		print()
		data = edit(v)
		tasks[k] = data
	
	tasklist = json.dumps(tasklist)
	with open("tasks.json","w") as f:
		f.write(tasklist)


def edit(taskdata):

	allowed_details = ["priority", "name"] #TODO: Add Alarm
	edited_task = {}

	for k, v in taskdata.items():
		allowed_details.remove(k)
		log(k + ": " , "turquoise_2")
		typewrite(v)
		user_val = input()
		edited_task[k] = user_val
	
	for details in allowed_details:
		log(details + ": " , "turquoise_2")
		user_val = input()
		edited_task[details] = user_val
	
	return edited_task
