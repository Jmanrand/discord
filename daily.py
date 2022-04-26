import requests
test_channel_id = "937500122185617438"
test2_channel_id = "937501668503867432"

hooli_daily_channel_id = "906671688463290420"
clem_cashier_channel = "945786893843464252"

with open('access.secret') as f:
    auth_token = f.readline()

json_dict = {
    "data": [
        {
            "channel_id": test_channel_id,
            "payload": {"content": "!daily"}
        },
        {
            "channel_id": test2_channel_id,
            "payload": {"content":"$collect"}
        }
    ]
}

header = {
    'authorization': auth_token
}

for i in json_dict["data"]:
    channel_id = i["channel_id"]
    payload = i["payload"]
    print(channel_id, payload)
    r = requests.post(url="https://discord.com/api/v9/channels/" + channel_id + "/messages", data=payload, headers=header)

# if __name__ == '__main__':
#     main()