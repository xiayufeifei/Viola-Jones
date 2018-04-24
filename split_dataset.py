
import numpy as numpy
import os
from sklearn.model_selection import train_test_split

DataPath = 'data/large/'

def split_data(source, train_dest, test_dest):
    fileslist = os.listdir(source)
    fileslist_train, fileslist_test = train_test_split(fileslist, test_size=0.6, shuffle=True)

    os.makedirs(train_dest, exist_ok=True)
    os.makedirs(test_dest, exist_ok=True)

    for f in fileslist_train:
        filename = os.path.split(f)[-1]
        os.rename(os.path.join(source, filename), os.path.join(train_dest, filename))
        
    for f in fileslist_test:
        filename = os.path.split(f)[-1]
        os.rename(os.path.join(source, filename), os.path.join(test_dest, filename))

if __name__ == '__main__':
    split_data(DataPath + 'faces', DataPath + 'train/faces', DataPath + 'test/faces')
    split_data(DataPath + 'non-faces', DataPath + 'train/non-faces', DataPath + 'test/non-faces')
