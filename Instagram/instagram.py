import requests
import time
url = "https://www.instagram.com/api/v1/web/comments/3091081576033527019/add/"

payload='comment_text=new%20comment'
headers = {
  'authority': 'www.instagram.com',
  'accept': '*/*',
  'accept-language': 'es-US,es-419;q=0.9,es;q=0.8,en;q=0.7',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': <cambiar>
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
