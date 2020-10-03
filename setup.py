print("\n show images of rock , paper, scissors and NOTHING in the same order for data collection\n") 

import os
print("\nWelcome to the setup!")
try:
    os.system('rmdir train_data')
except:
    os.system('rm -r train_data')

print("\nremoved older data\n")




try:
    os.system('python collect_images.py rock 100')
    os.system('python collect_images.py paper 100')
    os.system('python collect_images.py scissors 100')
    os.system('python collect_images.py none 100')
except:
    os.system('collect_images.py rock 100')
    os.system('collect_images.py paper 100')
    os.system('collect_images.py scissors 100')
    os.system('collect_images.py none 100')


try:
    os.system('python train.py')
except:
    os.system('train.py')