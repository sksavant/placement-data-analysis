# Placement data saver

## Introduction

This code logs in to the placement portal and saves the company JAFs data into a JSON? file so that analysis can be done later

## How does it do?

Uses [mechanize](http://wwwsearch.sourceforge.net/mechanize) to emulate a browser

## TODO

- Store JAF data in a class structure
- Decide on format to store to disk
- Updating the disk
  - Resolving duplicates
  - Reading data from disk
  - Storing new data
