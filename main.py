import discord
import asyncio
import requests
import threading
import sys
import os
from typing import Optional
from colorama import Fore
import time

print("Discord Token Hoster")

session = requests.Session()
tokens = []
with open("tokens.txt", "r") as f:
  client_token = f.read().split("\n")

if len(client_token) == 0:
  print("Please Write Some Tokens In tokens.txt to run this code.")
  exit()

def check(Token):
  response = requests.get(f"https://discord.com/api/v9/users/@me", headers={"Authorization": Token})
  if response.status_code in [204, 200, 201]:
    print(f"{Token} Is Vaild.")
    tokens.append(Token)
  if "need to verify" in response.text:
    print(f"{Token} Needs Verification.")
  elif response.status_code in [404, 401, 400]:
    print(f"{Token} is Invaild Token.")

for tk in client_token:
  check(tk)


if len(tokens) == 0:
  print("All Tokens Were Invaild, Try Again With Some Other Tokens.")
  exit()

time.sleep(2)
if sys.platform in ["linux", "linux2"]:
  os.system("clear")
else:
  os.system("cls")

stat = input('What Should Be The Accounts Status Idle, Dnd, Online, Mobile, Random:')
akks = []
stl = stat.lower()
if stl == "dnd":
  status = discord.Status.dnd
elif stl == "idle":
  status = discord.Status.idle
elif stl == "online":
  status = discord.Status.online
elif stl == "random":
  status = random.choice([discord.Status.online, discord.Status.idle, discord.Status.online])
ty = input("What Should Be The Activity Type Playing, Streaming, Listening, Watching: ")
tyy = ty.lower()
if tyy == "streaming":
  name = input("Streaming Name: ")
  acttt = discord.Streaming(name=name, url="https:/twitch/KaramveerPlayZ")
elif tyy == "playing":
  name = input("Playing Name: ")
  acttt = discord.Game(name=name)
elif tyy == "listening":
  name = input("Listening Name: ")
  acttt=discord.Activity(type=discord.ActivityType.listening, name=name)
elif tyy == "watching":
  name = input("Watching Name: ")
  acttt=discord.Activity(type=discord.ActivityType.watching, name=name)
loop = asyncio.get_event_loop()
for tk in tokens:
  client = discord.Client(status=status, activity=acttt)
  loop.create_task(client.start(tk, bot=False))
  akks.append(client)
  print(" ")
  print("{} Is Hosted.\n".format(tk))

threading.Thread(target=loop.run_forever).start()

while True:
  idk = 0
  idk += 1
