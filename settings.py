import os
# COMPUTER_NAME = os.environ['COMPUTERNAME']
# print("Computer: ", COMPUTER_NAME)

WORKER_POOL_SIZE = 8

TARGET_VOXEL_MM = 1.00
MEAN_PIXEL_VALUE_NODULE = 41
LUNA_SUBSET_START_INDEX = 0
SEGMENTER_IMG_SIZE = 320

BASE_DIR_SSD = "/Users/chylvina/WorkSpace/GitHub/kaggle_ndsb2017/tmp/"
BASE_DIR = "/Users/chylvina/WorkSpace/GitHub/kaggle_ndsb2017/tmp/"
EXTRA_DATA_DIR = "resources/"
NDSB3_RAW_SRC_DIR = BASE_DIR + "ndsb_raw/"
LUNA16_RAW_SRC_DIR = BASE_DIR + "luna_raw/"

NDSB3_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "ndsb3_extracted_images/"
LUNA16_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "luna16_extracted_images/"
NDSB3_NODULE_DETECTION_DIR = BASE_DIR_SSD + "ndsb3_nodule_predictions/"
LUNA_NODULE_DETECTION_DIR = BASE_DIR_SSD + "luna_nodule_predictions/"

