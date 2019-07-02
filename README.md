# jrmsdev/dockerfiles

## Debian

Just dist-upgrade and cleanup base image.

* debian
	* FROM debian:stable-slim
* debian:testing
	* FROM debian:testing-slim

## Golang

dist-upgrade and install (excluding recommends) golang package.

* golang
	* FROM jrmsdev/debian
* golang:testing
	* FROM jrmsdev/debian:testing
