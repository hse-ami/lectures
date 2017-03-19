#!/usr/bin/env bash
for i in _build/*.pdf;
do
	utils/dropbox_uploader.sh upload $i Public/`basename $i`;
done
