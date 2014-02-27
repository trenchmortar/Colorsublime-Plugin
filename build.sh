#!/usr/bin/env bash
# set -e
killall sublime_text
PKG="Colorsublime-Plugin"
DIR="$HOME/.config/sublime-text-3/Packages"
# zip -r $PKG *
rm -fr "$DIR"/"$PKG"
cp -r ../"$PKG" "$DIR"
subl
