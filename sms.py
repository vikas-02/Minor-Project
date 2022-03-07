import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=Alert Motion detected&language=english&route=p&numbers=9346175460"
headers = {
'authorization': "SKgV9pjynw5hzZWu1aoPILlF8kHUCAXc4qBRd3rvNibmGE7Mt0jgUSNmEM1dweaOCTcGRbxW9yVIl56Y",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)