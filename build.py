#!/usr/bin/env python3

import sys
from glob import glob
from os import path
from subprocess import check_output

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
	cmd = ['docker', 'build', '--rm', '-t', tag, src]
	print('--  ', ' '.join(cmd))
	check_output(['docker', 'build', '--rm', '-t', tag, src])

if __name__ == '__main__':
	sys.exit(main())
