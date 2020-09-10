#!/bin/bash

cd pymms/lib/go-mms
go build -o libmms.so -buildmode=c-shared ./export
mv libmms.* ../
