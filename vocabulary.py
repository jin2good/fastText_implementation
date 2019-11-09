import pdb


# Basic punctuation declared as global variables.\
COMMA = ','
PERIOD = '.'
QUESTION = '?'
COLON = ':'
SEMICOLON = ';'
EXCLAMATION = '!'
HYPHEN = '-'

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
		assert self.idx2token[index], 'Invalid index provided.'

	def get_index(self, token):
		assert self.token2idx[token], 'Invalid token provided.'


def punctuation_split(sentence):
	sentence.replace('.', ' . ')
	sentence.replace(',', ' , ')
	sentence.replace('!', ' ! ')
	sentence.replace('?', ' ? ')
	sentence.replace(';', ' ; ')
	sentence.replace(':', ' : ')

	return sentence


def make_vocabulary(data, vocab):
	vocab.new_token(COMMA)
	vocab.new_token(PERIOD)
	vocab.new_token(QUESTION)
	vocab.new_token(COLON)
	vocab.new_token(SEMICOLON)
	vocab.new_token(EXCLAMATION)
	vocab.new_token(HYPHEN)

	for i in range(data.shape[0]):
		data[i] = punctuation_split(data[i])
		for word in data[i].split():
			pdb.set_trace()
			vocab.new_token(word)

	return vocab
