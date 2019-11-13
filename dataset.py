import os
import pdb
import time

import pandas as pd
from tqdm import trange


class Dataset():
	def __init__(self, config, mode='train'):
		self.config = config
		self.mode = mode
		print('Loading dataset...')
		self.load()
		self.punctuation_split()
		self.find_longest()

	def load(self):
		if os.path.isfile(os.path.join(self.config.data_dir, '{}train_preproc.csv'.format(self.config.file_prefix))):
			print('\tUsing preprocessed data.')
			if self.mode == 'train':
				train_dir = os.path.join(self.config.data_dir, '{}train_preproc.csv'.format(self.config.file_prefix))
				self.data = pd.read_csv(train_dir, header=None, engine='python').iloc[:, -1]
				print('\ttrain.shape = {}'.format(self.data.shape))
			else:
				test_dir = os.path.join(self.config.data_dir, '{}test_preproc.csv'.format(self.config.file_prefix))
				self.data = pd.read_csv(test_dir, header=None, engine='python').iloc[:, -1]
				print('\ttest.shape = {}'.format(self.data.shape))
		else:
			print('\tCreating new data...')
			if self.mode == 'train':
				train_dir = os.path.join(self.config.data_dir, '{}train.csv'.format(self.config.file_prefix))
				self.data = pd.read_csv(train_dir, header=None, engine='python').iloc[:, -1]

				for i in trange(self.data.shape[0], desc='Replacing forward slashes for train'):
					self.data.iloc[i] = self.data.iloc[i].lower().replace('\\', ' ')

				self.data.to_csv(os.path.join(self.config.data_dir, '{}train_preproc.csv'.format(self.config.file_prefix)), header=None, index=False)
			else:
				test_dir = os.path.join(self.config.data_dir, '{}test.csv'.format(self.config.file_prefix))
				self.data = pd.read_csv(test_dir, header=None, engine='python').iloc[:, -1]

				for i in trange(self.data.shape[0], desc='Replacing forward slahes for test'):
					self.data.iloc[i] = self.data.iloc[i].lower().replace('\\', ' ')

				self.data.to_csv(os.path.join(self.config.data_dir, '{}test_preproc.csv'.format(self.config.file_prefix)), header=None, index=False)

	def find_longest(self):
		longest = 0

		if self.mode == 'train':
			for i in trange(self.data.shape[0], desc='Finding longest for train...'):
				if len(self.data[i].split()) > longest:
					longest = len(self.data[i].split())

			self.longest = longest
			print('\tLongest length for train is {}.'.format(self.longest))
		else:
			for i in trange(self.data.shape[0], desc='Finding longest for test...'):
				if len(self.data[i].split()) > longest:
					longest = len(self.data[i].split())

			self.longest = longest
			print('\tLongest length for test is {}.'.format(self.longest))

	def punctuation_split(self):
		"""
		Adds extra space around each punctuation mark
	  	so that we can run the split function and also
	 	return the punctuation tokens.
		"""
		for i in range(self.data.shape[0]):
			self.data[i] = self.data[i].replace('.', ' . ')
			self.data[i] = self.data[i].replace(',', ' , ')
			self.data[i] = self.data[i].replace('!', ' ! ')
			self.data[i] = self.data[i].replace('?', ' ? ')
			self.data[i] = self.data[i].replace(';', ' ; ')
			self.data[i] = self.data[i].replace(':', ' : ')
