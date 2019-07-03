#!/usr/bin/env python3

import sys
from os import path, system

def run(image):
	image = image.replace(path.sep, ':')
	print('-- run', image)
	cmd = f"docker run --rm -it jrmsdev/{image}"
	print('--   ', cmd)
	return system(cmd)

if __name__ == '__main__':
	try:
		image = sys.argv[1]
	except IndexError:
		print("image path?")
		sys.exit(2)
	sys.exit(run(image))
