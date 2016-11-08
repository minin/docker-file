#!/bin/bash

echo Starting celery.
celery -A moonShot worker --loglevel=info