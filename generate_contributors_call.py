import os

# inputing date from command line
date = input("What date is the call? (i.e. 19 February 2022) ")
print("Date chosen: " + date)

# Getting relevant date parameters for time zone link generation
date_split = date.split(" ")
day = date_split[0]
month = date_split[1]
year = date_split[2]

# inputing time from command line
time = input("What time is the call in UTC? (leave blank to set to 4pm UTC) ")
print(time)

# savvy time link based off of previous time zones in community call notes
link_base = "https://savvytime.com/converter/utc-to-ca-los-angeles-il-chicago-ny-new-york-city-brazil-sao-paulo-united-kingdom-london-france-paris-south-africa-johannesburg-msd-india-mumbai-hkt-japan-tokyo-australia-sydney/"

# code to handle default time if left blank
if time == "":
    # set the default time if input is set to blank
    # autogenerate time zones for default time
    link = link_base + month[0:3] + "-" + day + "-" + year + "/" + "4pm"
    time = "4pm UTC, which is can be found in your local time zone [here](%s)" % link

    #     time = """4pm UTC, which is:
    # Los Angeles: 09:00
    # Chicago: 11:00
    # New York: 12:00
    # São Paulo: 14:00
    # London: 17:00
    # Paris: 18:00
    # Johannesburg: 19:00
    # Moscow: 20:00
    # Mumbai: 22:30
    # Hong Kong: 01:00 on Sunday
    # Tokyo: 02:00 on Sunday
    # Sydney: 04:00 on Sunday"""
    print("Default time chosen: 4pm UTC")

else:
    # autogenerate time zones for given time
    temp_time = time
    link = link_base + month[0:3] + "-" + day + "-" + year + "/" + temp_time

    time = """%s UTC, which is can be found in your local time zone [here](%s)""" % (temp_time, link)
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

instructions_string = """
Content to copy & paste into discussion has been generated in 'output.txt' which will open automatically

In windows you can use the shortcuts:
- CTRL+A to select all
- CTRL+C to copy the text
- then CTRL+V in the discussion to paste the content

Similar shortcuts can be found in other operating systems

Double check & make any adjustments if required before posting such as

In the discussion:
- Set the category to Q&A
- Add labels "fscc" & "community"
- Check the date, time & hosts are what you intended them to be and that the time zone generated link works
"""

print(instructions_string)
# opening the file automatically to make it easy to copy & paste into discussion form
os.system("\"output.txt\"")
