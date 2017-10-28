# sozlik-web
sozlik-web project is build using [Flask](http://flask.pocoo.org/) and sqlite. It is a simple dictionary application that has following features:
- Auto suggestions on user input
- If a user searches for a wrong word, or makes a typo, there will be 'did you mean' option with possible substitues 
(if applicable)

## Setup
### Install and initialize virtual environment
```
pip install virtualenv
virtualenv sozlikenv
source sozlikenv/bin/activate
```
### Install required libraries
```
pip install flask gunicorn
```
### Clone the project
```
git clone https://github.com/shagalalab/sozlik-web.git
```
### Run the app
```
gunicorn --bind localhost:5000 wsgi:app
```
### Access the app
You can open the app in your browser by typing http://localhost:5000

