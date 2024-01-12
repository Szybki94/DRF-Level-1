# DRF Level 1

The test consists in creating a Web API Project for a JobBoard website. Similar to indeed.com, companies will be able to create and publish new job offers that people will then be able to see.

Clients will be able to communicate with our Web API from 2 URL Endpoints:

- `api/jobs/` - accepts GET and POST methods, allowing to create new instances and retrieve a list with all the available job offer instances.

- `api/jobs/<int:pk>/` - accepts GET, PUT and DELETE, allowing a user to retrieve, update or delete an object instance.

You can choose if you want to write the project views using the `@api_view` decorator or the `APIView` class, and you can also choose to write the necessary Serializer using the homonym class or the `ModelSerializer` class instead.

What really matters is for you to have understood the respective advantages and disadvantages of the different options available... everything else is about your coding style and preferences!

You will not need to build an authentication system for this specific API, as that is a more advanced topic we will discuss together in the next sections of the course!

## Requirements

<!-- TODO: List the project requirements here -->

## App Setup Instructions

<!-- TODO: Add app setup instructions here -->

