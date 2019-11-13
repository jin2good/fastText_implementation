import os
import pdb
import pickle

import numpy as np
from tqdm import trange

from config import get_args
from dataset import Dataset
from preprocess import word2token
from vocabulary import Vocabulary, make_vocabulary


np.set_printoptions(suppress=True) # Prevents Numpy arrays from showing scientific notation.


def main():
	config = get_args()
	train_dataset = Dataset(config)
	test_dataset = Dataset(config, mode='test')

	# If a premade vocabulary exists, use it.
	if os.path.isfile('{}vocab.pickle'.format(config.file_prefix)):
		pickle_in = open('{}vocab.pickle'.format(config.file_prefix), mode='rb')
		vocabulary = pickle.load(pickle_in)
		pickle_in.close()
	else:
		vocabulary = Vocabulary()
		vocabulary = make_vocabulary(train_dataset.data, vocabulary)
		pickle_out = open('{}vocab.pickle'.format(config.file_prefix), mode='wb')
		pickle.dump(vocabulary, pickle_out)
		pickle_out.close()

	print('\n\tVocabulary contains a total of {} words.\n'.format(len(vocabulary.token2idx)))

	train_tokenized = word2token(train_dataset, vocabulary)
	test_tokenized = word2token(test_dataset, vocabulary)

	print('Samples:\n')
	print('train_dataset.data[0] = \n{}'.format(train_dataset.data[0]))
	print()
	print('train_tokenized[0, :] = \n{}'.format(train_tokenized[0, :]))
	print()
	print('test_dataset.data[0] = \n{}'.format(test_dataset.data[0]))
	print()
	print('test_tokenized[0, :] = \n{}'.format(test_tokenized[0]))


if __name__ == '__main__':
	main()
