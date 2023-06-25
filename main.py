from fastapi import FastAPI
import random
# hi
app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome": "Hi World!"}

@app.get("/random")
async def get_random():
    rn: int = random.randint(0, 100)
    return {'number': rn, 'limit': 100}

@app.get("/random/{limit}")
async def get_random(limit: int):
    rn: int = random.randint(0, limit)
    return {'number': rn, 'limit': limit}
