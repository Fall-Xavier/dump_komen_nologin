import re, requests, bs4, json
from bs4 import BeautifulSoup as parser
ses=requests.Session()
id = []
#idt = "me"
#token = "EAAGNO4a7r2wBAN2lSnt4pPKSiqocPWk7hoQFF5lPhHenC8u9YZBZBvbcSGqzVZAF60ao7iNE4GhCvUQGZBxcFpKk92zE5z4kYYZC68FIMkjuFSyh3iERInwJm9enSAbeHNNZCJKObyzqeH7ZBoJax8dCPiyOEqs3YyAjIi8yxaDjZB2LLZAiHLT9p"
#cookie = {"cookie":"datr=0pGdYhiYB7hsj1JBrjTBi4ux;sb=0pGdYpBPSM42TJ7oAgaU4GaO;locale=id_ID;m_pixel_ratio=3;dnonce=AWlQ57AlpQk8E69TYADwIyUIuTwU8PUzRW0vKVfWiMuKmYZ8oBMn5LYc9jpjkpqmtrpXt87T6nUS4fK9OsO0LiJF;fr=03QbEnxNEoyNmqDTN.AWUyLqqdoRDp4rBJJGG7M6lvTXo.BinZHS.yS.AAA.0.0.Bin1XH.AWXn49V4tYc;c_user=100080709721804;xs=39%3A3B83EwZcC8TEww%3A2%3A1654609352%3A-1%3A10903;wd=360x667;"}
def menu():
	idt = input("masukan id post : ")
	url = "https://mbasic.facebook.com/"+idt
	get_komen(url)
	
def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):uid = ids.get("href").split('=')[1].replace("&refid","")
			else:uid = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if uid+"<=>"+nama in id:pass
			else:id.append(uid+"<=>"+nama);print(uid+"<=>"+nama)
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			get_komen("https://mbasic.facebook.com"+z["href"])

menu()