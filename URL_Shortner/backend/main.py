
# main.py
from fastapi import FastAPI, HTTPException
from http.client import HTTPException
import random
import string
from database import Session
from model import URL
from schema import ShortenRequest
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000/"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)



def generate_code():
    characters = string.ascii_letters + string.digits
    code_length = 6
    return ''.join(random.choice(characters) for i in range(code_length))

# Roputing of url shortner

@app.post("/shorten/")

def shorten_url(url_input: ShortenRequest):
    db = Session()
    code = generate_code()
    while db.query(URL).filter(URL.uni_code == code).first():
        code = generate_code()
    db_url = URL(uni_code=code, original_url=url_input.original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return {"shortened_url": f"http://localhost:8000/{code}"}


# to redirect shortened URL
@app.get("/{code}")
def redirect_url(code: str):
    db = Session()
    url = db.query(URL).filter(URL.uni_code == code).first()
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"redirect_url": url.original_url}


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)




































# # Function to generate a short URL
# def generate_short_url(url: str) -> str:
#     hash_object = hashlib.sha1(url.encode())
#     return hash_object.hexdigest()[:8]

# # Function to shorten a URL
# def shorten_url(url: str) -> str:
#     short_url = generate_short_url(url)
#     with Session() as session:
#         mapping = URLMapping(short_url=short_url, original_url=url)
#         session.add(mapping)
#         session.commit()
#     return short_url

# # Function to retrieve original URL from short URL
# def get_original_url(short_url: str) -> str:
#     with Session() as session:
#         mapping = session.query(URLMapping).filter(URLMapping.short_url == short_url).first()
#         if mapping:
#             return mapping.original_url
#     return None

# # Example usage
# if __name__ == "__main__":
#     original_url = "https://www.google.com/"
#     short_url = shorten_url(original_url)
#     print("Short URL:", short_url)
#     retrieved_url = get_original_url(short_url)
#     print("Retrieved URL:", retrieved_url)






