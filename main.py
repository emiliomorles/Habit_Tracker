import requests
from datetime import datetime

TOKEN = "YOUR PASSWORD"
USERNAME = "YOUR USERNAME"
ID = "graph1"
DAY_DEC_16 = "20231216"
DAY_DEC_15 = "20231215"

# ------------------- Create my pixela account ------------------------> Call /v1/users API (https://pixe.la/)

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
 }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ------------------- Create a graph definition ------------------------> /v1/users/<username>/graphs

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Basketball Graph",
    "unit": "commit",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ------------------- Get the graph! ------------------------>
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph ! This is also /v1/users/<username>/graphs/<graphID>

# ------------------- Post value to the graph ------------------------> Call /v1/users/<username>/graphs/<graphID>
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

formatted_today = datetime(year=2023, month=12, day=14)
# print(formatted_today.strftime("%Y%m%d"))


post_data = {
    "date": formatted_today.strftime("%Y%m%d"),
    "quantity": "9.6",  # I can change the 'value' into: input("How much effort did you do today?")
 }

# response = requests.post(url=post_endpoint, json=post_data, headers=headers)
# print(response.text)

# ------------------- Browse again! ------------------------> Browse
# https://pixe.la/v1/users/a-know/graphs/test-graph, again!

# ------------------- Update one data point ------------------------> PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# https://docs.pixe.la/entry/put-pixel

edit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DAY_DEC_16}"

edit_data = {
    "quantity": "5.29",
 }

# response = requests.put(url=edit_endpoint, json=edit_data, headers=headers)
# print(response.text)

# ------------------- Delete one data point ------------------------>
# DELETE - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

eliminate_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DAY_DEC_15}"

response = requests.delete(url=eliminate_endpoint, headers=headers)
print(response.text)