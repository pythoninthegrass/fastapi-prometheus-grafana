#!/usr/bin/env python

import os
import sys
from eliot import log_call, to_file, Message as msg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

PORT = os.getenv("PORT", 8000)

to_file(sys.stdout)

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
    msg.log(message_type="home", message="Hello World")
    return "Hello World"


def main():
    import uvicorn

    try:
        msg.log(message_type="start", message="Starting the server")
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=PORT,
                    limit_max_requests=10000,
                    log_level="info",
                    reload=True)
    except KeyboardInterrupt:
        msg.log(message_type="exit", message="Exiting the server")
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        msg.log(message_type="error", message=str(e))
        exit(1)


if __name__ == "__main__":
    main()
