import json
import os
import subprocess
import sys
import urllib


def localsearch(search_keywords):
    search_result_filepaths = [0]*2000
    search_result_filenames = [0]*2000
    i = 0
    for root, dirs, files in os.walk('../../../../'):
        for file in files:
            if search_keywords in file:
                print(file + ' and ')
                # Getting full path of the file
                print(os.path.join(root, file))
                filepathh = os.path.join(root, file)
                search_result_filenames[i] = file
                search_result_filepaths[i] = filepathh
                i += 1
    return search_result_filepaths, search_result_filenames


def open_file_in_default_application(file_path):
    subprocess.call(["xdg-open", file_path])


def google_search(text):
    url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDKXPuaXh84T_tVVQcxQdbQS8TzNk2uuuU%20&cx=017576662512468239146:omuauf_lfve&q="
    words_to_search = text.split()
    search_keywords = ""
    for word in words_to_search:
        search_keywords += word + '+'
        url = url + search_keywords
    print("URL is : " + url)
    response = urllib.request.urlopen(url)
    content = response.read()
    data = json.loads(content.decode("utf8"))
    for i in data['items']:
        print(i['title'])
        print(i['link'])
        print(i['snippet'])
    return data
