import requests
import json
from bs4 import BeautifulSoup as BS
import time

disciplines = [
        # 'astronomy',
        'geology',
        'gyroscope',
        'literature',
        'marketing',
        'mathematics',
        'music',
        'polit',
        'agrobiologia',
        'law',
        'psychology',
        'geography',
        'physics',
        'philosophy',
        'chemistry',
        'estetica'
    ]

# page = 'astronomy'

for page in disciplines:
    for i in range(1, 1001):
        r = requests.get("https://yandex.ru/referats/?t=" + str(page) + "&s=" + str(i))
        # "https://yandex.ru/referats/?t=astronomy&s=1"
        html = BS(r.content, 'html.parser')

        discipline = html.select(".referats__text > div")[0].get_text()
        title = html.select(".referats__text > strong")[0].get_text()
        content = html.select(".referats__text > p")
        title = title.replace("Тема: «", "")
        title = title.replace("»", "")
        discipline = discipline.replace("Реферат", "Статья")

        referat = list('')
        for p in content:
            referat.extend(list(p))

        paragraphsCount = len(referat)

        discipline = str(discipline)
        referat = str(referat)
        referat = referat.replace("['", "<p>")
        referat = referat.replace("']", "</p>")
        referat = referat.replace("', '", "</p><p>")

        url = "http://127.0.0.1:8000/api/randomtext/list/"

        payload = json.dumps({
          "discipline": discipline,
          "discipline_id": page,
          "subject": str(title),
          "article": referat,
          "number_ext": i,
          "paragraphs": paragraphsCount
        })
        headers = {
          'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(i, response.text)
        i += 1
    sleep = 60
    print('Я заснул на ', str(sleep), ' сек.')
    time.sleep(sleep)

