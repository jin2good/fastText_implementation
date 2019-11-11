import numpy as np
from tqdm import tqdm

def preprocess(data, vocab):
	data = data[0].to_numpy()
	new_data = np.array()
