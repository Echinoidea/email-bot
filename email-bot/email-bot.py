# 2018-12-23
# Email bot that sends various quotes from a text file.

import random
import smtplib

sender = input("SENDER'S EMAIL ADDRESS: ")
receiver = [""]

quoteFile = ""


def get_line_count(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_quote(filename):
    try:
        with open(filename) as f:
            return f.read().split('\n')[random.randint(0, get_line_count(quoteFile))]
    except:
        print("ERROR: COULD NOT GET LINE FROM TEXT FILE.")
        return "Oops. Something went wrong."


username = sender
password = ""

password = input("PASSWORD: ")

quoteFile = input("TEXT FILE PATH: ")

receiver.append(input("ENTER RECEIVER'S EMAIL ADDRESS: "))

isInputDone = False
while not isInputDone:
    check = input("ADD ANOTHER RECEIVER? Y/N: ").upper()
    if check == "Y":
        receiver.append(input("ENTER RECEIVER'S EMAIL ADDRESS: "))
    elif check == "N":
        isInputDone = True
        break
    else:
        print("INVALID INPUT")


def send_email():
    msg = "\r\n".join([
        "From: {}".format(sender),
        "To: {}".format(receiver),
        "Subject: Quote",
        "",
        "{}".format(get_quote(quoteFile))
    ])

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(sender, receiver, msg)
        server.quit()
        print("SUCCESSFULLY SENT EMAIL")
        print(msg + "\n")
    except:
        print("ERROR: UNABLE TO SEND EMAIL")


emails = int(input("NUMBERS OF EMAILS TO SEND: "))

for i in range(emails):
    send_email()

input("PROCESS COMPLETE. PRESS ENTER TO EXIT...")
