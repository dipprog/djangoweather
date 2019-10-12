# View file to view our templates
from django.shortcuts import render
def home(request):
    import json
    import requests
    api_key = # "your airnow api key"
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=" + api_key )
        try:
            api_content = json.loads(api_request.content)
        except Exception as e:
            api_content = "Error..."

        if (api_content[0]['Category']['Number'] == 1):
            category_color = "good"
        elif (api_content[0]['Category']['Number'] == 2):
            category_color = "moderate"
        elif (api_content[0]['Category']['Number'] == 3):
            category_color = "usg"
        elif (api_content[0]['Category']['Number'] == 4):
            category_color = "unhealthy"
        elif (api_content[0]['Category']['Number'] == 5):
            category_color = "veryunhealthy"
        elif (api_content[0]['Category']['Number'] == 6):
            category_color = "hazardous"

        return render(request, 'home.html', {'api_content': api_content,'category_color': category_color })
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=" + api_key )        
        try:
            api_content = json.loads(api_request.content)
        except Exception as e:
            api_content = "Error..."

        if (api_content[0]['Category']['Number'] == 1):
            category_color = "good"
        elif (api_content[0]['Category']['Number'] == 2):
            category_color = "moderate"
        elif (api_content[0]['Category']['Number'] == 3):
            category_color = "usg"
        elif (api_content[0]['Category']['Number'] == 4):
            category_color = "unhealthy"
        elif (api_content[0]['Category']['Number'] == 5):
            category_color = "veryunhealthy"
        elif (api_content[0]['Category']['Number'] == 6):
            category_color = "hazardous"

        return render(request, 'home.html', {'api_content': api_content,'category_color': category_color })

def about(request):
    return render(request, 'about.html', {})