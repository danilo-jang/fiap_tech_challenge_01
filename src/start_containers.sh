#!/bin/bash

docker-compose up -d

export MONGODB_URL="mongodb+srv://pos3mlet:pos3mlet@127.0.0.1:27017/pos3mlet?retryWrites=true&w=majority"