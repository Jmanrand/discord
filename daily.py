import requests
import os

hooli_daily_channel_id = "979184045583917076"
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/access.secret') as f:
    auth_token = f.readline()

json_dict = {
    "data": [
        {
            "channel_id": hooli_daily_channel_id,
            "payload": {"content": "!daily"}
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