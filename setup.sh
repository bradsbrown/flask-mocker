# if venv not activated, create one and source it
if [[ -z "$VIRTUAL_ENV" ]]; then
    virtualenv MOCKER
    source MOCKER/bin/activate
fi

# install flask-restful (includes base flask)
pip install flask-restful
