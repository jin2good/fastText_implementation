from config import get_args
from dataset import Dataset
from vocabulary import Vocabulary, make_vocabulary


def main():
	config = get_args()
	dataset = Dataset(config)
	vocabulary = Vocabulary()
	vocabulary = make_vocabulary(dataset.train, vocabulary)

if __name__ == '__main__':
	main()
