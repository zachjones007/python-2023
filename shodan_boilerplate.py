
import shodan
import ezgmail
from twilio.rest import Client

# Your Shodan API key
SHODAN_API_KEY = 'jE5UJFS3qQhIyoclEf3KMduaEKbzwb1X'


TWILIO_ACCOUNT_SID = 'AC3db95df93de48e4b4b8866aad20f480e'
TWILIO_AUTH_TOKEN = '62a554d68bdc0ed7e00e4cdfe668c246'

def shodan_query(query):
    # init
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        #use the .search built in to seach what has been init
        results = api.search(query=query)

#for loop to check if elements are present in results
        for result in results['matches']:
            ip = result['ip_str']
            org = result.get('org', 'N/A')
            data = result.get('data', 'N/A')

            print(f"IP: {ip}")
            print(f"Organization: {org}")
            print(f"Data: {data}\n")

        # Send the report via email
        email_subject = 'Shodan Report'
        email_body = "\n".join([f"IP: {result['ip_str']}\nOrganization: {result.get('org', 'N/A')}\nData: {result.get('data', 'N/A')}\n\n" for result in results['matches']])
        send_report_email(email_subject, email_body)


    except shodan.APIError as e:
        print(f"Error: {e}")

def send_report_email(email_subject, email_body):
    # Use ezgmail to send the email
    ezgmail.init()  # Initialize the ezgmail module (make sure to authenticate with your Google account)
    ezgmail.send('recipient@example.com', email_subject, email_body)


#run code
search_query = "'in-tank inventory' state:'AZ'"
shodan_query(search_query)
