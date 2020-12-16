import requests
from bs4 import BeautifulSoup
import time

# TODO: Error Handling

def get_archived_releases(pages=1, perpage=5):
    if type(pages) is not list:
        page = [pages]

    rows = []
    for page in pages:
        rows.extend(get_archived_release_page(page=page, perpage=perpage))

    return rows

def get_archived_release_page(page=1, perpage=5, delay=3):
    url = 'https://www.mangaupdates.com/releases.html'

    params = {'act': 'archive', 'page': page, 'perpage': perpage}
    response = requests.get(url, params=params)
    time.sleep(delay)
    soup = BeautifulSoup(response.content, 'lxml')

    main_content = soup.find(id='main_content')
    rows = main_content.select_one('div.p-2.pt-2.pb-2.text > div.row.no-gutters')
    
    # TODO: Use generators instead for better performance
    table_headers = rows.select('div.releasestitle')
    table_entries = rows.select('div.row.no-gutters > div.text')

    rows = []
    num_cols = len(table_headers)
    for i, entry in enumerate(table_entries):
        row_index = i // num_cols
        col_index = i % num_cols
        header = table_headers[col_index].text

        if col_index == 0:      # if new row, create new `rows` element
            rows.append({header: entry.text})
        else:
            rows[row_index][header] = entry.text

    if len(rows[-1]) < num_cols:    # remove extraneous last row
        del rows[-1]

    return rows
