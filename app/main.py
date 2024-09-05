#!/usr/bin/env python

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

PORT = os.getenv("PORT", 8000)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)


@app.get("/")
def home():
    return "Hello World"


def main():
    import uvicorn

    try:
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=PORT,
                    limit_max_requests=10000,
                    log_level="warning",
                    reload=True)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
