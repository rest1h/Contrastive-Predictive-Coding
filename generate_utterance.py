# Generates train.txt, eval.txt, validation.txt, which
# are just lists of utterance ids. This script looks
# at all the .txt files within LibriSpeech to extract
# the ids and write the files.
# An utterance id is a string like "61-70968-0009".

import os

train_root = "LibriSpeech/train-clean-100/"  # , 'train-clean-360/', 'train-other-500/'
dev_root = "LibriSpeech/dev-clean/"  # , 'LibriSpeech/dev-other/'
test_root = "LibriSpeech/test-clean/"


def generate_list(root_dir: str, filename: str) -> None:
    """ get the utterance ids """
    utterance_ids = []
    for sub_dir, _, files in os.walk(root_dir):
        for filename in [file for file in files if file.endswith(".txt")]:
            with open(os.path.join(sub_dir, filename)) as f:
                ids = [l.split(" ")[0] + "\n" for l in f.readlines()]
                utterance_ids.extend(ids)

    # write them
    with open(filename, "w") as of:
        of.writelines(utterance_ids)


if __name__ == "__main__":
    generate_list(train_root, "LibriSpeech/list/train.txt")
    generate_list(test_root, "LibriSpeech/list/eval.txt")
    generate_list(dev_root, "LibriSpeech/list/validation.txt")
