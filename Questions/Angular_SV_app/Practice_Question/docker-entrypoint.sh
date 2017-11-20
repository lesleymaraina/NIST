#!/bin/bash

# npm looks for 'node' command but Ubuntu default node.js command is nodejs.
ln -s /usr/bin/nodejs /usr/bin/node
npm start