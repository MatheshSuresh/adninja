import firebase_admin
import google.cloud
import json
from firebase_admin import credentials, firestore

def firebase(): 
    cred = credentials.Certificate("./ServiceAccountKey.json")
    app = firebase_admin.initialize_app(cred)

    store = firestore.client()

    users_ref = store.collection(u'Videos').document(u'02')

    try:
        user = users_ref.get()
        sample_data=(u'{}'.format(user.to_dict()))
        f= True
        link = ''
        while (f==True):
            for i in range(13,999):
                try:
                    link = link + sample_data[i]    
                except IndexError:
                    f= False
                    destination = ((link[:-2]))
                    download(destination)
                    break
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')

def download(url):
    import urllib.request
    print(url)
    urllib.request.urlretrieve(url,'2.mp4')

def main():
        firebase()

if __name__ == '__main__':
    main()
    
