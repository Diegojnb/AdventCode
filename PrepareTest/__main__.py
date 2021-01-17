from urllib.request import *
import requests
import urllib
import os

def create_dir(path):
    if(not os.path.isdir(path)):
        os.mkdir(path)

def download_html_page(year,day):
    url = 'https://adventofcode.com/' + year + '/day/' + day
    return download_page(url)

def download_input_page(year,day):
    url = 'https://adventofcode.com/' + str(year) + '/day/' + str(day) + '/input'
    return test_download(url)

def download_page(url):
    try:
        response = requests.get(url,headers = get_headers())
        return response
    except Exception as e:
        print (url)
        print (e)

def get_headers():
    return {'authority': 'adventofcode.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'es-ES,es;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.2.628325036.1608645785; session=53616c7465645f5fb448c2b8913fa1f01cc5f4ddd114203bb7874b40e6e9f27d97976d0c2c011bcf7d69a3b7d9731fd9; _gid=GA1.2.1333595893.1610786678',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.465'}

def test_download(url):
    response = requests.get(url,headers = get_headers())
    return response

def create_file(file_name,content):
    if content is not None:
        f = open(file_name, "w")
        f.write(content.content.decode("utf-8"))
        f.close()

def create_empty_file(file_name):
    f = open(file_name, "w")
    f.close()

def download_day_page(path,year,day):
    content_html_page = download_html_page(year,day)
    create_file(path + "/page.html",content_html_page)
    content_input_page = download_input_page(year,day)
    create_file(path + "/input.txt",content_input_page)

def __main__():
    current_path = os.getcwd()
    try:
        for year in range(2018, 2021):
            str_year = str(year)
            year_path = current_path + "/" + str_year
            create_dir(year_path)
            for day in range(1,26):
                str_day = str(day)
                day_path = year_path + "/" + str_day
                print(day_path)
                create_empty_file(day_path + "/__main__.py")
                # create_dir(day_path)
                # download_day_page(day_path,str_year,str_day)
    except OSError:
        print ("Creation of the directory %s failed" % current_path)
    else:
        print ("Successfully created the directory %s " % current_path)
    pass

__main__()
