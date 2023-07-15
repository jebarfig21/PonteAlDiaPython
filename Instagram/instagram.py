import requests
import time
url = "https://www.instagram.com/api/v1/web/comments/3091081576033527019/add/"

payload='comment_text=new%20comment'
headers = {
  'authority': 'www.instagram.com',
  'accept': '*/*',
  'accept-language': 'es-US,es-419;q=0.9,es;q=0.8,en;q=0.7',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'mid=YXLtcAAEAAHRxTo23AKDUrR4WU2o; ig_did=70B936FB-C037-44A9-8EC4-477DE2461EEA; fbm_124024574287414=base_domain=.instagram.com; datr=li_wYUnJ4gkeaNrGdJzcD3AX; ig_nrcb=1; csrftoken=aPJ4uwN0vaFGcR9Rzl1d8ngpHHpwPFve; ds_user_id=1473380265; sessionid=1473380265%3AFBfwG4uFK3fTjl%3A19%3AAYdhmZE0dqlRMXXc4dbje-9jhxnh1XL6p4qMy49_eg; shbid="3805\\0541473380265\\0541720676849:01f7f41bbb8ab78ebe4a71da994d4e492b4b07428e51e00b77b5c20f29c595c37eafe0fb"; shbts="1689140849\\0541473380265\\0541720676849:01f7bf9b8720d197c77b382117dcb38a96ff6715cd35880b23b6555da271c7afb49c41f1"; dpr=0.5; fbsr_124024574287414=f7qHUGrPiQGAftFJL99yelTnwrvQeNItT6376ekp2K0.eyJ1c2VyX2lkIjoiMTAwMDAwOTI1Njc2MzAwIiwiY29kZSI6IkFRRDN5ZXRFcEdGZXlnOVZDYXJ6dnd5UHZocmoyVHFzXzlpRUVvM2RLS0pUcWdnTzJJU3ViSEFvdFpUVU94bFhPZHcwYW5oak9FRDFfYnQxdU5iQWJXUEFCVGpkMld4WktiMjFFem0xelhKUkVXQjRQN3gwTUNHMHJ4VXJMMUVGU0pUU3hsWDA2Rk1CWlBYdWhqbW5JOHRwei1TaWIzM3JJSE05WC01ZThydVg4X0pUZU0wQ3JMYmlwN09BMnAzS2lBSk1ta1JhbTVieEx1b0RvamUtb0wwWnZHQjhpMlFkMmFpVWV3dVdqc2V6TEFuZklMaG1DNTZBMDVCTHhnaFdBXzY5MVIwODV5ckkwUDV0QV9yakJJYVJyeUdBV0dBejJVby1KTkMzRGRjRkVOUURsLWFJRnhtU1l3b3Vtdk5YaDBKR25MY2l3YUFUeDJucDRVNjRaQlJBIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU5sa2VtTFZWbk1WMFU3VFpDSGhLaElTTlVaQWlwWkJ0TDFTUzlyekphTTlaQk5FR3lBQ0VrQ2p5Z2p3RzV4RGpLbmlmZEpxOEZGdmFqNmcwVG9CbFhvY3RXdXNWSjVQNFpDWkNCQ0ZLVHJiT2xodFVkbDVxWWpxdDZmeFduWVVGUERNNGRRM1lsWkFIa2wyU21xZ2ZMclpBYWdFRDgwVEpScnNneE9xSzdTREtmb1F4bDNhUXdRWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4OTE0MjU4N30; rur="NCG\\0541473380265\\0541720678596:01f7ba770737fec5f3ac957fdffe49c0a7ce0ede9c189ef5028a190a683fc030b409bd54"; csrftoken=aPJ4uwN0vaFGcR9Rzl1d8ngpHHpwPFve; ds_user_id=1473380265; rur="NCG\\0541473380265\\0541720892065:01f765d6b296b1610fb157c22a74c1672cc6cc9e49d200acb0d85575299b97fbbeec8845"',
  'origin': 'https://www.instagram.com',
  'referer': 'https://www.instagram.com/p/CrlulDvO6Tr/?img_index=1',
  'sec-ch-prefers-color-scheme': 'dark',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.198", "Google Chrome";v="114.0.5735.198"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-ch-ua-platform-version': '"13.4.1"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'viewport-width': '1920',
  'x-asbd-id': '129477',
  'x-csrftoken': 'aPJ4uwN0vaFGcR9Rzl1d8ngpHHpwPFve',
  'x-ig-app-id': '936619743392459',
  'x-ig-www-claim': 'hmac.AR0jJlwOc4RY_9GWCVVbWZ0-DS3VJaI1VJ9Wy6ydNKrgNIwK',
  'x-instagram-ajax': '1007825200',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


with open("frases.txt", 'r') as archivo:
    frases = archivo.readlines()

for frase in frases:

    payload='comment_text='+frase
    response = requests.request("POST", url, headers=headers, data=payload)
    time.sleep(20)
    print(response.text)
