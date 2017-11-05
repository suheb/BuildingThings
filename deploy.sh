#!/usr/bin/env bash


if [[ $1 == "-m" ]]; then
	msg=$2
else
	msg="Updading site"
fi

echo "Genrating content..."
pelican content -d -o output -s publishconf.py
echo "Updading gh-pages branch.."
ghp-import output -m "$msg"
echo "Pushing to user page repo.."
env -i git push https://github.com/suheb/suheb.github.io.git gh-pages:master
echo "Success!"