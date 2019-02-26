#Import modules
from datetime import datetime
import libs.socks, argparse, re
import os, sys, shutil
root = sys.path
sys.path.insert(0,"libs")
from telethon import TelegramClient, sync
sys.path = root

#Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--number", "-n", dest="NUMBER", help="Telephone number", required=True)
parser.add_argument("--clear", "-c", dest="ISCLEARED", help="Clear directory before exporting", default=False, action="store_true")
parser.add_argument("--photos", "-p", dest="EXPORTPHOTOS", help="Export photos", default=False, action="store_true")
parser.add_argument("--audios", "-a", dest="EXPORTAUDIOS", help="Export audios", default=False, action="store_true")
parser.add_argument("--full", "-f", dest="EXPORTALL", help="Export everything", default=False, action="store_true")
parser.add_argument("--include-channels", "-i", dest="EXPORTCHANNELS", help="Export media from channels", default=False, action="store_true")

args = parser.parse_args()

#Save from arguments
number = args.NUMBER
clear = args.ISCLEARED
is_photos = args.EXPORTPHOTOS
is_audios = args.EXPORTAUDIOS
from_channels = args.EXPORTCHANNELS
if args.EXPORTALL:
	is_photos = True
	is_audios = True

#Functions
def parse_file_name(string):
	return re.sub(r"[<>:;,?\"*|/\\]", "_", string)
	
def log(data):
	print(data)
	sys.stdout.flush();

#Creating client
client = TelegramClient(
   "exporter", 
    760605, #api id
    "5ea1a2f93b1d038e328c012846a35b13" #api hash
)

#Logging in
log("Connecting to {}...".format(number))
client.connect()
log("Connected!")
status = client.is_user_authorized()
log("Authorization status: {}".format(status))

#Sending code
if status == False:
	client.send_code_request(number)
	code = input("Enter code: ")
	client.sign_in(number, code)
	
	#Get the last message from Telegram
	telegram_message_id = client.get_messages(777000, 1)[0].id
	result = client.delete_messages(777000, [telegram_message_id])[0]
	if result.pts_count == 1:
		log("Code message from Telegram was deleted!")
	else:
		log("Something went wrong while deleting Telegram code message!")

#Setup exports folder
if clear and os.path.isdir("exports"):
	log("Clearing old exports...")
	shutil.rmtree("exports")
username = client.get_entity("me").username
current_time = datetime.now().strftime("%Y.%m.%d %H-%M-%S")
exports_folder = os.path.join("exports", parse_file_name("{} ({})".format(username, number)), current_time)
if not os.path.exists(exports_folder):
    os.makedirs(exports_folder)

#Define arrays
users = {}
dialogs_content = {}
#Get all client's dialogs
dialogs = client.get_dialogs()
log("Exporting {} dialogs...".format(len(dialogs)))
log("=====================================")
#Iterating dialogs
#Exporting messages
for dialog in dialogs:
	#Prepare path to export
	file_name = parse_file_name(dialog.name)
	path = os.path.join(exports_folder, file_name + ".txt")
	#Getting messages count
	total = client.get_messages(dialog.id, 0).total
	
	log("Exporting {} messages from \"{}\"...".format(total, dialog.name))
	
	#Getting all messages
	messages = client.get_messages(dialog.id, total)
	dialog_file = open(path, "w", encoding="utf8")
	#Write date title
	date_format = "\n============|%Y.%m.%d|============\n"
	date = messages[-1].date
	dialog_file.write(date.strftime(date_format))
	
	for message in reversed(messages):
		is_channel = False
		#Write date title
		if date.day != message.date.day or date.month != message.date.month or date.year != message.date.year:
			date = message.date
			dialog_file.write(date.strftime(date_format))
		
		if not message.from_id == None and not message.from_id in users:
			users[message.from_id] = client.get_entity(message.from_id)
		
		#Format message prefix
		if not message.from_id == None:
			#For chats
			user = users[message.from_id]
			username = user.username or user.first_name + ((" " + user.last_name) if not user.last_name == None else "")
		else:
			#For channels
			is_channel = True
			username = dialog.name
		
		prefix = "[{}|{}]: ".format(message.date.strftime("%H:%M:%S"), username)
		
		if message.message == None:
			message.message = ""
			
		if not message.photo == None:
			if not is_channel or (is_channel and from_channels):
				if not dialog.name in dialogs_content:
					dialogs_content[dialog.name] = {"photos": [], "audios": []};
				dialogs_content[dialog.name]["photos"].append(message);

				message.message += "◄Photo:\"{}.jpg\"►".format(len(dialogs_content[dialog.name]["photos"]) - 1)
			else:
				message.message += "◄Photo►"
			
		if not message.action == None and hasattr(message.action, "duration"):
			message.message += "◄Call:{}s►".format(message.action.duration)
			
		if not message.media == None and hasattr(message.media, "document"):
			for attribute in message.media.document.attributes:
				if attribute.CONSTRUCTOR_ID == 0x15590068: #DocumentAttributeFilename
					message.message += "◄Document:\"{}\"►".format(attribute.file_name)
				elif attribute.CONSTRUCTOR_ID == 0x6319d612: #DocumentAttributeSticker
					message.message += "◄Sticker:{}►".format(attribute.alt)
				elif attribute.CONSTRUCTOR_ID == 0xef02ce6: #DocumentAttributeVideo
					message.message += "◄Video:{}s►".format(attribute.duration)
				elif attribute.CONSTRUCTOR_ID == 0x9852f9c6: #DocumentAttributeAudio
					if not is_channel or (is_channel and from_channels):
						if not dialog.name in dialogs_content:
							dialogs_content[dialog.name] = {"photos": [], "audios": []};
							
						dialogs_content[dialog.name]["audios"].append(message);
						message.message += "◄Audio:{}s:\"{}.ogg\"►".format(attribute.duration, len(dialogs_content[dialog.name]["audios"]) - 1)
					else:
						message.message += "◄Audio:{}s►".format(attribute.duration)
		
		#Save message
		dialog_file.write(prefix + message.message + "\n")
	dialog_file.close()

log("=====================================")
log("")

#Exporting media content

#Exporting audios
if is_audios:
	log("Exporting audios...")
	log("=====================================")

	for dialog in dialogs_content:
		audios = dialogs_content[dialog]["audios"]
		
		if (len(audios) > 0):
			#Prepare path to export
			audios_path = os.path.join(exports_folder, "audios", parse_file_name(dialog))
			if not os.path.exists(audios_path):
				os.makedirs(audios_path)
			
			log("Exporting {} audios from \"{}\"...".format(len(audios), dialog))
		
		for id, audio in enumerate(audios):
			client.download_media(audio, os.path.join(audios_path, str(id)))
		
	log("=====================================")
	log("")

#Exporting photos
if is_photos:
	log("Exporting photos...")
	log("=====================================")

	for dialog in dialogs_content:
		photos = dialogs_content[dialog]["photos"]
		if (len(photos) > 0):
			#Prepare path to export
			photos_path = os.path.join(exports_folder, "photos", parse_file_name(dialog))
			if not os.path.exists(photos_path):
				os.makedirs(photos_path)
			
			log("Exporting {} photos from \"{}\"...".format(len(photos), dialog))
		
		for id, photo in enumerate(photos):
			client.download_media(photo, os.path.join(photos_path, str(id)))
			
	log("=====================================")
	log("")
log("Export successfully finished!")