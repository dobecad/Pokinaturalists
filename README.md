# Pokinaturalists

Pokinaturalists is a web application written using the Django python framework. This application displays interesting animal, insect, and plant data that are within an area around the user's location. The user will be able to capture these creatures to add to their collection. The user will also be able to battle other creatures or other players in battles. 

# Requirements
- Python 3.6+
- Heroku account
- iNaturalist Account and Registered Project

# Current Functionality
Pokinaturalist is currently able to extract user IP address when they connect to the web server, and request access to the GPS functionality of the user's device. From there, Pokinaturalist can track the user's position and display their longitude and latitude coordinates.

# Installation
```bash
cd Pokinaturalists/Pokinaturalists/
pip -r requirements.txt
```

# Deployment
### Ensure all environment variables are set on the Heroku Deployment page. Such variables will include:
- SECRET_KEY - Django's secret key

```bash
# If deploying locally
python manage.py runserver

# If deploying to heroku. Make sure to add the heroku app URL to the ALLOWED_HOSTS variable 
# in the settings.py in the Pokinaturalists directory.
git push heroku main
```