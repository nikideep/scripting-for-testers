#Problem description
#Find out if there are any duplicate urls used in the
#json placeholder photo data

import requests

url = 'https://jsonplaceholder.typicode.com/photos'

#get the data about the photos
response = requests.get(url)

#read that data into a variable  
json_data = response.json()

#create a list for storing the url of each photo
url_list = []
for photo in json_data:
  url_list.append(photo['url'])
  print(photo['url'])
print(type(photo))
print(type(photo['url']))
assert len(url_list)==5000,"length is not 5000"
#print the length of the list
print("the length of the List is:\n",len(url_list))
#convert the list to set to find the duplicatae urls
conv_1 = set(url_list)
assert len(conv_1)<5000,"no duplicates found"
print("The length of the list after removing duplicate url:\n",len(conv_1))
