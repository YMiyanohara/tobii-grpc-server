# Tobii Remote (gRPC)

gRPC Server/Stub to isolate Tobii Pro SDK environment from your application

gRPC Introduction -> https://grpc.io/docs/what-is-grpc/introduction/

Tobii Pro SDK documentation -> https://developer.tobiipro.com/python/python-getting-started.html

## Requirements

- python 3.8.0 (_required_)
- pyenv (recommended)
- poetry (recommended)

## Install

Run

```
> pyenv shell 3.8.0
> poetry env use python
> poetry install
```

at the root of repository.

## Example

### Server

`poetry run python example/tobii_remote_server.py`

### Client

`poetry run python example/tobii_remote_client.py`
