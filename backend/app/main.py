from fastapi import FastAPI

# 1. Create the main application instance
app = FastAPI(title="AegisTrace API")

# 2. Define a "Route" or "Endpoint"
@app.get("/")
def health_check():
    # 3. Return a response
    return {
        "status": "ok", 
        "message": "AegisTrace Backend is running!"
    }
