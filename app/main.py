import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, post, user, vote


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]  # public API

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # domains which are able to talk to our API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
