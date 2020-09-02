import requests
import smtplib

# API key
api_file = open("api-key.txt", "r")
api_key = api_file.read()
api_file.close()

# home address input
home = input("Enter your home address\n")

# work address
work = input("Enter your work address\n")

# base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get response
r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key)

# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

#print the total travel time
print("\n The total travel time from home to work is: ", time)

# check if travel time is more than 1 hour
if (seconds > 1800):
    # email constraints
    sender = "aleciin.psn@gmail.com"
    recipient = "evangelista.alec@gmail.com"
    subject = "Sick Day"
    message = "Hi Team, \n\nSorry, but I cannot make it into work today."

    # format email
    email = "Subject: {}\n\n{}".format(subject, message)

    # get sender email
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()

    # create SMTP session
    s = smtplib.SMTP("smtp.gmail.com", 587)

    # start TLS for security
    s.starttls()

    # authentication
    s.login(sender, pw)

    # sending the email
    s.sendmail(sender, recipient, email)

    # succcess message
    print("\nSuccessfully sent email to", recipient)
