# verify virtualenv is installed and active
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "No virtualenvironment detected. Please set up and activate a virtualenv."
    exit
fi

# install flask-restful (includes base flask)
pip install flask-restful
