# Debian

Just dist-upgrade and cleanup base image.

* [debian](https://github.com/jrmsdev/dockerfiles/blob/master/debian/Dockerfile)
	* FROM debian:stable-slim
* [debian:testing](https://github.com/jrmsdev/dockerfiles/blob/master/debian/testing/Dockerfile)
	* FROM debian:testing-slim

# Golang

dist-upgrade and install (excluding recommends) golang package.

* [golang](https://github.com/jrmsdev/dockerfiles/blob/master/golang/Dockerfile)
	* FROM jrmsdev/debian
* [golang:testing](https://github.com/jrmsdev/dockerfiles/blob/master/golang/testing/Dockerfile)
	* FROM jrmsdev/debian:testing
