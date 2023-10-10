from typing import Annotated

from fastapi import FastAPI, status
from fastapi import Form
import flask

import schemas
from lib import get_logger
from fastapi_pagination import Page, paginate

LOG = get_logger(__name__)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["http://testapp"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        reload=True,
    )
