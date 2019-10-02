import os


def _exclude():
	names = []
	with open('.gitignore', 'r') as f:
		for line in f.readlines():
			if not line.startswith('#') and line is not '\n':
				line = line.replace('\n', '')
				line = line.replace('*', '')
				line = line.replace('/', '')
				names.append(line)
	return names + ['.gitignore', '.git']


def list_files(startpath='.', name='structure.md', exclude=[]):
	with open(name, 'w+') as file:
		for root, dirs, files in os.walk(startpath):
			dirs[:] = [d for d in dirs if d not in exclude]
			files[:] = [f for f in files if f not in exclude]
			level = root.replace(startpath, '').count(os.sep) - 1
			indent = '\t'* (level)
			folder = os.path.basename(root)
			if root is not startpath: # not to print root
				file.write('{}- **{}/**  \n'.format(indent, folder))
			subindent = '\t' * (level + 1)
			for f in files:
				file.write('{}- {}  \n'.format(subindent, f))


if __name__ == '__main__':
	list_files(exclude=_exclude())