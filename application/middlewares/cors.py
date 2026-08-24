from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# List of allowed origins
origins = [
   "http://localhost",
   "http://localhost:8080",
]

# Adding CORSMiddleware to the FastAPI application
def add_cors_middleware(app):
    CORSMiddleware,
    allow_origins=origins, # List of allowed origins
    allow_credentials=True, # Allow credentials such as cookies and authorization headers
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all HTTP headers
