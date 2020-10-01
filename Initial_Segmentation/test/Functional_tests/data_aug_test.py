#Author: Michail Mamalakis
#Version: 0.1/test
#Licence:
#email:mmamalakis1@sheffield.ac.uk

from auto_segm.regularization import data_augmentation
from auto_segm import  datasetnet, config
import numpy as np
import cv2
args = config.parse_arguments()
STORE_PATH=args.store_data_test
roi_shape=args.roi_shape_roi
original_image_shape=args.original_image_shape_roi
image_shape=args.image_shape_roi

dsnr=datasetnet.datasetnet('train','roi')
X, X_fullsize, Y, contour_mask, storetxt, images = dsnr.create_dataset()
# looop in the iterator to create all the augmented data
Xaug, Yaug= [], []
				
for i in data_augmentation(X,Y):
	Xaug.append(i[0])
	Yaug.append(i[1])
# add the initial data
Xaug.append(X)
Yaug.append(Y)
#reshape to (total_image,height,weight,channels)
Xaug1, Yaug2= np.asarray(Xaug) , np.asarray(Yaug)
Xaug1=Xaug1.reshape((Xaug1.shape[0]*Xaug1.shape[1],Xaug1.shape[2],Xaug1.shape[3],Xaug1.shape[4]))
Yaug2= Yaug2.reshape((Yaug2.shape[0]*Yaug2.shape[1],Yaug2.shape[2],Yaug2.shape[3],Yaug2.shape[4]))
print(Yaug2.shape, Xaug1.shape)

for o in range(0, len(Xaug1)-1, (len(X))):
	for i in range(0,len(X)):
		#print(Xaug1[i].shape)	
		#print(Yaug2[i].shape)
		pred1 = cv2.resize(Xaug1[i+o].reshape((image_shape, image_shape)), (original_image_shape, original_image_shape), cv2.INTER_NEAREST)
		pred2 = cv2.resize(Yaug2[i+o].reshape((roi_shape, roi_shape)), (original_image_shape, original_image_shape), cv2.INTER_NEAREST)	
		#print(pred1.shape)	
		#print(pred2.shape)
		str1=STORE_PATH + '/Augment/only_space_augment/%sAugmentROItrain%s.%s' % (o,i,'jpeg') 
		#str2=STORE_PATH + '/Augment/%sAugmentROIlabels%s.%s' % (o,i,'jpeg') 
		cv2.imwrite(str1,  pred1)
		#cv2.imwrite(str2,  pred2)
