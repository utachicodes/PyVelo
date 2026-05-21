# PyVelo

[![Build Status](https://github.com/utachicodes/pyvelo/actions/workflows/test.yml/badge.svg)](https://github.com/utachicodes/pyvelo/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/pyvelo-http.svg)](https://pypi.org/project/pyvelo-http/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/pyvelo-http.svg)](https://pypi.org/project/pyvelo-http/)

**PyVelo** is a next-generation, high-performance async HTTP client library for Python, built on the robust [AnyIO](https://github.com/agronholm/anyio) framework. It is designed for speed, reliability, and ease of use in modern asynchronous applications.

---

## Features

- **High Performance**: Optimized for speed and low latency.
- **AnyIO Backed**: Compatible with `asyncio` and `trio`.
- **HTTP/1.1 & HTTP/2**: Full support for modern HTTP standards.
- **WebSocket Client**: Robust WebSocket implementation.
- **Server-Sent Events (SSE)**: Easy-to-use SSE client.
- **Advanced Decompression**: Transparent support for deflate, gzip, zstd, and brotli.
- **ASGI Support**: Test ASGI 3.0 applications directly without a running server.
- **Flexible Body Serialization**: Built-in JSON, CBOR, and multipart form helpers.

## Installation

```bash
pip install pyvelo-http
```

To include optional extras (brotli compression, CBOR serialization, etc.):

```bash
pip install pyvelo-http[brotli,zstd,cbor]
```

## Quick Start

```python
import anyio
from pyvelo import HTTPClient

async def main():
    async with HTTPClient() as client:
        response = await client.get("https://httpbin.org/get")
        print(response.status_code)
        print(response.text)

anyio.run(main)
```

### POST with JSON

```python
import anyio
from pyvelo import HTTPClient, JSON

async def main():
    async with HTTPClient() as client:
        response = await client.post(
            "https://httpbin.org/post",
            JSON({"hello": "world"}),
        )
        print(response.text)

anyio.run(main)
```

### WebSocket

```python
import anyio
from pyvelo import HTTPClient

async def main():
    async with HTTPClient() as client:
        async with client.connect_ws("wss://echo.example.com/ws") as ws:
            await ws.send("Hello!")
            reply = await ws.receive()
            print(reply)

anyio.run(main)
```

### Server-Sent Events

```python
import anyio
from pyvelo import HTTPClient

async def main():
    async with HTTPClient() as client:
        async with client.connect_sse("https://example.com/events") as stream:
            async for event in stream:
                print(event.event, event.data)

anyio.run(main)
```

## Documentation

Full documentation is available at [pyvelo.readthedocs.io](https://pyvelo.readthedocs.io/).

## License

This project is licensed under the MIT License.
