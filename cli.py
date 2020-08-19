import os
import sys
import six
import json
import colored
from colored import stylize
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--add", help = "Add a task")
parser.add_argument("--rem", help = "Remove a task")
parser.add_argument("--view", help = "Remove a task")
parser.add_argument("--alarm", help = "Set reminder for an already added task")
args = parser.parse_args()

add = None
remove = None
view = None
if args.add:
	add = args.add
if args.rem:
	remove = int(args.rem)
if args.view:
	if args.view.lower() != "all":
		view = int(args.view)
	else:
		view = args.view.lower()

if not os.path.isfile("tasks.json"):
	print("----Creating initial configuration----")
	tasks = {"taskcount":0,"todo":{}}
	tasks = json.dumps(tasks)
	with open("tasks.json", "w") as f:
		f.write(tasks)
	print("----CLI configuration done----")


def getContentType(answer, conttype):
	return answer.get("content_type").lower() == conttype.lower()

def log(string, color, font="slant", figlet=False):
	print(stylize(string, colored.fg(color)))

def main():
	if add is not None:
		with open("tasks.json","r") as f:
			tasklist = f.read()
		tasklist = json.loads(tasklist)
		tasks = tasklist['taskcount']
		tasklist['todo'][tasks] = add
		tasklist['taskcount'] = tasks + 1
		tasklist = json.dumps(tasklist)
		with open("tasks.json","w") as f:
			f.write(tasklist)
		log("Task added!", "green_1")
		sys.exit(0)
	if view is not None:
		with open("tasks.json","r") as f:
			tasklist = f.read()
		tasklist = json.loads(tasklist)
		tasks = tasklist['todo']
		count = 0
		for k, v in tasks.items():
			log(str(k) + " : " + v, "cyan_1")
			count += 1
			if isinstance(view, int) and view == count:
				break
		sys.exit(0)
	if remove is not None:
		rem = remove
		with open("tasks.json","r") as f:
			tasklist = f.read()
		tasklist = json.loads(tasklist)
		if rem > tasklist['taskcount']:
			log("You do not have such a task currently!", "red_1")
			sys.exit(0)
		new_list = {}
		count = 0
		for k, v in tasklist['todo'].items():
			if str(k) == str(rem):
				pass
			else:
				#print(str(k) + "," + str(rem))
				new_list[count] = v
				count += 1
		#print(new_list)
		tasklist['taskcount'] = tasklist['taskcount'] - 1
		tasklist['todo'] = new_list
		tasklist = json.dumps(tasklist)
		with open("tasks.json","w") as f:
			f.write(tasklist)
		log("Task removed!", "indian_red_1d")
		sys.exit(0)

if __name__=="__main__":
	main()