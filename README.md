
# Flask App Boilerplate Code

Boilerplate template for a Python Flask application.

## Directory Structure
```
├── data/
├── env/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   └── js/
├── templates/
│   └── base.html
├── tests/
├── crud.py
├── model.py
├── requirements.txt
├── seed.py
├── server.py
└── README.md
```

## <a name="Install"></a>Installation Instructions

1. Clone this repository:
```shell
git clone https://github.com/yvonneyeh/flask-boilerplate.git
```

***Optional***: Create and activate a virtual environment:
```shell
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

2. Install dependencies: 
```shell
pip3 install -r requirements.txt
```

3. Create environmental variables to hold your API keys in a `secrets.sh` file:
```
export API_KEY='{API_KEY}'
```

4. Create your database & seed sample data:
```shell
createdb database
python3 seed.py
```

5. Run the app on localhost:
```shell
source secrets.sh
python3 server.py
```