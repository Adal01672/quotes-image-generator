import requests
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
import os
import random
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)
from PIL import Image, ImageFilter
from name import *
cj=0
ch=int(input("number of quotes to be generated: "))
print("""business
change
charachter
competition
conservative
courage
education
faith
family
famous-quotes
film
freedom
friendship
future
happiness
history
honor
humorous
inspirational
leadership
life
literature
love
motivational
nature
pain
philosophy
politics
power-quotes
religion
science
self
self-help
social-justice
spirituality
sports
success
technology
time
truth
virtue
war
wisdom""")
tag=input("pick a tag name to get quotes: ")
while cj !=ch:
    def lest():
        p=False
        r=requests.get(f'https://api.quotable.io/random?tags={tag}').text
        print(r)
        t=json.loads(r)
        c=t['content']
        with open("db.txt", "r") as f:
            found = any(f"{c}" in x for x in f)
            if found:
                p=True
                print('duplicate found, skipping...')
            else:
                p=False
                with open("db.txt", "a") as f:
                    f.write(c+"\n")

        print(p)
        a=t['author']
        return c,a,p
    c,a,p=lest()


    def get_image():
        
        directory='images'
        images=[]
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                images.append(f)
        t=random.randint(0,12)
        t=images[t]
        return t

    def edit_image():
        #variables for image size
        x1 = 612
        y1 = 612

        #my quote
        sentence = f"{c} -{a}"

        #choose a font
        fnt = ImageFont.truetype('limits.ttf', 30)

        img = Image.open(get_image()).resize((x1,y1))
        img=img.filter(ImageFilter.BLUR)
        d = ImageDraw.Draw(img)

        #find the average size of the letter
        sum = 0
        for letter in sentence:
            sum += d.textsize(letter, font=fnt)[0]

        average_length_of_letter = sum/len(sentence)

        #find the number of letters to be put on each line
        number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
        incrementer = 0
        fresh_sentence = ''

        #add some line breaks
        for letter in sentence:
            if(letter == '-'):
                fresh_sentence += '\n\n' + '-'+letter
            elif(incrementer < number_of_letters_for_each_line):
                fresh_sentence += letter
            else:
                if(letter == ' '):
                    fresh_sentence += '\n'
                    incrementer = 0
                else:
                    fresh_sentence += letter
            incrementer+=1

        print(fresh_sentence)

        #render the text in the center of the box
        dim = d.textsize(fresh_sentence, font=fnt)
        x2 = dim[0]
        y2 = dim[1]

        qx = (x1/2 - x2/2)
        qy = (y1/2-y2/2)

        d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(255,255,255))
        t=False
        img.save(f'quotesimg/{unique_key()}.png')

    if p==False:
        edit_image()
    else:
        print('failed to edit image')
    cj+=1
    
    


