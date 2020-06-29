## Requirements

    python 3.8
    MongoDB
    
Use "Users().json_to_mongo()" in models.py to import data from JSON to MongoDB.
    
## Start FastAPI

    uvicorn main:app --reload
    
## Build and up Docker

создать образ и запустить его

    docker build --tag fastapi-mongodb .
    docker run --name python-app -p 8000:8000 fastapi-mongodb
    
создание и запуск докера

    docker-compose build
    docker-compose up
    