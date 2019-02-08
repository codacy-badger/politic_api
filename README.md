# politic_api

Politico enables citizens give their mandate to politicians running for different government offices
while building trust in the process through transparency.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6.7
Virtualenv
Flask==1.0.2
pytest==4.2.0
pylint==2.2.2
```

### Installing

Step 1. Clone the repository



```
git clone https://github.com/Warui-K/politico-api.git
```

cd to the directory locally

```
cd politico-api
```

Create and activate a virtual environment

```
virtualenv venv
```
```
source venv/bin/activate
```

Step 2

Run the application
```
flask run
```

Step 3

Test the application
Test the endpoints using Postman
Run pytest
```
pytest
```
# API Endpoints

## User Endpoint /api/v1

| METHOD        | ENDPOINT      | FUNCTION      |
| ------------- | ------------- | ------------- |
| GET           | /user         | Get All Users |
| GET           | /user/<int:id>| Get one User  |
| POST          | /user         | Add User(s)   |
| DELETE        | /user/<int:id>| Delete a User |
| PATCH         | /user/<int:id>| Update a User |

## office Endpoint /api/v1

| METHOD        | ENDPOINT          | FUNCTION      |
| ------------- | -------------     | ------------- |
| GET           | /office           | Get offices   |
| GET           | /office/<int:id>  | Get one office|
| POST          | /office           | Add office(s) |

## party Endpoint /api/v1

| METHOD        | ENDPOINT          | FUNCTION          |
| ------------- | -------------     | -------------     |
| GET           | /party            | Get partyies      |
| GET           | /party/<int:id>   | Get one party     |
| POST          | /party            | Add party(s)      |



## Authors

* **Warui Kamiri**

## Acknowledgments

* Andela Pre-Bootcamp 
