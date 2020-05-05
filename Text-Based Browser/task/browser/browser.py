import collections
import os
import requests
import sys
from bs4 import BeautifulSoup
from colorama import init, Fore
init(autoreset=True)

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def open_page(path, url):
    filename = path + '/' + url + '.txt'
    if not os.path.exists(filename):
        print("Error: Incorrect URL")
    else:
        with open(filename) as infile:
            print(infile.read())


def save_page(path, url, text):
    index = url.rfind('.')
    filename = path + '/' + url[0:index] + '.txt'
    with open(filename, 'w') as outfile:
        outfile.write(text)
    return url[0:index]


def get_page(url):
    if url.find('https://') < 0:
        url = 'https://' + url
    r = requests.get(url)
    return r.text


def parse_page(text):
    text_list = []
    tags = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
    soup = BeautifulSoup(text, 'html.parser')
    for tag in soup.find_all(tags):
        text = tag.get_text()
        if tag.name == 'a':
            text = Fore.BLUE + text
        text_list.append(text)
    return '\n'.join(text_list)


# write your code here
path = '.'
if len(sys.argv) > 1:
    # create directory
    directory = sys.argv[1]
    if not os.path.exists(directory):
        os.mkdir(directory)
    path = directory

history = collections.deque()
previous_page = ''
current_page = ''

while True:
    if current_page != previous_page:
        history.append(previous_page)
        previous_page = current_page
    url = input()
    if url == "exit":
        break
    elif url == "back":
        if history:
            current_page = history.pop()
            open_page(path, current_page)
    elif url.rfind('.') < 0:
        current_page = url
        open_page(path, current_page)
    else:
        text = parse_page(get_page(url))
        print(text)
        current_page = save_page(path, url, text)
