import requests as req
import random
import ctypes
import os
import time

USERPROFILE = os.path.expanduser("~")
SPI_SETDESKWALLPAPER = 0x0014

class Images:
    def __init__(self):
        self.imageUrls = [
            "https://th.bing.com/th/id/OIP.fBA_4gU6JpZxgwOq-_QHcgHaHa?rs=1&pid=ImgDetMain",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEv6-sdGoobcN1nh-vod7751AmGIQh0221Mw&usqp=CAU",
            "https://th.bing.com/th/id/OIG4.E2L6rD5b_wOo.rEOrxOY?pid=ImgGn",
            "https://th.bing.com/th/id/OIG2.Q5lwGBQuKQbeYRWoR.fX?pid=ImgGn",
            "https://pics.craiyon.com/2023-07-01/272e6851268c40688e0ab65e9c63926a.webp"
        ]
    def randomUrl(self):
        return random.choice(self.imageUrls)
    def saveRandomWallpaper(self):
        try:
            resp = req.get(self.randomUrl())
            imgPath = os.path.join(USERPROFILE,".newwallpaperrandom000000000.jpg")
            with open(imgPath, "wb") as file:
                file.write(resp.content)
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imgPath, 3)
            os.remove(imgPath)
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
    wall = Images()
    while True:
        wall.saveRandomWallpaper()
        time.sleep(10)