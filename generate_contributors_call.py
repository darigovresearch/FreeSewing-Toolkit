import os

# inputing date from command line
date = input("What date is the call? ")
print("Date chosen: " + date)

# inputing time from command line
time = input("What time is the call? (leave blank to set to 16:00 UTC)")
print(time)

# code to handle default time if left blank
if time == "":
	# set the default time if input is set to blank
	# TODO autogenerate time zones
	time = """16:00 UTC, which is:
Los Angeles: 09:00
Chicago: 11:00
New York: 12:00
São Paulo: 14:00
London: 17:00
Paris: 18:00
Johannesburg: 19:00
Moscow: 20:00
Mumbai: 22:30
Hong Kong: 01:00 on Sunday
Tokyo: 02:00 on Sunday
Sydney: 04:00 on Sunday"""
	print("Default time chosen: 16:00 UTC")

else:
	print("Time chosen: " +  time)

# inputing hosts from command line
hosts = input("Who are the hosts? (leave blank to set to @tangerineshark and @lucibytes)")
print(hosts)

# code to handle default hosts if left blank
if hosts == "":
	# set the default hosts if input is set to blank
	hosts = """@tangerineshark and @lucibytes"""
	print("Default hosts chosen: @tangerineshark and @lucibytes")

else:
	print("hosts chosen: " +  time)


# generating full string to copy & paste into form
reference_text = """Contributor call: """ + date + """
You are all invited to the FreeSewing Contributor Call.
Please leave a comment here or [on Discord](https://discord.freesewing.org/) to add things to the agenda.
This issue will be updated after the call with notes and to-dos.

### About
FreeSewing's contributor call is an informal hangout/chat/meeting that is open to all FreeSewing contributors and users alike.
The call is organized/hosted by """ + hosts + """ on our Discord server.
The call does not have a fixed structure or agenda items. Everyone is free to suggest agenda items, ask questions, or bring ideas.

Details:

Location: https://discord.freesewing.org (meeting room: 🔊voice chat)
Date: """ + date + """ """ + time + """
Or check the bot in Discord! #meetings

### Agenda
- To be determined

> This discussion will be updated after the call with notes and to-dos.
"""

# writing to file to make it easy to copy & paste into discussion form
x = open("output.txt", "w", encoding="utf8")
x.write(reference_text)
x.close()

instructions_string = """Content to copy & paste into discussion has been generated in 'output.txt which will open automatically

In windows you can use the shortcuts:
- CTRL+A to select all
- CTRL+C to copy the text
- then CTRL+V in the discussion to paste the content

Similar shortcuts can be found in other operating systems

Double check & make any adjustments if required before posting such as

In the discussion:
- Set the category to Q&A
- Add labels "fscc" & "community"
- Check the date, time & hosts are what you intended them to be
"""

print(instructions_string)
# opening the file automatically to make it easy to copy & paste into discussion form
os.system("\"output.txt\"")
