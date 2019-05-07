import qrcode
import os
import time

def gen_qrcode():
    url = input("Website or text: ")
    name = input("Name for qrcode: ")
    qr = qrcode.QRCode(5, error_correction=qrcode.constants.ERROR_CORRECT_L) #QR object
    qr.add_data(url)
    qr.make()
    im = qr.make_image()
    time.sleep(1)

    qr_img_path = os.path.join(name+".png")

    if os.path.isfile(qr_img_path):
        os.remove(qr_img_path)

    im.save(qr_img_path, format = 'png')
    print("QRCode has been generated!")

if __name__ == "__main__": gen_qrcode()
