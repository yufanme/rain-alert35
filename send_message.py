import os
from twilio.rest import Client

account_sid = "AC8a95a85cabd382f190b3ac17e0a97d26"
auth_token = "d0a97233c9bdc2f83822d6c4771f018f"

client = Client(account_sid, auth_token)
message = client.messages \
        .create(
            body="It will rain today,take your umbrella.",
            from_="+16065540848",
            to="+8619808145773"
        )
print(message.status)
