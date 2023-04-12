# 2. We are coding for QRcode

# I've already done with this ( QRcode ) project & it's my 2.0 version for my practice
# but you can do through this also.All the things will be available in my GitHub repository or linkdin.
# For more you can contact me everywhere !!



# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "https://www.youtube.com/@rykers_charan8169"
  
# Generate QR code
url = pyqrcode.create(s)
  
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)