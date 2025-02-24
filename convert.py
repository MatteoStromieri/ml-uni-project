#!/usr/bin/env python

import utils

tracks = utils.load('./fma_metadata/tracks.csv')
subset = tracks.index[tracks['set', 'subset'] <= 'medium']
labels = tracks.loc[subset, ('track', 'genre_top')]
labels.name = 'genre'
labels =labels =  labels.str.lower()
labels.to_csv('./fma_metadata/train_labels.csv', header=True)

# features = utils.load('./fma_metadata/features.csv')
# medium = features.loc[subset]
# medium.to_csv('./fma_metadata/features_medium.csv', header=True)


