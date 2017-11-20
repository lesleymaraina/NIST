#!/usr/bin/env bash

county=US
state=MD
locality=Gaithersburg
organization=NIST
organizationalUnit=MML
commonName=localhost # Change later to real name
email=root@localhost # Change later to a real email

openssl genrsa -out ./nginx/server.key 2048

openssl req -nodes -new -key ./nginx/server.key -out ./nginx/server.csr -subj "/C=US/ST=$state/L=$locality/O=$organization/OU=$organizationalUnit/CN=$commonName/emailAddress=$email"

openssl x509 -req -days 365 -in ./nginx/server.csr -signkey ./nginx/server.key -out ./nginx/server.cer