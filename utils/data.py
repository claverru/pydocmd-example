import os
import pickle


def load_object(filename='pickles/object.pkl'):
	"""Load object from pickle."""
	with open(filename, 'rb') as f:
		return pickle.load(f)


def save_object(obj, filename='pickles/object.pkl'):
	"""Save object into a pickle."""
	with open(filename, 'wb') as f:  # Overwrites any existing file.
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)	
