#Author: Michail Mamalakis
#Version: 0.2
#Licence:
#email:mmamalakis1@sheffield.ac.uk

from __future__ import division, print_function
from auto_segm import main


mn=main.main('test','lge_unet_ss_2')

# run test of main segmentation based on roi 'ESendo_dout_4' 
mn.test_main()

