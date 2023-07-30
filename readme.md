# NokiaPhoneTask

Your task is to implement and test a REST-based application which can store and present information about mobile phones.

Preferably you should choose a python based REST framework for the API implementation (cherrypy, pecan, ...) and  use JMeter for the API testing scenarios. Please create a detailed description in a readme file how to deploy, 
start and use your application and description about the test scenarios. 

Your application can use the choosen REST framework's built-in web/application server, 
it is not required to deploy it to an additional webserver. The main focus of this task is the
testing part to validate the implemented features and reveal the defects of the application.

We know the following facts about a mobile phone:
- Name
- Brand
- Year of release
- OS platform
It is possible to have different phones with the same name, but phones with the same name and same brand should be treated as the same.

Base url of the application:
http://<localhost>:<port>/phone_store/

Features:

1 - Adding a new phone:
The request input has to contain all facts about the phone in json format. If the operation was successful the response should be the 201 Created HTTP status code with the input (+ ID field) in the response body. 
Error cases:
	409 Conflict - Phone is already in the database
	422 Unprocessable Entity - Some of the facts are missing or not in the proper format
	400 Bad Request - otherwise

Request example:
POST http://<localhost>:<port>/phone_store/
{"Name": "X30", "Brand": "Nokia", "Release": 2022, "OS": "Android"}

Response example:
{"Id": 9, "Name": "X30", "Brand": "Nokia", "Release": 2022, "OS": "Android"}

Tips: Use in-memory database to store data, it is not neccessary to have a real database. The structure of the phone data is really simple, it is not neccessary to create your own datasturcture, use built-in objects. When you insert a phone to the database add an ID (sequential numbers) to the record.

2 - Querying phone information:
It is possible to query information about one phone by its database id. If the operation was succesful the response is 200 - OK status code and the body contains the phone info in the following format/example:

GET http://<localhost>:<port>/phone_store/<id>
{"Id": 9, "Name": "X30", "Brand": "Nokia", "Release": 2022, "OS": "Android"}

Error cases:
	404 Not Found - Id is not in the database
	400 Bad Request - otherwise

3 - Listing phones
It is possible to list all of the stored phones. If the list operation was succesful the response is 200 - OK and the body contains the phone infos in the following format/example:

GET http://<localhost>:<port>/phone_store/
[{"Id": 9, "Name": "X30", "Brand": "Nokia", "Release": 2022, "OS": "Android"}, {"Id": 10, "Name": "X20", "Brand": "Nokia", "Release": 2021, "OS": "Android"}]

4 - Delete phone
The user can delete phone from the database by its ID. If the operation was succesful the response is 204 without content.

DELETE http://<localhost>:<port>/phone_store/<id>

Error cases:
	404 Not Found - Id is not in the database
	400 Bad Request - otherwise

Testing:
To test your application you have to use Apache JMeter. In the JMeter it is possible to create test plans to validate your application. Based on the specification you have to find out what should be tested to cover all of the features. Any additional test plans about the appliciation are welcome.
The suggestion is to create smaller tests after a feature is ready. When the application development is finished you can create full lifecycle tests. 

Outcome:
- Create a zip file which contains the application code, the test plans and the documentation
- The phone application can be started, running continuously and ready to serve incoming requests
- Test plans can be imported and executed in JMeter to test the running application
- Documentation: Detailed description how to build and use the application and short notes about the test plans


===
# Documentation

This is an implementation and testing of a REST-based application able to store and show information about [mobile phones](https://www.nokia.com/phones/en_au/smartphones) using [Flask](https://pythonbasics.org/what-is-flask-python/) and [JMeter](https://jmeter.apache.org/) technologies.

In this particular task, only the following fields were considered:
- Name
- Brand
- Year of Release
- Operating System

[Contents]
- [Build and Use the application?](#build_and_use_the_application)
- [Testing](#testing)
- [Deployment](#deployment)

# Build and Use the application? <a name = "build_and_use_the_application"></a>

## Setup

The following the tutorial on how to install Flask Framework: https://flask.palletsprojects.com/installation/


## Run

Run the python application using the command:

```shell
python3 app.py
```

# API

## Description
This is an API that allow to perform GET, POST, PUT and DELETE HTTP request methods to Mobile phones.

## Base URL of the application
http://<localhost>:<port>/phone_store/

Most problably the port will be 5000.

## Features
- [Add new phone](#add_new_phone)
- [Query phone information](#query_phone_information)
- [List phones](#list_phones)
- [Delete phone](#delete_phone)

### Add new phone <a name = "add_new_phone"></a>

### Endpoint
```
POST http://<localhost>:<port>/phone_store/
```
Inserts a new phone to the database if no error is encountered.

### Error cases:
Error code operations for adding new phone:
- 409 Conflit: Duplicate phone now allowed.
- 422 Unprocessable Entity: Parameters not passed correctly or malformated.
- 400 Bad Request: In case any other error occur.

### Query phone informatione <a name = "query_phone_information"></a>

### Endpoint
```
GET http://<localhost>:<port>/phone_store/<id>
```
Gives back the phone with specific ID in JSON format.

### Error cases:
Error code operations for adding new phone:
- 404 Not Found: ID not found in the database
- 400 Bad Request: In case any other error occur.


### List phones <a name = "list_phones"></a>

### Endpoint
```
GET http://<localhost>:<port>/phone_store/
```

List all phones stored in the database in JSON format. Code 200 - OK is returned to represent sucessfull operation. 

### Delete phone <a name = "delete_phone"></a>

### Endpoint
```
DELETE http://<localhost>:<port>/phone_store/<id>
```
Delete from the database the phone with specific ID in JSON format.

### Error cases:
Error code operations for delete operations:
- 404 Not Found: ID not found in the database
- 400 Bad Request: In case any other error occur.

## Testing <a name = "testing"></a>

The goal of this plan is to test the application based It's specification either in MASTER and LEVEL SPECIFIC TEST plan using the IEEE 829 Standard.

### Plan

### Test Items
We are testing all the features the application can perform (complete CRUD).

### Software Risk Issues
By adding more than 10^8 items in our database, the application tends to load all the mobile phones lowly due to the complexity and ammount of data which might lead to a bug.

### Features to be tested

| Syntax      					| Level	|
| :---------------------------: | :---: |
| Add 1 mobile phone      		| H     |
| Add another mobile phone   	| M    	|
| List all mobile phones   		| H     |
| Show only the 2nd added   	| H     |
| Delete the first   			| H     |
| List all mobile phones   		| L     |
| Edit a mobile phone   		| H     |
| Delete all mobile phones   	| H     |
| List again  					| L     |
| Show the 1st mobile phone   	| L     |

On risk levels, H - High; M - Medium; L - Low

### Features not to be tested
No need for this task.

### Strategy
For this task, [Apache JMeter](https://jmeter.apache.org/) is the testing software recommended to be used. Please check out [JMeter Getting Started](https://jmeter.apache.org/usermanual/get-started.html) to learn in case needed.

There will be about 4 regression tests. We used "Retest all" and "Regression test selection".

At MASTER LEVEL is expected all functionality work perfect.

Please, be noticed that first we try to test small test cases and then move bigger ones so that when get finished we create the full lifecycle tests.

### Item pass/fail criteria
#### Unit test level
Similar test cases can be found on the file
Tests:


When running the test cases using the current version, "all test cases completed" are expected as output.

#### Master test plan level
Percentage of minor defects -> 0%
Lower level plans completed -> 0%

### Suspension criteria and resumption requirements
It is only allowed an upper bound of 50% of defects. More than that, It is recommended to have a deep check on the solution provided before rerun the tests.

### Test Deliverables
As part of this plan, we deliver:
- Test plan document
- Test cases
- Test Design specifications
- Tools and their ouputs

### Remaining test tasks
No more test cases are listed up to this release documentation date.

### Environmental needs
We recommend to run the application and test software using:
- Minimum RAM 4G
- 10 GB available disk space
- Ubuntu 20.04.6 LTS
- Apache JMeter 5.6.2
- Java 8+
- Python3
- Flask

### Staffing and training needs
In case of any questions, please contact Alfredo Martins.
Many resources can be used to learn how to use all the tools mentioned; Some links were left to help on training.

### Responsibilites
Alfredo Martins is in charge of everything related to this task.

### Schedule
This work was done in no more than 7 days using a flexible time schedule.

### Planning risks
Skipped

### Approvals
Skipped

### Test plans
Download the [test plan](https://github.com/CodeTyperPro/phone-task-testing/) and import it on JMeter in order to test the running application.

Now please follow the steps:
1. ...
2. ...
3. ...


## Deployment <a name = "deployment"></a># phone-task-testing
