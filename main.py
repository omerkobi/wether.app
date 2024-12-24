import streamlit as st
import requests as re
print('I was here')
print('hello')
print('say hello my friend')
######### streamlit ###########
#st.markdown('''
#Title 
##subtitle

#-bullet1
#-bullet2
#bullet3

#> Amazingv quote :
#''')

#st.radio("Which desert is better?", ["cake","ice cream","Pie"])

################## API ##################
categories_url = 'https://api.chucknorris.io/jokes/categories'
response = re.get(categories_url)
response.raise_for_status() # 200 ok
print(response.text)

########## Using jason ##########
import  json
categories = json.loads(response.text)
print(type(categories))

#### Shorter way using json ######
print(response.json())
print(response.json()[1])


def get_chuck_norris_joke_by_category(category):
    url = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = re.get(url)
    response.raise_for_status()
    return response.json()


# Try categories like 'animal', 'career', 'celebrity'
joke_dict = get_chuck_norris_joke_by_category('animal')
# print(joke_dict)
print(joke_dict['value'])

obj = [{}, 1,2,3, ["abc"], {"name": "moshe"}]
type(obj)  # list
result = json.dumps(obj)
print(type(result), repr(result))


### requasting wether

url = "https://catfact.ninja/fact"
response = re.get(url)
print(response.json().keys())
print(response.json()['fact'])


fred_key = '25af470e22d07300c84e19895ed91600'
data_type = "CPIAUCSL"
url = f'https://api.stlouisfed.org/fred/series/observations?series_id={data_type}&api_key={fred_key}&file_type=json&units=chg'
fred = re.get(url)
print(fred.text)
#print(fred.json())