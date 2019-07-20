import cv2
import sys
import requests
import base64
import os

# Pegando dados do usuário e inicializando o detector
targetIp = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Lendo a imagem através da rede, decodificando, e convertendo para escala de cinza
response = requests.get("http://" + targetIp + ":3030/image")
image_base64 = response.json()["image_base64"]
with open("image.jpg", "wb") as f:
	f.write(base64.b64decode(image_base64))
image = cv2.imread("image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectando as faces na imagem
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Verifica se encontrou faces e acende o LED
n_faces = len(faces)
print("Encontrou %d faces!" % (n_faces))

led_pin = 0
os.system("gpio mode %d out" % (led_pin))
if n_faces > 0:
	os.system("gpio write %d 1" % (led_pin))
else:
	os.system("gpio write %d 0" % (led_pin))

# Desenhando um retângulo ao redor das faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces encontradas", image)
cv2.waitKey(0)
