#!/bin/bash

cd pymms/lib
go build -o libdummy.so -buildmode=c-shared ./go-dummy
