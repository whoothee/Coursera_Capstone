# import requests
# from bs4 import BeautifulSoup



# client_ID = 'UXWEDPWPTWEWH0YVOCWCCOTR11CTY25TK3OPNALHQMN2YFEN'
# client_secret = 'D5Q2RYDAXAIGCI3O5SHQNZ4O15HJGQYXYFYAPXT3SB1P2VI4'
# url = 'https://api.foursquare.com/v2/venues/explore?'
# my_credential = client_ID +'&' + client_secret + '20200802'
# location ='&||=40.73,-74.01&'



# res = requests.get(url+my_credential+location+'query=cofee').json()
# print(res)


import geocoder # import geocoder

# initialize your variable to None
#lat_lng_coords = None
postal_code = 'M8Z'
# loop until you get the coordinates

g = geocoder.google('{}, Toronto, Ontario,Canada'.format(postal_code))
lat_lng_coords = g.latlng

latitude = lat_lng_coords[0]
longitude = lat_lng_coords[1]

print(latitude,longitude)


