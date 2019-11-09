import os
import pdb
import time

import pandas as pd


class Dataset():
	def __init__(self, config):
		self.config = config
		self.load()

	def load(self):
		self.train = pd.read_csv(os.path.join(self.config.data_dir, 'train.csv'), header=None, engine='python').iloc[:, -1]
		self.test = pd.read_csv(os.path.join(self.config.data_dir, 'test.csv'), header=None, engine='python').iloc[:, -1]

		pdb.set_trace()

		for i in range(self.train.shape[0]):
			self.train.iloc[i] = self.train.iloc[i].lower().replace('\\', ' ')

		for i in range(self.test.shape[0]):
			self.test.iloc[i] = self.test.iloc[i].lower().replace('\\', ' ')
