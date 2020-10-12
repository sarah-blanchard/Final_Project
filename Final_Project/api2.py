import requests, json


degree_sign= u'\N{DEGREE SIGN}'



def connect():
	full_url = ("http://api.openweathermap.org/data/2.5/weather?zip=32566&units=imperial&us&appid=e4f9c3989f6e3d0f337d8f18c8995bef")
	req = requests.get(full_url)
	wx = req.json()

	try:
		requests.get(full_url)
		wx = req.json()
		print(wx)
		

	except:
			print("An unexpected error has occured, please ensure you have entered the correct zip code and try again")

get_weather()