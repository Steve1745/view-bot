import webbrowser
import time

# Your tiktok video URL
url = "https://www.instagram.com/reel/Cs5f2N6Od15/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="

# Number of views you want
num = 100

views=0
for i in range(num):
    webbrowser.open(url, new=2) 
    views=views+1
    print("[+] New view - View amounnt :"+str(views))
    time.sleep(0.1) 
print(str(num) + " views sended")
    
