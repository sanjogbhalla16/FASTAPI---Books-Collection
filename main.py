from fastapi import FastAPI
from routes.UserCred import user_router  # Import the router

app = FastAPI()

# Include the user routes
app.include_router(user_router)