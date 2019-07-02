#!/usr/bin/env python3

import sys
from glob import glob
from os import path, system

files = glob('**/Dockerfile', recursive = True)

def main():
	rc = 0
	for fn in sorted(files):
		print('--', fn)
		src = path.dirname(fn)
		tag = '/'.join(['jrmsdev', src.replace(path.sep, ':')])
		build(src, tag)
	return rc

def build(src, tag):
	print('--  ', src)
	print('--    ', tag)
	cmd = f"docker build --rm -t {tag} {src}"
	print('--  ', cmd)
	rc = system(cmd)
	if rc != 0:
		print('-- FAIL:', cmd)
		sys.exit(1)

if __name__ == '__main__':
	sys.exit(main())
