

import csv
from ping3 import ping
import ezgmail

# Initialize the Gmail API
ezgmail.init(tokenFile='token.json', credentialsFile='credentials.json')

# Open the CSV filee and read IP addresses
ipFile = open('ip.csv')
ipReader = csv.DictReader(ipFile)
msg = "Ping Results:\n\n"

for row in ipReader:
    ip = row['ip']
    ping_time = ping(ip)
    msg += f"{ip}: {ping_time}\n"

# Close the CSV file
ipFile.close()

# Send the email
subject = "Ping Results"
ezgmail.send('zjones5@mail.pima.edu', subject, msg)
