import requests
from lxml import html
from urllib.parse import urlparse
from urllib.parse import urljoin
import collections
from urllib.request import urlopen
import urllib.request
import re
from collections import Counter
import time
from threading import Thread

how = int(input())
start = time.time()

WIKI_RANDOM = "https://ru.wikipedia.org/wiki/Special:Random"
WIKI_DOMAIN = "https://ru.wikipedia.org"

response = urlopen(WIKI_RANDOM)
response_bytes = response.read()
urls_queue = collections.deque()
urls_queue.append(WIKI_RANDOM)
found_urls = set()
found_urls.add(WIKI_RANDOM)
txt = response_bytes.decode("utf8")
words = list(map(lambda s: s.lower().strip(), filter(lambda s: s.isalpha(), txt.split())))
urls = re.findall(r'href=[\'"]?([^\'" >]+)', response_bytes.decode("utf8"))
filtered_urls = filter(lambda url: url.startswith('/wiki/'), urls)
corrected_urls = map(lambda url: WIKI_DOMAIN + url, filtered_urls)
response = urlopen(WIKI_RANDOM)
response_bytes = response.read()

def counter(words):
    count = {}
    for element in words:
        if count.get(element, None):
            count[element] += 1
        else:
            count[element] = 1
    sorted_values = sorted(count.items(), key=lambda tpl: tpl[1], reverse=True)
    return dict(sorted_values)


for i in range(how):
    WIKI = next(corrected_urls)
    response = urlopen(WIKI)
    response_bytes = response.read()
    urls_queue = collections.deque()
    urls_queue.append(WIKI)
    found_urls = set()
    found_urls.add(WIKI)
    txt = response_bytes.decode("utf8")
    new_words = list(map(lambda s: s.lower().strip(), filter(lambda s: s.isalpha(), txt.split())))
    count = counter(new_words)


    with open("urls", "a", encoding = "utf-8") as file:
        file.write(WIKI + '\n')


    f = str("words" + str(i) + ".txt")
    with open(f, "w", encoding = "utf-8") as file:
            for key,value in count.items():
                file.write(f'{key} {value}\n')


all_words = {}
counter_lines = 0
for j in range(10):
    file_name = "words" + str(j) + ".txt"
    with open(file_name, encoding= "utf-8") as file:
        for line in file:
            key, value = line.split()
            if key in all_words:
                all_words[key] += int(value)
            else:
                all_words[key] = int(value)
                counter_lines += 1


with open("all_words.txt", "w", encoding="utf-8") as file:
    for key, value in all_words.items():
        file.write(f'{key} {value}\n')


end = time.time()
print(end - start)
