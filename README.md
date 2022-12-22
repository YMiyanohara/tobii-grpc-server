# Tobii Remote (gRPC)

gRPC Server/Stub to isolate Tobii Pro SDK environment from your application

gRPC Introduction -> https://grpc.io/docs/what-is-grpc/introduction/

Tobii Pro SDK documentation -> https://developer.tobiipro.com/python/python-getting-started.html

## requirements

- python 3.8.0 (_required_)
- pyenv (recommended)
- poetry (recommended)

## install

`poetry install`

## usage

### Server

`poetry run python tobii_remote/tobii_remote_server.py`

### Client (sample)

`(poetry run) python tobii_remote/tobii_remote_client.py`
