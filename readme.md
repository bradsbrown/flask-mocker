# Flask Mocker

## Introduction
This is a simple Flask-based application to mock-test a RESTful client.
It supports GET/PUT/POST/DELETE operations and requires little to no setup, pulling data from a JSON file.
It never writes to your file, so each new instance of your server starts with a fresh data set.

## Installation
* Create your directory (`mkdir flask-mocker`) and cd into it (`cd flask-mocker`)
* Set up a virtual environment (`virutalenv MOCKER`)
* Activate your virtualenvironment (`source MOCKER/bin/activate`)
* Clone this repo into your directory (`git clone https://github.rackspace.com/brad2913/flask-mocker.git`)
* CD into the directory (`cd flask-mocker`)
* run the setup script (`./setup.sh`)
* You can modify the data.json file if you'd like, or create your own, but you can just use the demo provided
    * Make sure to keep it in the same directory as the app

## Running the app
You can call the app as simply as `python app.py <file name>`, but there are optional arguments you can pass as well:
`python app.py [-p PORT] [--debug] <file name>`
* `-p` or `--port` followed by a port number will run the server on the port of your choosing
* `--debug` will run the server in debug mode for additional information on issue tracing

## Operations and Endpoints
**Note: default port is 5000**

The supported enddpoints and operations are:
### Root (`http://localhost:<port>`, henceforth referred to as `/`)
* GET - returns the full JSON data object

### Category (`/<category name>`)
* GET - returns the list of items within that category
* POST - adds a new item to the category, and returns the new item.
    * Include a form with as many key/value pairs as you wish.
    * item will be assigned an auto-generated uuid4-based key

### Item (`/<category name>/<item id>`)
* GET - returns the item information
* PUT - Updates the item details, and returns the updated item.
    * allows for change of current key values as well as addition of new values
* DELETE - Deletes the item from the list, returns a success message.

## Data Format
Your data file should be a standard .json file, with a basic two-layer structure.
* The top layer is a stack of category names, each containing a subdict.
* The inner layer is a list of items.
    * Each item can have as many different types of key/value pairs as you'd like
    * The only format requirement is that each item have a key that is unique within the category
    * It is recommended that item keys are uuid4 strings, to match the format of added items.

Sample format:
{
    "category1": {
        "key1": {
            "name": "value",
        },
        "key2": {
            "name": "value",
        }
    },
    "category2": {
        "key1": {
            "fizz": "buzz",
            "pop": "bam",
        }
    }
}
