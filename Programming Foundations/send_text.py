from twilio.rest import TwilioRestClient
#from twilio import rest

account_sid = "AC2e54b07b97d0c1060f7d10a0451a3501" # Your Account SID from www.twilio.com/console
auth_token  = "022933820157e3579f5f077365c880e5"  # Your Auth Token from www.twilio.com/console

#client = rest.TwilioRestClient(account_sid, auth_token)
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from the other side",
    to="+12022976795",    # Replace with your phone number
    from_="+12027590216") # Replace with your Twilio number

print(message.sid)
