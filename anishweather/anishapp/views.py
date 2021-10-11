from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
from django.shortcuts import redirect



def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid="your api_key here "  '''

        # source contain json data from api

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=bf1e579c03d61f78400bcf1dd1abcf6c').read()

        # converting json data to dictionary

        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data={}
        
    return render(request, "home.html",data)

def home(request):
    return render(request, 'home.html')

def detail(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")    

