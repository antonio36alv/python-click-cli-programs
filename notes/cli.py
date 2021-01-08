# from os import system, listdir
import traceback
from os import path, system, stat
import click

@click.command()
@click.option("-v", is_flag = True, help="-v View file")
@click.option("-b", is_flag = True, help="-b Browse note directory tree")
def cli(v, b):
	"""
Suggested combinations of flags:
		

-b
	Browse tree of notes, prompted for topic (file), proceed to vim


-vb
	Browse tree of notes, prompted for topic (file), mdv the file

Recomended to quit after browse if quiting is intended
	"""	
	# we are here to browse, tree notes directory
	if b:
		# tree notes directory
		system("tree /home/t/Desktop/notes")
	# prompt for the file
	topic = input("Topic: ")
	topic += ".md"
	
	# if the file did not exist
	if not path.exists(f"/home/t/Desktop/notes/{topic}") and not v:
		# check to see if we specified any directories
		if topic.find("/") != -1:
			# handle directories
			handleNewDir(topic)
		# we make the file
		system(f"touch /home/t/Desktop/notes/{topic}")
		# and also let the user know
		print(f"Created file: {topic}")
	# file did exist and we were here to view it, this is an error
	elif not path.exists(f"/home/t/Desktop/notes/{topic}") and v:
		print("Error: Most likely an issue with your input. Make sure it exsits.")
		return

	# if we are here to view (command line option)
	if v:
		# then use mdv to view the file 
		print("time to show you the goods!")
		print(topic)
		system(f"mdv /home/t/Desktop/notes/{topic}")
	else:
		system(f"vim /home/t/Desktop/notes/{topic}")

		print("fuck what im saying ")
		if stat(f"/home/t/Desktop/notes/{topic}").st_size == 0:
			print("this did happen")
			system(f"rm /home/t/Desktop/notes/{topic}")



# write code to excute necessary mkdir's
def handleNewDir(userInput):
	print("here i come to save the day")
	# we got here because of this: /
	# possible risks are lines 34, 
	# will keep track of the last / found
	lastSlash = -1
	print(userInput)
	# we have to execute mkdir for every / we find
	for x in range(userInput.count("/")):
		lastSlash = userInput.find("/", lastSlash + 1)
		DIR = userInput[:lastSlash]
		system(f"mkdir /home/t/Desktop/notes/{DIR}")

# if __name__ == "__main__":
# 	cli()
