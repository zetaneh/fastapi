import requests

cookies = {
    '_gid': 'GA1.2.1900003861.1668381943',
    '_gat_gtag_UA_238256076_2': '1',
    '_gat_gtag_UA_216476449_1': '1',
    '_ga': 'GA1.1.151942136.1668381943',
    '_ga_PMD3JBGXGL': 'GS1.1.1668395317.3.1.1668395362.0.0.0',
}

headers = {
    'authority': 'badil.info',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gid=GA1.2.1900003861.1668381943; _gat_gtag_UA_238256076_2=1; _gat_gtag_UA_216476449_1=1; _ga=GA1.1.151942136.1668381943; _ga_PMD3JBGXGL=GS1.1.1668395317.3.1.1668395362.0.0.0',
    'referer': 'https://badil.info/category/info/national/page/2',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

response = requests.get('https://badil.info/wp-json/wp-statistics/v2/hit?_=1668395362&_wpnonce=16f5236071&wp_statistics_hit_rest=yes&referred=https%3A%2F%2Fbadil.info%2Fcategory%2Finfo%2Fnational&exclusion_match=no&exclusion_reason&track_all=1&current_page_type=category&current_page_id=24&search_query&page_uri=/category/info/national/page/2', cookies=cookies, headers=headers)