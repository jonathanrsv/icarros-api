import requests

api_url = "https://paginasegura.icarros.com.br/rest/"

def search_cars(search):
	request_url = api_url + "search/deals/rai_10.1-esc_2.1-sta_1.1/0/20/1?includeAMDeals=true&openSearch={search}"
	formated_url = request_url.format(search=search)
	data_response = requests.get(formated_url)
	return data_response.json()['deals']


