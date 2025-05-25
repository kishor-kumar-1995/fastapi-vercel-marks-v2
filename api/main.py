from fastapi import FastAPI

app = FastAPI()

marks_data = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30
}

@app.get("/")
def root():
    return {"message": "Welcome to the marks API. Use /api?name=Alice&name=Bob"}

@app.get("/api")
def get_marks(name: list[str] = []):
    result = [marks_data.get(n, 0) for n in name]
    return {"marks": result}

from mangum import Mangum
handler = Mangum(app)
