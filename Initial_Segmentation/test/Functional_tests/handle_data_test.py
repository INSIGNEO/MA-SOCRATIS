#Author: Michail Mamalakis
#Version: 0.1
#Licence:
#email:mmamalakis1@sheffield.ac.uk

from __future__ import division, print_function
from auto_segm import datasetnet, handle_data

dsn=datasetnet.datasetnet("train_pre","roi")
X, X_total, Y, contour_mask, storetxt = dsn.create_dataset()
h_d=handle_data.handle_data(X,Y)
training_augment, train_steps_per_epoch, validation_augment, val_steps_per_epoch =h_d.validation_data()
print("validation data handle test passed")
training_augment2, train_steps_per_epoch2 =h_d.no_validation_data()
print("no validation data handle test passed")
