import requests
import json
import random
import string
from time import sleep

def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_message(webhook_url):
    username = " Ayu X Webhook V1 bitches "
    message = ":warning: @everyone"+" "+messages+" "+" :warning: "+" :chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:**https://discord.gg/JX8wHc5mUC**:truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag:"
    avatar = "https://picsum.photos/id/{}/200".format(random.randint(1, 500))
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": True
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, data, headers=header)

    if not response.ok:
        if response.status_code == 429:
            print("Too many requests... - waiting before retying...")
        else:
            print("Failed to send message!")
            print(response.status_code)
            print(response.reason)
            print(response.text)
        return False
    else:
        print("Send message!")
        return True

messages= input("put ur message u wanna spam to him:")
webhook = input("put the webhook : ")
attempt_count = 0
sent_count = 0

print("spammin dat bitch hard asf if u wanna stop it like a bitch type ctrl+c")
sleep(1)

failed_previous = False

try:
    while True:
        if (send_message(webhook)):
            sent_count += 1
            failed_previous = False
        else:
            if failed_previous:
                print("Waiting 30 seconds - didn't work second time")
                sleep(30)
            else:
                sleep(1)
            failed_previous = True
        attempt_count += 1
except KeyboardInterrupt:
    print("Stopped! Send {} messages and did {} attempts.".format(sent_count, attempt_count))
pass
