# FooBar API - TechnicalChallenge

## Specification

I would like you to develop a REST API for a fictional client “FooBar Inc”. FooBar Inc need a REST API for accessing House Price Paid Data (PPD).
The raw data can be found, for free, as a CSV file here: https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads.

Acceptance Criteria:
- A list of all records is returned in JSON format via the REST API
- A single record is returned in JSON format when its ID is provided
- A list of purchase records made in a specified time range is returned in JSON format
when a date time range is provided

## Solution - Django framework

I used Django framework for the solutions, because it very useful and.
https://www.djangoproject.com/

### Used extra modules:

- rest_framework
- django_filters

## Get data

## Setting on local environment

I downloade data in csv from this page:
https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads.

### Requirements

- Python 3.8 or greater
- django, djangorestframework, django-filters

### Steps

1. Get the code from the repository and go into the directory

2. Set virtualenv (It not necessary, but I think this is a good practice)
   Iy you haven't got, please install:
   `pip3 install virtualenv`

3. Activate virtual environment: `source venv/bin/activate`

4. Install necessarry packages with pip:
   `pip install django djangorestframework, django-filters`

5. Run migration:
   `./managepy migrate`

If you want to leave virtual environment, jus this: `deactivate`

For this project I used SQLite3 (django default) database system, but you can use anything (MySQL, Postgres) if you want.
Currently I pushed a little imported (11612 record) databse, but it not the best practice. Please use a tool or script to
csv import.

## Authentication

In this case it isn't in the requirements, but if we want to use Authentication or user management the best way the dajnago rest framework's default.

Installation: \
`pip install djangorestframework_simplejwt`

Add to settings (to settings.py):\
`REST_FRAMEWORK = { 'DEFAULT_AUTHENTICATION_CLASSES': [ 'rest_framework_simplejwt.authentication.JWTAuthentication', ], }`

And set urls (urls.py):\
`from django.urls import path`\
`from rest_framework_simplejwt import views as jwt_views`

`urlpatterns = [ # Your URLs... path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'), path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), ]`

Use in the views example:

`from rest_framework.permissions import IsAuthenticated`\

`class HouseListView(APIView): `\
 `permission_classes = (IsAuthenticated,)`

For all information visi these: \
https://github.com/jazzband/django-rest-framework-simplejwt \
https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html

## Logging

If the application is grow, the logging is very important. Fortunately Django has a great solution for this problem.
Logging in Django it very simple, just need to be set in the settings.py.

Example:

```
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

```

And usage:

```
# Log an error message
logger.error('Something went wrong!')

```

And here is the offitial documentation:\
https://docs.djangoproject.com/en/3.1/topics/logging/

And also we have many other option to logging, for example:

- elk (Elastic search, Logstahs, Kibana)
- Splunk
- Sentry (It easy to set in Django)

And maybe it will be good idea, if we connect with a monitoring and alert tool. Some example:

- Sentry
- Prometheus
- Merticly

## Caching

If we need many quick requests, and need search fastly, the best way if we use any indexing, caching solutions:

- Redis
- Simple database cache (sometimes is more than enough)
- Django has an own solution memcached:
  https://docs.djangoproject.com/en/3.1/topics/cache/

## Models

### House

The house model represents the PPD which can be available to sell.

I used similar field whic are mentioned it this page:

https://www.gov.uk/guidance/about-the-price-paid-data#explanations-of-column-headers-in-the-ppd

So my model fields are the following:

- transaction_identifier
- price
- date_of_transfer
- postal_code
- property_type
- old_new
- duration
- paon
- saon
- street
- locality
- town
- district
- country
- ppd_cat
- record_stat
- currency
- created_at

## API - Available endpoints:

### Swagger

I used Django Rest Framework, so the swagger it's implemented.

<img width="1405" alt="Screenshot 2021-04-09 at 9 15 54" src="https://user-images.githubusercontent.com/5425780/114145124-63586600-9916-11eb-8c94-098c1c56ac5b.png">


### List all PPD with pagination (pagination has been set int the settings)

#### [GET] api/houses/

Result example:

JSON Result example:
`[{"transaction_identifier": "{BC8936BC-0425-0E2C-E053-6C04A8C0DBF4}", "price": "735000", "date_of_transfer": "2021-01-08 00:00", "postal_code": "SE12 8QH", "property_type": "T", "old_new": "N", "duration": "F", "paon": "11", "saon": null, "street": "AISLIBIE ROAD", "locality": null, "town": "LONDON", "district": "LEWISHAM", "country": "GREATER LONDON", "ppd_cat": "A", "record_stat": "A"},{...}]`

### Get a PPD by id (primary key)

#### [GET] api/houses/1 with ID in request, but it just the primary key

JSON Result example:
`[{"transaction_identifier": "{BC8936BC-0425-0E2C-E053-6C04A8C0DBF4}", "price": "735000", "date_of_transfer": "2021-01-08 00:00", "postal_code": "SE12 8QH", "property_type": "T", "old_new": "N", "duration": "F", "paon": "11", "saon": null, "street": "AISLIBIE ROAD", "locality": null, "town": "LONDON", "district": "LEWISHAM", "country": "GREATER LONDON", "ppd_cat": "A", "record_stat": "A"}]`

### Get a PPD by transaction identifier

#### [GET] api/houses?transaction_identifier\_\_iexact= ...

Example request: api/houses?transaction_identifier\_\_iexact={BC8936BC-0425-0E2C-E053-6C04A8C0DBF4}

### Get a PPD by filtered with purchase range (used date_of_transfer field)

#### [GET] api/houses?drange=...

Example request: api/houses?drange=2021-01-08%2000:00\*2021-01-08%2000:00
Two date separated by '\_'

### Add a record

#### [POST] api/houses/add

Exaple request body:
`{ "transaction_identifier": "", "price": "", "date_of_transfer": "", "postal_code": "", "property_type": "", "old_new": "", "duration": "", "paon": "", "saon": "", "street": "", "locality": "", "town": "", "district": "", "country": "", "ppd_cat": "", "record_stat": "" }`

Necessary request header: Content-Type: application/json
