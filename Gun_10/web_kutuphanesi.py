from pprint import pprint
import urllib.request

with urllib.request.urlopen('https://www.kadirblog.com/')
    pprint(response.read())