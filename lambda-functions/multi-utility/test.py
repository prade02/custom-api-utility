import multi_utility
event = {
    "body": "{\"resource\":\"base64\", \"action\": \"decode\", \"message\": \"cHJhZGVlcA==\"}"
}
print(multi_utility.handler(event,None))

