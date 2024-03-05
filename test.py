import requests
import numpy as np
import json

url = "https://parseapi.back4app.com/classes/jeu/"

headerGetDelete = {
    "X-Parse-Application-Id": "82aGsY5nVCNoECX4J474mWvYN1gK2BPOcJBme4Nm",
    "X-Parse-REST-API-Key": "njCoYKaYBqVJIbrCIXsRKCV8ScNFCV2ztrGRipv9",
}

headerPutPost = {
    "X-Parse-Application-Id": "82aGsY5nVCNoECX4J474mWvYN1gK2BPOcJBme4Nm",
    "X-Parse-REST-API-Key": "njCoYKaYBqVJIbrCIXsRKCV8ScNFCV2ztrGRipv9",
    "Content-Type": "application/json"
}

matrice= np.zeros((3,3))
matrice[1, 1] = 1
print(matrice)

data = {
    "matrice": matrice.tolist()
}

objectId = requests.request("GET", url, headers=headerGetDelete).json()["results"][0]["objectId"]
response = requests.request("PUT", url + "/" + objectId, headers=headerPutPost, json=data)
print(response)