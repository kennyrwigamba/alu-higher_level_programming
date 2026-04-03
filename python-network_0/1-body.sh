#!/bin/bash
# Display the response body for a 200 status code
url="$1"
tmp_file="$(mktemp)"
status_code="$(curl -sL -o "$tmp_file" -w "%{http_code}" "$url")"

if [ "$status_code" -eq 200 ]; then
	cat "$tmp_file"
fi

rm -f "$tmp_file"
