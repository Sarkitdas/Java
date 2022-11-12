import qrcode
import image

qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
url="https://www.facebook.com/albart.sarkit.5/"

qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")
