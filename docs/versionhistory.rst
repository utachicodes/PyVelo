Version history
===============

This library adheres to `Semantic Versioning 2.0 <http://semver.org/>`_.

**0.1.4** (2026-05-21)

- Fixed ``force_multipart=True`` on ``Form`` incorrectly using URL-encoded encoding instead of multipart
- Fixed SSE parser crashing on blank lines and comment lines; multi-line ``data`` fields now correctly joined with newline
- Fixed ``ZstdDecompressor`` not setting internal decompressor object on Python 3.14+
- Fixed HTTP/2 ``_can_send_event`` attribute not being initialized, causing ``AttributeError`` on connection-level window updates
- Fixed WebSocket handshake key to use base64 encoding per RFC 6455
- Fixed ``User-Agent`` version lookup using wrong distribution name
- Fixed ``url_to_connectable`` no-op port assignment
- Updated install instructions and README examples to reflect the ``pyvelo-http`` package name
- Updated error messages to reference ``pyvelo-http`` in install hints

**0.1.3** (2026-05-21)

- Initial release
