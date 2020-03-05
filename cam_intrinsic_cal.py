# load modules
import argparse
import glob
import os
from tqdm import tqdm
import numpy as np
import cv2


__author__ = "Ali Alizadeh"
__email__ = 'aalizade@ford.com.tr / a.alizade@live.com'
__license__ = 'AA_intrinsic_cal'

def parse_arguments():
    parser = argparse.ArgumentParser(description='Multi-camera intrinsic calibration')
    parser.add_argument('-i', '--input_dir', default='multi_cam', help='Parent directory of the original images')
    parser.add_argument('-o', '--output_dir', default='multi_cam', help='Directory of the undistorted images')
    args = parser.parse_args()
    return args

def main(in_dir, out_dir):
    for dir in tqdm(os.listdir(in_dir)):
        mtx = np.load(os.path.join(in_dir, 'mtx.npy'))
        dist = np.load(os.path.join(in_dir, 'dist.npy'))
        images = glob.glob(in_dir + '/' + os.path.join(dir, '*.png'))
        print(images)
        for fname in tqdm(images):
            img = cv2.imread(fname)
            # undistort
            dst = cv2.undistort(img, mtx, dist, None, mtx)
            # save image
            cv2.imwrite(os.path.join(out_dir + '/' + dir, fname.split('/')[-1]), dst)

if __name__ == '__main__':
    args = parse_arguments()
    in_dir = args.input_dir
    out_dir = args.output_dir
    main(in_dir, out_dir)



