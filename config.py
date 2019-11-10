import argparse


def get_args():
	argp = argparse.ArgumentParser(description='fastText',
	                               formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	# Directories.
	argp.add_argument('--data_dir', type=str, default='./data')
	argp.add_argument('--file_prefix', type=str, default='ag_')

	# Process arguments.
	argp.add_argument('--use_preprocessed', action='store_true', default=False)

	return argp.parse_args()
