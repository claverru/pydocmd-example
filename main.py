import os

from utils import data


def main():
	if 'pickles' not in os.listdir():
		os.mkdir('pickles')

		a = {'hi': 1, 'bye': 0}

		data.save_object(a, 'pickles/a.pkl')

		del a

		a = data.load_object('pickles/a.pkl')
		print(a)


if __name__ == '__main__':
	main()