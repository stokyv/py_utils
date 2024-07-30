import time
import requests
import json
import os
from bs4 import BeautifulSoup

from common import *
from models import *
from mongo_queue import MongoQueue

mongo_queue = MongoQueue('business', 'guland')
mongo_queue.update_connection_type('local')




async def fetch_data(lat, lon, province_id):
    """
    Send a GET request to Guland API to retrieve information about thua dat.
    Return a dictionary of data if request is successful or None if not
    Args: 
        lat, lon of position. Floats or strings.
        province_id: a str of length 2
    """
    if type(lat)==float:
        lat = str(lat)
    if type(lon)==float:
        lon = str(lon)
    assert type(province_id) == str
    assert len(province_id) == 2

    # province_id = '01' #hanoi

    url = 'https://guland.vn/get-bound-2'
    params = {
        'marker_lat': lat,
        'marker_lng': lon,
        'province_id': province_id
    } 
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'is_show_free=eyJpdiI6IjE1aEYxaytJMnhBWTNYa2s5Vi83U2c9PSIsInZhbHVlIjoiT1dCeXJLSWJCREdpTDlWZ3NLUkVkSEduTGcrL0IwZkRvbVNoYW10bWxsUHZBdHNsbFRoQmFYd1N0MzJZVmJHRVFraXVaejNYSTZ3RzN0djJBQ0JaMGc9PSIsIm1hYyI6ImMxNGE5ODZkNGZhZTAzNDkwMjNlZTliNDUxNjgzMDRiMTA2ZDZhYjVjZDk5NDQ4ZWMyYzIwMjEwYTFkYWE1NzYifQ%3D%3D; affiliate_phone=eyJpdiI6IldkMGNqRWh2VDJoeVc3U3pHYWp6SWc9PSIsInZhbHVlIjoiejFVOVA3d2M3eHVENzlVaS9tU1pYVWRJQWZvUHY0dXVaakFKRStYOGZVblRyWEczN2RNcU9XQ1VhQnMvVVUvdVVPYUVUOXp4am1CWEpaWTlwSjFwQVE9PSIsIm1hYyI6IjRhNjkyYzYxZTdlNWUxZWJiYzU2YjI3Y2E3OTIwNDViNzA0MjhiZWVhNGQ0YzRmYzg3NmE0M2Q2ZmU0MjlhNzUifQ%3D%3D; affiliate_id=eyJpdiI6IjRVWkxWVDNpcmI2RDRqYldLNDd1MGc9PSIsInZhbHVlIjoiL0JIeVdiMmxWQ2ZJcjdoVjlYWUZpTDhoTzdBTGJZUVljY2dOL3Z4dnpCZHJubW1TWlJGUEg4MHduVnIrMVUrWCIsIm1hYyI6IjkzNmU3ZWJiODlhNmY1YTYzODk0ZTY4MTA2OTNjNzA1NGFjYzUzYjVkYzE0YmU2ZDIzNGJmZTcwNzcwM2ZkZDgifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IkVtWkUvQVY0a21NNmpxV252SlNVTnc9PSIsInZhbHVlIjoibzc3S1dVc2FwT2d2VzlUM29SMU1rbUZGWlZQN2RETzRzT0o3NVBSVDlUYU1yWnJjMVZGaDhoL1oxbTRDRUxFczBya3Q0VFFkZHNYRXYzRjMyalIvdFp1WmdMT3pvSWZYdXZSdWtlSm9RK1kydWNzbG02cm9jR2lvalBSMytQSFIiLCJtYWMiOiI5ZDg3ZjQzODNiZjdlMTg1MmVlMjU5N2M0YTc4NTFmYzNhNzM1MzBkODc3MzAyY2RkM2ZhYjA1M2Q5Y2JkNTkxIn0%3D; laravel_session=eyJpdiI6IlNvcmI2aXJWdG42MEZ4S08rL0E1Vmc9PSIsInZhbHVlIjoiTHU2bnhYMGRkbFl0a2dHZWxNRlhjNHhSdHZTV25uK0VnZTl2ajdPRU14ekNyck9rQzd1c00zM21lUlRFR0dBelY3bnN5SXE3UmV4S1ROUTkxRFE0NkFXN20xY251aFlMWi8zN2txZzhhWHU4QWpWZTZtL0NLMGpaRDVjQ3NycGwiLCJtYWMiOiI4Nzc4YjA5ZGJjODM2MTM0NjkwY2Y3M2RiNzZlYWU2MDNlMzRiZWVmODI0MzM3MDc1NTY0NDAyMTYyZWQzOTYxIn0%3D',
        'DNT': '1',
        'Host': 'guland.vn',
        'Referer': 'https://guland.vn/soi-quy-hoach',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        # 'X-CSRF-Token': 'LhjdMtU8PdRlQfVntxVJb6orlj6YltppGjD53MaN',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        return response.json()
    except requests.exceptions.RequestException as e:
        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 60))
            print(f"Rate limit exceeded. Retrying in {retry_after} seconds...")
            time.sleep(retry_after)
            return await fetch_data(lat, lon, province_id)


async def process_data(response_data):
    data = {}
    if not response_data:
        return None
    data['status'] = response_data.get('status', None)
    data['points'] = response_data.get('points', None)
    data['address'] = response_data.get('address', None)
    data['id'] = response_data.get('id', None)
    data['province_id'] = response_data.get('province_id', None)
    data['district_id'] = response_data.get('district_id', None)
    data['ward_id'] = response_data.get('ward_id', None)
    data['so_to'] = None
    data['so_thua'] = None
    data['dien_tich'] = None

    pattern = r"Thửa (\d+), tờ (\d+). Diện tích: (\d+\.\d+\w+)"
    match = re.match(pattern, data['address'])
    if match:
        data['so_thua'], data['so_to'], data['dien_tich'] = match.groups()
    else:
        pattern = r"Diện tích: (\d+\.\d+\w+)"
        match = re.match(pattern, data['address'])
        if match:
            [data['dien_tich']] = match.groups()
    return data

def add_to_mongo(mongo_queue, data):
    # only add if data has id:
    mongo_queue.insert_one(data)

async def test():
    p2_lat, p2_lon = 21.001349250803205, 105.8439561724663
    province_id = '01' #ha noi
    results = []

    lat, lon = p2_lat, p2_lon #hanoi

    for i in range(50):
        response_data = await fetch_data(lat, lon, province_id)
        data = await process_data(response_data)
        # results.append(data)
        lat += 0.001
        lon += 0.001
        if data != None:
            if data['id'] != None:
                # if data['so_to'] != None:
                #     str_so_to = str(data['so_to'])
                #     while len(str_so_to) < 3: str_so_to = '0' + str_so_to
                #     str_so_thua = str(data['so_thua'])
                #     while len(str_so_thua) < 4: str_so_thua = '0' + str_so_thua
                #     temp_url = str(data['ward_id']) + str_so_to + str_so_thua
                #     if await mongo_queue.check_url_exists_in_db(temp_url) == False:
                #         await mongo_queue.add_queue_weburl_if_available([temp_url])
                #     await mongo_queue.update_crawled_weburl(temp_url, status_code=True, data=data)
                # else:
                    temp_url = str(data['ward_id']) + str(data['id'])
                    if await mongo_queue.check_url_exists_in_db(temp_url) == False:
                        await mongo_queue.add_queue_weburl_if_available([temp_url])
                    await mongo_queue.update_crawled_weburl(temp_url, status_code=True, data=data)

    # print(results)
    return results

if __name__ == '__main__':
    import asyncio
    asyncio.run(test())