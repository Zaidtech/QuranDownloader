import os
import re
import urllib.request
import urllib.error
import platform
import time
import random
import socket


timeout = 100
socket.setdefaulttimeout(timeout)

print(f"You are currently running {os.name}.....")
print(f"Running on {platform.system}...")
print("Starting download")
with open("Link.text","r") as f:
    urls = f.readlines()
    downloaded = []
    for url in urls:
        print(url)
        # print(f"URL : {url}")
        random_delay = random.randint(0,10)
        # time.sleep(random_delay) # to reduce download speed set setting a sleep timer to 5sec  
        
        try:
            # filename using regex...
            filename = re.findall("[0-9A-Za-z\-\.mp3]*",url)[14]
            
            # time.sleep(5)
            urllib.request.urlretrieve(url,f"./{filename}")
            # time.sleep(10) # to reduce download speed set setting a sleep timer to 5sec  
            print(f"File downloaded as: {filename} ")
            
        except Exception as e:
            print("Download failed!!...")
            print(str(e))

 

