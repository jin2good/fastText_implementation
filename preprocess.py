import pdb

import numpy as np
from tqdm import trange


UNK = '<UNK>'

def map2idx(sentence, vocab):
	mapped = []

	for token in sentence.split():
		try:
			mapped.append(vocab.get_index(token))
		except KeyError:
			mapped.append(vocab.get_index(UNK))

	return mapped


def word2token(dataset, vocab, mode='train'):
	if mode == 'train':
		train = dataset.data
		tokenized = np.zeros(shape=(train.shape[0], dataset.longest)) # Create template for mapping.

		for i in trange(tokenized.shape[0], desc='Mapping tokens to indices...'):
			sentence = train[i]
			mapped = map2idx(sentence, vocab)
			tokenized[i, :len(mapped)] = mapped
	else:
		test = dataset.data
		tokenized = np.zeros(shape=(test.shape[0], dataset.longest)) # Create template for mapping.

		for i in trange(tokenized.shape[0], desc='Mapping tokens to indices...'):
			sentence = test[i]
			mapped = map2idx(sentence, vocab)
			tokenized[i, :len(mapped)] = mapped

	return tokenized


def preprocess(data, vocab):
	data = data[0].to_numpy()
	new_data = np.array()
