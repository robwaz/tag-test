#!/bin/bash

find . -iname '*.json' -exec bash -c '
for f; do
  BASE=$(basename $f)
  DIR=$(dirname $f)
  mv "$f" "$DIR/tags.json"
done' {} +
