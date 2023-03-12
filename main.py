
import webbrowser

import requests

if __name__ == '__main__':
    urlPage = input("Podaj stronę internetową: ")
    A = [20100101,20150202,20200303]
    for number in range(len(A)):
        url = "http://archive.org/wayback/available?url=" + urlPage + "&timestamp=" + str(A[number])
        response = requests.get(url)
        d = response.json()
        page = d["archived_snapshots"]["closest"]["url"]
        webbrowser.open(page)
