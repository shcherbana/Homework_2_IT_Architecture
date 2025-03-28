# Homework_2_IT_Architecture

# **Overview**

This project is built on a microservice architecture using FastAPI. It includes three independent services working together to classify text messages as automobile or medicine related:

*Client Service* - acts as an entry point, handling communication between the user, Business Logic Service, and DB Service.

*Business Logic Service* - processes text data using a pre-trained model to detect wether it is related to automobile or medicical industry.

*DB Service* - stores and retrieves detection/classification results.

# **Starting the Services**

To run all services locally, use the following commands in separate terminal windows:

1. Business Logic Service (runs on port 8000):
   
```bash
uvicorn business_logis:app --port 8000
```


2. Database Service (runs on port 8001):

```bash
uvicorn database_service:app --port 8001
```

3.  Client Service (runs on port 8002):

```bash
uvicorn client_logis:app --port 8002
```

# **Client Service - Token-Based Authentication**
1. Client Service requires authentication for requests to `/process`
2. Authentication uses a Bearer Token - checked in the Authorization header.
3. The expected token is stored in the variable SECRET_TOKEN. 
4. If the provided token is invalid/missing - request is rejected(401 Unauthorized).

# **Example Request with Token**

```bash
curl -X POST "http://localhost:8002/process" \ 
     -H "Authorization: Bearer secret-token" \        
     -H "Content-Type: application/json" \
     -d '{"data":{"text": "I have problem with my heart"}, "key": 1}' 
{"status":"success","processed_data":{"text":"I have problem with my heart","category":"Medical"}}
```
# **Request Flow and Usage Example**

1. Client sends a request to classify text `(/process)`
2. Client service validates the token and forwards the request to the buiness logic service.
3. Business logic service processes the request using the trained model and returns the result.
4. Client service forwards the result to the DB service for storage.
5. Client service returns the results to the client.

If the client wants to classify by category(automobile/medicine) some text(As example here is used sentence - "I have problm with my heart")in the seperate terminal he should run the following command:

```bash
curl -X POST "http://localhost:8002/process" \ 
     -H "Authorization: Bearer secret-token" \        
     -H "Content-Type: application/json" \
     -d '{"data":{"text": "I have problem with my heart"}, "key": 1}'
```
The client will see the following in the terminal:
`{"status":"success","processed_data":{"text":"I have problem with my heart","category":"Medical"}}`

Check in the postman wether it was saved to our db:

<img width="1281" alt="Знімок екрана 2025-03-28 о 18 00 53" src="https://github.com/user-attachments/assets/2f5fea3d-da5d-4fcb-830e-ae084e3c8814" />

