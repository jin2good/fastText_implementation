import os
import pdb
import time

import pandas as pd
from tqdm import trange


class Dataset():
	def __init__(self, config):
		self.config = config
		print('Loading dataset...')
		self.load()

	def load(self):
		if self.config.use_preprocessed:
			print('\tUsing preprocessed data.')
			self.train = pd.read_csv(os.path.join(self.config.data_dir, '{}train_preproc.csv'.format(self.config.file_prefix)), header=None, engine='python')
			self.test = pd.read_csv(os.path.join(self.config.data_dir, '{}test_preproc.csv'.format(self.config.file_prefix)), header=None, engine='python')
			print('\ttrain.shape = {}\ttest.shape = {}'.format(self.train.shape, self.test.shape))
		else:
			print('\tCreating new data...')
			self.train = pd.read_csv(os.path.join(self.config.data_dir, '{}train.csv'.format(self.config.file_prefix)), header=None, engine='python').iloc[:, -1]
			self.test = pd.read_csv(os.path.join(self.config.data_dir, '{}test.csv'.format(self.config.file_prefix)), header=None, engine='python').iloc[:, -1]

			# The AG News data contains unnecessary forward slashes in the training and test data. We'll remove those with
			#   the following two for loops.
			for i in trange(self.train.shape[0], desc='Replacing forward slashes for train'):
				self.train.iloc[i] = self.train.iloc[i].lower().replace('\\', ' ')

			print()

			for i in trange(self.test.shape[0], desc='Replacing forward slahes for test'):
				self.test.iloc[i] = self.test.iloc[i].lower().replace('\\', ' ')

			self.train.to_csv(os.path.join(self.config.data_dir, '{}train_preproc.csv'.format(self.config.file_prefix)), header=None, index=False)
			self.test.to_csv(os.path.join(self.config.data_dir, '{}test_preproc.csv'.format(self.config.file_prefix)), header=None, index=False)
