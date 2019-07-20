import cv2
import sys
import requests
import base64

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

print("Encontrou {0} faces!".format(len(faces)))

# Desenhando um retângulo ao redor das faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces encontradas", image)
cv2.waitKey(0)
