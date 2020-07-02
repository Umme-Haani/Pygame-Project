import os

IMAGE_SIZE=128
SCREEN_SIZE=512
NUM_TILE_SIZE=4
NUM_TILE_TOT=16
MARGIN=4

ASSET_DIR='assets'
ASSET_FILE=[x for x in os.listdir(ASSET_DIR) if x[-3:].lower()=='png']
#print(len(ASSET_FILE))
assert len(ASSET_FILE) == 8