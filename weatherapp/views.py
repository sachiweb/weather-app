import json  
from django.shortcuts import render  
import urllib.request  
import json  
  
# Create your views here.  
  
def base(request):  
    if request.method == 'POST':    
        city = request.POST.get('city', 'True')  
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=356fc53cef44650879bd46581128a8da').read()  

        list_of_data = json.loads(source)  
  
        context = {  
            'city': city,  
            "country_code": str(list_of_data['sys']['country']),  
            "coordinate": str(list_of_data['coord']['lon']) + ' '  
                            + str(list_of_data['coord']['lat']),  
            "temp": str(list_of_data['main']['temp']) + '°C',  
            "pressure": str(list_of_data['main']['pressure']),  
            "humidity": str(list_of_data['main']['humidity']),
            "icon":str(list_of_data['weather'][0]['icon']), 
            "main":str(list_of_data['weather'][0]['main']),
            "clouds":str(list_of_data['clouds']['all'])
        }  
    else:  
        context = {}  
      
    return render(request, 'base.html', context)  

# # Create your views here.

# def weather(request):
#     if request.method == 'POST':
#         city=request.POST.get('city','true')
#         source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=356fc53cef44650879bd46581128a8da').read()
#         list_of_data=json.loads(source)
#         data = {
#             'city': city,  
#             "country_code": str(list_of_data['sys']['country']),  
#             "coordinate": str(list_of_data['coord']['lon']) + ' '  
#                             + str(list_of_data['coord']['lat']),  
#             "temp": str(list_of_data['main']['temp']) + 'k',  
#             "pressure": str(list_of_data['main']['pressure']),  
#             "humidity": str(list_of_data['main']['humidity']),  
#             # "city":city,
#             # "description":str(list_of_data['weather'][0]['description']),
#             # "coordinate":str(list_of_data['coord']['lon'])+ ','
#             # + str(list_of_data['coord']['lat']),
#             # # "main":str(list_of_data['weather'][0]['main']),
#             # # "temp":str(list_of_data['main']['temp']) +' °C',
#             # # "humidity":str(list_of_data['main']['humidity']),
#             # # "countrycode":str(list_of_data['sys']['country']),
#             # # "icon":str(list_of_data['weather'][0]['icon']),
#             # "time":str(list_of_data['sys']['timezone'])

#         }
        
#     else:
#         data={}
#     return render(request,"index.html",data)
   
