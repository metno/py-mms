#!/bin/bash

cd pymms/lib/go-mms
go build -o libgomms.so -buildmode=c-shared ./cmd/mms
mv libgomms.* ../
