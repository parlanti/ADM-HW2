#!/bin/bash
jq -c '. | {id: (.id), title: (.title), total_books_count: (.works | map(.books_count | tonumber) | add)}' series.json >> sum.json
jq -c -s 'sort_by(.total_books_count) | reverse[]' sum.json >> ordered.json
sed -n '1,5p' ordered.json | jq . 
rm sum.json ordered.json

