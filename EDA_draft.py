import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

pd.set_option('display.max_columns', None)

data_path = 'C:\\Users\\CHANJA8\\OneDrive - Orient Overseas Container Line Ltd\\Projects\\Personal\\20181112_driven_data_predict_disease_spread\\data\\'

# train_feature = pd.read_csv(data_path + 'dengue_features_train.csv')
# train_labels = pd.read_csv(data_path + 'dengue_labels_train.csv')
# len(train_feature)
# len(train_labels)
#
# # Merge train_feature and train_labels
# train_df = train_feature.merge(train_labels, how='left', on=['city', 'year', 'weekofyear']).fillna(0)
# len(train_df)
# train_df.head()
# train_df.info()
# train_df.to_csv(data_path + 'train_df.csv', index=False)

# Read train_df
train_df = pd.read_csv(data_path + 'train_df.csv')


# TODO: Handle missing value (now just fillna(0))
