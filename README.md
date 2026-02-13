# PyVelo

[![Build Status](https://github.com/utachicodes/pyvelo/actions/workflows/test.yml/badge.svg)](https://github.com/utachicodes/pyvelo/actions/workflows/test.yml)
[![Code Coverage](https://coveralls.io/repos/github/utachicodes/pyvelo/badge.svg?branch=master)](https://coveralls.io/github/utachicodes/pyvelo?branch=master)
[![Documentation Status](https://readthedocs.org/projects/pyvelo/badge/?version=latest)](https://pyvelo.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/pyvelo-http.svg)](https://pypi.org/project/pyvelo-http/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/pyvelo.svg)](https://pypi.org/project/pyvelo/)

**PyVelo** is a next-generation, high-performance HTTP client library for Python, built on the robust [AnyIO](https://github.com/agronholm/anyio) framework. It is designed for speed, reliability, and ease of use in modern asynchronous applications.

---

## Features

- **High Performance**: Optimized for speed and low latency.
- **Async & Sync Support**: Works seamlessly with both synchronous and asynchronous code.
- **AnyIO Backed**: Compatible with `asyncio`, `trio`, and other AnyIO-supported event loops.
- **HTTP/1.1 & HTTP/2**: Full support for modern HTTP standards.
- **WebSocket Client**: Robust WebSocket implementation.
- **Server Sent Events (SSE)**: Easy-to-use SSE client.
- **Advanced Decompression**: Transparent support for deflate, gzip, zstd, and brotli.
- **ASGI Support**: Test ASGI 3.0 applications directly without overhead.

## Installation

Install PyVelo using pip:

```bash
pip install pyvelo
```

To include optional dependencies for extra performance (like `brotli` or `zstd` support):

```bash
pip install pyvelo[brotli,zstd]
```

## Quick Start
```python
import anyio
from pyvelo import AsyncClient

async def main():
    async with AsyncClient() as client:
        response = await client.get('https://httpbin.org/get')
        print(response.json())

anyio.run(main)
```

## Documentation

Full documentation is available at [pyvelo.readthedocs.io](https://pyvelo.readthedocs.io/).

## License

This project is licensed under the MIT License.
