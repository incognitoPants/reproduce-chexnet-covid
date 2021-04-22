import cxr_dataset as CXR
import eval_model as E
import model as M
import torch
import time

def run():
    torch.multiprocessing.freeze_support()
    print('loop')


if __name__ == '__main__': #Only for Win10. Remove if running on Linux
    start = time.time()
    run()
    # you will need to customize PATH_TO_IMAGES to where you have uncompressed
    # NIH images
    PATH_TO_IMAGES = "./images"
    WEIGHT_DECAY = 1e-4
    LEARNING_RATE = 0.01
    preds, aucs = M.train_cnn(PATH_TO_IMAGES, LEARNING_RATE, WEIGHT_DECAY)
    end_time = time.time()
    print('Total run time: ', end_time - start)
