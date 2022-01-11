import eel
import requests

eel.init("web")

@eel.expose()
def getUsers():
    usersData = requests.get("https://jsonplaceholder.typicode.com/users")
    
    if usersData.status_code == 200:
        return usersData.json()
    else:
        print("Internal Server Error!")
        
@eel.expose()
def getUser(id):
    usersData = requests.get("https://jsonplaceholder.typicode.com/posts/" + id)
    
    if usersData.status_code == 200:
        return usersData.json()
    else:
        print("Internal Server Error!")

@eel.expose()
def getImage(id):
    imageData = requests.get("https://picsum.photos/id/" + id + "/info")
    
    if imageData.status_code == 200:
        return imageData.json()
    else:
        print("Internal Server Error!")

eel.start("index.html", size = (500, 700))