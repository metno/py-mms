#!/bin/bash

cd pymms/lib/go-mms

go build -v -o libmms.so -buildmode=c-shared ./export
go build -v ./cmd/mmsd
go build -v ./cmd/mms

mv libmms.* ../
mv mmsd ../
mv mms ../
