import os

INITIAL_PEERS = os.environ.get("INITIAL_PEERS")
if not INITIAL_PEERS:
    raise RuntimeError("Must specify INITIAL_PEERS environment variable with one or more peer ids")
INITIAL_PEERS = INITIAL_PEERS.split()


if MODEL_NAME := os.environ.get("MODEL_NAME"):
    REF_NAME = os.environ.get("REF_NAME")
else:
    raise RuntimeError("Must specify MODEL_NAME as an index of a transformer block to be tested")
