# Live Chat Room REST API

Build by using Django, Django REST Framework, PostgreSQL

Deployed on Heroku: https://chat-space-room.herokuapp.com

/api/messages/list/ will return all messages with POST message possibility <br />
/api/messages/list/0 will return first 10 messages <br />
/api/messages/list/1 will return second 10 messages <br />
/api/messages/single/slug will return specified single message <br />
/api/messages/single/anonymous-1582493345 (example) <br />
 
# Deploy project on your local machine

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Insert your own db configuration settings (see example secret.env):
and change file name to .env:

`DB_PASSWORD`,
`DB_NAME`,
`DB_USER`

3 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

4 - Run app:

`python3 manage.py runserver`
