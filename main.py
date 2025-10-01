from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from summarizer import summarize_pdf
from quiz_generator import generate_quiz
from unimercatorum import login_and_fetch_material

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/upload/")
async def upload(file: UploadFile):
    content = await file.read()
    with open(file.filename, "wb") as f:
        f.write(content)
    summary = summarize_pdf(file.filename)
    return {"summary": summary}

@app.post("/quiz/")
def quiz(topic: str = Form(...)):
    return {"quiz": generate_quiz(topic)}

@app.post("/unimercatorum/")
def connect(username: str = Form(...), password: str = Form(...)):
    return {"materials": login_and_fetch_material(username, password)}
