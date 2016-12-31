# Flask Mocker

## Introduction
This is a simple Flask-based application to mock-test a RESTful client.
It supports GET/PUT/POST/DELETE operations and requires little to no setup, pulling data from a JSON file.
It never writes to your file, so each new instance of your server starts with a fresh data set.

## Installation
* Create your directory (`mkdir flask-mocker`) and cd into it (`cd flask-mocker`)
* Set up a virtual environment (`virutalenv MOCKER`)
* Activate your virtualenvironment (`source MOCKER/bin/activate`)
* Install flask and flask-restful (`pip install flask`, `pip install flask-restful`)
* Clone this repo into your directory (`git clone https://github.com/bradsbrown/flask-mocker.git`)
* You can modify the data.json file if you'd like, or create your own, but you can just use the demo provided
    * Make sure to keep it in the same directory as the app
* CD into the directory (`cd flask-mocker`) and run the app from the command line, pasing it your data file name (`python app.py data.json`)

## Operations and Endpoints
The supported enddpoints and operations are:
### Root (`http://localhost:<port>`, henceforth referred to as `/`)
* GET - returns the full JSON data object

### Category (`/<category name>`)
* GET - returns the list of items within that category
* POST - adds a new item to the category, and returns the new item.
    * Include a form with as many key/value pairs as you wish.
    * any 'id' submitted will be overwritten by an auto-generated next-largest available integer

### Item (`/<category name>/<item id>`)
* GET - returns the item information
* PUT - Updates the item details, and returns the updated item.
    * allows for change of current key values as well as addition of new values
    * any 'id' submitted will be ignored
* DELETE - Deletes the item from the list, returns a success message.

## Data Format
Your data file should be a standard .json file, with a basic two-layer structure.
* The top layer is a stack of category names, each containing a list.
* The inner layer is a list of items.
    * Each item can have as many different types of key/value pairs as you'd like
    * The only format requirement is that each have a key of 'id' with a unique integer value
    * ID must only be unique _within_ the catergory (each category can have an item with ID of 2)

Sample format:
{
    "category1": [
    {
    "name": "value",
    "id": 1
    },
    {
    "name": "value",
    "id": 2
    }
    ],
    "category2": [
    {
    "fizz": "buzz",
    "pop": "bam",
    "id": 2
    }
    ]
}
