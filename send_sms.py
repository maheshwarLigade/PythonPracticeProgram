from twilio.rest import TwilioRestClient

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account, token)

message = client.messages.create(to="+12316851234", from_="+15555555555",
                                 body="Hello there!")
