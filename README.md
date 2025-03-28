# Homework_2_IT_Architecture

**Overview**

This project is built on a microservice architecture using FastAPI. It includes three independent services working together to classify text messages as automobile or medicine related:

*Client Service* - acts as an entry point, handling communication between the user, Business Logic Service, and DB Service.

*Business Logic Service* - processes text data using a pre-trained model to detect wether it is related to automobile or medicical industry.

*DB Service* - stores and retrieves detection/classification results.

**Starting the Services**

To run all services locally, use the following commands in separate terminal windows:

1. Business Logic Service (runs on port 8000):

```uvicorn business_logis:app --port 8000```

2. Database Service (runs on port 8001):
```uvicorn database_service:app --port 8001```

3.  Client Service (runs on port 8002):
```uvicorn client_logic:app --port 8002```




