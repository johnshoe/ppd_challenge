# FooBar API - TechnicalChallenge

## Django framework

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

## Available endpoints:

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
