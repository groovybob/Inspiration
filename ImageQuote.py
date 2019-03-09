from pixabay import Image
import csv
import random
import urllib.request
from multi_rake import Rake
from PIL import Image as IMAGE
from PIL import ImageDraw, ImageFont
import requests
from urllib.request import urlopen

def get_kword():
    with open("quotes.csv", 'r') as quotes:
        reader = csv.reader(quotes)
        chosen_row = random.choice(list(reader))
        print(chosen_row)
        author = chosen_row[0]
        quote = chosen_row[1]

    rake = Rake()

    keywords = rake.apply(quote)

    if len(keywords)==0:
        kword = author
    else:
        kword=keywords[1][0]
    print(kword)
    return kword


with open("API_key.txt",'r') as file:
    API_KEY = file.read()
    file.close()

def getimgURL(kword):
    # image operations
    image = Image(API_KEY)

    # default image search
    image.search()

    # custom image search
    ims = image.search(q=kword,
                 lang='en',
                 response_group='high_resolution',
                 image_type='photo',
                 orientation='horizontal',
                 #category='animals',
                 safesearch='true',
                 order='latest',
                 editors_choice= 'false',
                 page= 1,
                 per_page= 3)

    print(ims['totalHits'])
    print(ims)



    image1 = ims['hits'][0]['largeImageURL']
    return image1


def run():
    kword = get_kword()
    imagex = getimgURL(kword)
    return imagex

img = IMAGE.open(requests.get(imagex, stream=True).raw)


img.save("C:/Users/User/GITHUB/test.jpg")