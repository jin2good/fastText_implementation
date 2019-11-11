import argparse


def get_args():
	argp = argparse.ArgumentParser(description='fastText',
	                               formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	# Directories.
	argp.add_argument('--data_dir', type=str, default='./data')
	argp.add_argument('--file_prefix', type=str, default='ag_')

	return argp.parse_args()
