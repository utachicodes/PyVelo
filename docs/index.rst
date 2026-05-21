PyVelo
======

**PyVelo** is a next-generation, high-performance async HTTP client library for Python,
built on the robust `AnyIO <https://github.com/agronholm/anyio>`_ framework.

Features
--------

- **High Performance**: Optimized for speed and low latency.
- **AnyIO Backed**: Compatible with ``asyncio`` and ``trio``.
- **HTTP/1.1 & HTTP/2**: Full support for modern HTTP standards.
- **WebSocket Client**: Robust WebSocket implementation.
- **Server-Sent Events (SSE)**: Easy-to-use SSE client.
- **Advanced Decompression**: Transparent support for deflate, gzip, zstd, and brotli.
- **ASGI Support**: Test ASGI 3.0 applications directly without a running server.
- **Flexible Body Serialization**: Built-in JSON, CBOR, and multipart form helpers.

Installation
------------

.. code-block:: bash

   pip install pyvelo-http

To include optional extras:

.. code-block:: bash

   pip install pyvelo-http[brotli,zstd,cbor]

Quick Start
-----------

.. code-block:: python

   import anyio
   from pyvelo import HTTPClient

   async def main():
       async with HTTPClient() as client:
           response = await client.get("https://httpbin.org/get")
           print(response.status_code)
           print(response.text)

   anyio.run(main)

The manual
----------

.. toctree::
   :maxdepth: 2

   api
   faq
   support
   contributing
   versionhistory
