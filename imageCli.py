import socket

# مقدار دهی متغیر ها
HOST = '192.168.1.8'
PORT = 12345
BUFFER_SIZE = 1024

# ایجاد شبکه
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # برقراری ارتباط با شبکه
    s.connect((HOST, PORT))
    print('Connected to the server...')
    # دریافت داده ها (عکس) از سرور
    data = s.recv(BUFFER_SIZE)
    # ذخیره کردن عکس
    with open('image_received.jpg', 'wb') as f:
        f.write(data)
    print('Image received successfully.')
