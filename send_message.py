import os
from twilio.rest import Client

account_sid = "AC8a95a85cabd382f190b3ac17e0a97d26"
auth_token = "1c531beaff38baf0e0b5b5148a225b61"

client = Client(account_sid, auth_token)
message = client.messages \
        .create(
            body="It will rain today,take your umbrella.",
            from_="+16065540848",
            to="+8619808145773"
        )
print(message.status)
