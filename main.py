import os
import pdb
import pickle

from tqdm import trange

from config import get_args
from dataset import Dataset
from vocabulary import Vocabulary, make_vocabulary


def find_longest(data, name=''):
	longest_len = 0

	for i in trange(data.shape[0], desc='Finding longest for {}'.format(name)):
		if len(data.iloc[i].item()) > longest_len:
			longest_len = len(data.iloc[i].item())

	print('Longest length is {}.'.format(longest_len))


def main():
	config = get_args()
	dataset = Dataset(config)

	if os.path.isfile('{}vocab.pickle'.format(config.file_prefix)):
		pickle_in = open('{}vocab.pickle'.format(config.file_prefix), mode='rb')
		vocabulary = pickle.load(pickle_in)
		pickle_in.close()
	else:
		vocabulary = Vocabulary()
		vocabulary = make_vocabulary(dataset.train, vocabulary)
		pickle_out = open('{}vocab.pickle'.format(config.file_prefix), mode='wb')
		pickle.dump(vocabulary, pickle_out)
		pickle_out.close()

	print('\n\tVocabulary contains a total of {} words.'.format(len(vocabulary.token2idx)))
	find_longest(dataset.train, name='train')
	print()
	find_longest(dataset.test, name='test')

if __name__ == '__main__':
	main()
