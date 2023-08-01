from ping3 import ping
import csv
import ezgmail

# Initialize the ezgmail credentials
ezgmail.init(tokenFile='path_to_token.json', credentialsFile='path_to_credentials.json')

# Open the CSV file containing IP addresses
with open('ip.csv', 'r') as ipFile:
    ipReader = csv.DictReader(ipFile)
    msg = "IP Address\tPing Time\n"  # Header for the message

    for row in ipReader:
        ip = row['ip']
        ping_time = ping(ip)
        msg += f"{ip}\t{ping_time}\n"  # Append the IP and ping time to the message

# Send an email with the message
ezgmail.send('your_email@gmail.com', 'Ping Results', msg)

print("Email sent successfully!")
