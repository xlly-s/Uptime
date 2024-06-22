from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%D %H:%M:%S")






# create embed object for webhook
# you can set the color as a decimal (color=242424) or hex (color="03b2f8") number  

# add embed object to webhook


import requests
while True:
    try:
        resp = requests.get("http://31.127.85.170:21924/", timeout=(10, 12))
        if resp.status_code == 401:
        
            print("Online.")
            sleep(10)
    except requests.exceptions.Timeout:
     


        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1097200751362707466/yU-ZeR5W5I-6R_akmw7yw1bYkYwvqJUWlDKsTrA5zQrNHve_ipavSVnHYBpTeEtmBNfA")


        desc = "\n**Service Name**\nBlurpys Movies\n\n**Serviced URL**\nhttp://31.127.85.170:21924/\n\n**Time Of Service**\n"+current_time+" BST\n\n"
        embed = DiscordEmbed(title=":x: Blurpys Plex Server is Offline! :x: ", description=desc, color="FF0000")
        webhook.add_embed(embed)
        print("Offline")
        
        response = webhook.execute()
        sleep(150)
       










 
