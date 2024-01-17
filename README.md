# DRF Level 1

The test consists in creating a Web API Project for a JobBoard website. Similar to indeed.com, companies will be able to create and publish new job offers that people will then be able to see.

Clients will be able to communicate with our Web API from 2 URL Endpoints:

- `api/jobs/` - accepts GET and POST methods, allowing to create new instances and retrieve a list with all the available job offer instances.

- `api/jobs/<int:pk>/` - accepts GET, PUT and DELETE, allowing a user to retrieve, update or delete an object instance.

You can choose if you want to write the project views using the `@api_view` decorator or the `APIView` class, and you can also choose to write the necessary Serializer using the homonym class or the `ModelSerializer` class instead.

What really matters is for you to have understood the respective advantages and disadvantages of the different options available... everything else is about your coding style and preferences!

You will not need to build an authentication system for this specific API, as that is a more advanced topic we will discuss together in the next sections of the course!

## Model

In the project, you will need to create a model called `JobOffer` with the following fields:

- `company_name`: A string representing the name of the company.
- `company_email`: A string representing the contact email of the company.
- `job_title`: A string representing the title of the job offer.
- `job_description`: A text field that describes the job offer.
- `salary`: A decimal field to represent the salary for the job offer.
- `city`: A string representing the city in which the job is located.
- `state`: A string representing the state in which the job is located.
- `created_at`: A datetime field that captures the time the job offer was created.
- `available`: A boolean field indicating whether the job offer is still available.

## Requirements
```
asgiref==3.7.2
Django==5.0.1
djangorestframework==3.14.0
pytz==2023.3.post1
sqlparse==0.4.4
typing_extensions==4.9.0
```

## App Setup Instructions
I think it will never happen, sorry :(
<!-- TODO: Add app setup instructions here -->

