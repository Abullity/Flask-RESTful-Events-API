# RESTful Flask App
A simple Flask based RESTful events/calendar Web API

# What does the API do

API takes POST, GET and DELETE requests and updates, retrieves or delets an event 
an event is a json data, which has attributes:

• event (the name of the event)

• date 

• location

The API can retrieve all the events, an event by id or events filtered by starting and ending dates

detailed inforamtion on POST request's body data-format as well as routes and methods available for given routes are given on API's root page

# Installation and dependencies

App uses Flask-RESTful framework

The required modules (Including Flask, Flask-RESTful and Flask_Sqlalchemy) are given in requirements.txt file, which was generated by 'pip freeze' command.

To install required modules run 'pip -r requirements.txt' command from project's root directory

After you have every package installed, execute run.py file, the rest should work without issues.



#Running the app

Open terminal in project's root directory and run the following command

"python run.py"

or

"python3 run.py"

The command takes two arguments host address and port,
you don't have to specify these and by default the app will be run on localhost port 5000 ---> http://127.0.0.1:5000/


# Routesu222008989u222008989ad54

u222http://12u22200u222008989u2220089897.0.0.1:5000u222008989222008989u222008989ad54