import collections
import os
import sys

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
        if url == "bloomberg.com":
            text = bloomberg_com
        elif url == "nytimes.com":
            text = nytimes_com
        else:
            print("Error: Incorrect URL")
            continue
        print(text)
        current_page = save_page(path, url, text)
