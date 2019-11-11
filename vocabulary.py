import pdb

from tqdm import trange


# Basic punctuation declared as global variables.\
COMMA = ','
PERIOD = '.'
QUESTION = '?'
COLON = ':'
SEMICOLON = ';'
EXCLAMATION = '!'
HYPHEN = '-'
PAD = '<PAD>'

class Vocabulary():
	"""
	Class that contains our vocabulary.
	|
	|
	|  Attributes:
	|  | token2idx: Dictionary whose keys are tokens and values are corresponding indices.
	|  | idx2token: Analogous to token2idx.
	|
	|  Methods:
	|  | new_token: Adds new token to vocabulary.
	|  | get_token: Retrieves token corresponding to given index.
	|  | get_index: Retrieves index corresponding to given token.s
	"""
	def __init__(self):
		self.token2idx = {}
		self.idx2token = {}

	def new_token(self, token):
		if token not in self.token2idx:
			idx = len(self.token2idx)
			self.token2idx[token] = idx
			self.idx2token[idx] = token

		return self.token2idx, self.idx2token

	def get_token(self, index):
		return self.idx2token[index]

	def get_index(self, token):
		return self.token2idx[token]


def punctuation_split(sentence):
	"""
	Adds extra space around each punctuation mark
	  so that we can run the split function and also
	  return the punctuation tokens.
	"""
	sentence = sentence.replace('.', ' . ')
	sentence = sentence.replace(',', ' , ')
	sentence = sentence.replace('!', ' ! ')
	sentence = sentence.replace('?', ' ? ')
	sentence = sentence.replace(';', ' ; ')
	sentence = sentence.replace(':', ' : ')

	return sentence


def make_vocabulary(data, vocab):
	vocab.new_token(PAD)
	vocab.new_token(COMMA)
	vocab.new_token(PERIOD)
	vocab.new_token(QUESTION)
	vocab.new_token(COLON)
	vocab.new_token(SEMICOLON)
	vocab.new_token(EXCLAMATION)
	vocab.new_token(HYPHEN)

	for i in trange(data.shape[0], desc='Creating vocabulary'):
		data.iloc[i] = punctuation_split(data.iloc[i].item())
		for word in data.iloc[i].item().split():
			vocab.new_token(word)

	return vocab
