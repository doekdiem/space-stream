from collections.abc import AsyncIterable, Iterable

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

message = """
            Streaming from VPS
            This is doekdiem
            This is developer
"""

@app.get("/stream", response_class=StreamingResponse)
async def stream_response() -> AsyncIterable[str]:
    for line in message.splitlines():
        yield line