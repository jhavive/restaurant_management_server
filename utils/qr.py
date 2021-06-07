import qrcode
from io import BytesIO
import os
from restaurant_management_server.settings import BASE_DIR


def saveQRCode(hotel_id, table_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(table_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    print(BASE_DIR)
    if not os.path.isdir(os.path.join(BASE_DIR, 'public', 'qr', str(hotel_id))):
        os.mkdir(os.path.join(BASE_DIR, 'public', 'qr', str(hotel_id)))

    path = os.path.join(BASE_DIR, 'public', 'qr', str(hotel_id), str(table_id) + '.jpeg')
    img.save(path)

