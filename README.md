

## Risk form application.
Django rest framework + vue.js + docker

### Prerequisites
Node: 10.8.0
Docker: 18.06.0-ce
Docker-compose: 1.22.0
Python:3.6

## Instalation:
```
git clone https://github.com/amdrgoncalves/risk.git
cd risk 
```

#venv
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r config/requirements.txt
```

Frontend. Vue is working like a template for django. In deployment is served by Nginx at collectstatic folder created by django.
```
cd src/static/risk_frontend
sudo npm install -g @vue/cli
npm install
npm run build #django serves from static/risk_frontend/dist
npm run test:unit
```
For development (localhost:8080)

```
npm run serve 
```


## Running
```
docker-compose build
docker-compose up
```

Create sample data and test
```
docker exec -it dg01 bash
python api/scripts/create_data.py
python manage.py test
exit
```

DRF - API

localhost:8000/api/v1/risks

localhost:8000/api/v1/risks/1





