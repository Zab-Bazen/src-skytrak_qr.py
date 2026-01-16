# Import windows terminal commands
import subprocess
# Import QRCode from pyqrcode
import pyqrcode
import png
# Import pyqrcode to convert QRcode to image
from pyqrcode import QRCode
# Import PIL import to open Images after all the code runs
from PIL import Image

# This Runs windows commands to show the wifi or any device thats connected to the wifi.
wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'])
data = wifi.decode('utf-8')

# for SKYTRAK original units
if (data[-71:-64]) == "SKYTRAK":
    print("This is a SKYTRAK original")
    mac_address = (data[-63:-51])
    print(mac_address)

    # Generate QR code
    url = pyqrcode.create(mac_address)
    # Create and save the svg file naming "myqr.svg"
    url.svg("myqr.svg", scale = 8)
    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale = 6)
    # this opens qr code as an image
    with Image.open('myqr.png') as img:
        img.show()

#for SKYTRAKPLUS units
elif (data[-71:-64]) == " STPLUS":
    print("This is a SKYTRAKPLUS")
    mac_address = (data[-63:-51])
    print(mac_address)

    # Generate QR code
    url = pyqrcode.create(mac_address)
    # Create and save the svg file naming "myqr.svg"
    url.svg("myqr.svg", scale = 8)
    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale = 6)
    # this opens qr code as an image
    with Image.open('myqr.png') as img:
        img.show()
