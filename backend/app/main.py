from fastapi import FastAPI

app = FastAPI()

@app.get("/shipment")
def get_shipments():
    return {
        "content": "wooden table",
        "status": "in transit",
    }