Refs:
  https://memememememememe.me/post/training-haar-cascades/


[=] Haar Cascade Training

# gathering image from ImageNet (from urls )
'''python python3 gathering_pics_from_urls.py '''

# remove ugly images. make sure u have already placed ugly images in directory 'uglies'
python3 remove_ugly_imgs.py

# creating bg text
python3 creating_bgtxt.py

#
python3 creating_pos_image.py

# make sure creating_pos_image works properly
python3 check_info_lst.py

# Create positive vectors
# -info <info file including information of positive images>
# -num <max is num of pos images in info directory>
# -w <recommend using 20>
# -h <recommend using 20>
#
# Note: copy info.lst into info/
opencv_createsamples -info info/info.lst -num 1000 -w 50 -h 50 \
-vec positives.vec

# start training
# -data <directory to store Haar classifier
# -bg <info of negative images>
# -numPos <max is value of -num>
# -numNeg <half of -numPos>
# empty the folder data/
opencv_traincascade -data data -vec positives.vec  -bg bg.txt \
-numPos 1000 -numNeg 600 -numStages 20 -w 50 -h 50 \
-featureType HAAR \
-precalcValBufSize 1024 -precalcIdxBufSize 1024 \
-minHitRate 0.999 -maxFalseAlarmRate 0.2

refs:http://answers.opencv.org/question/64431/number-of-stages-or-maxfalsealarmrate/
'''
A minHitRate is the parameter that ensures us that our positive training data yields at least a decent detection output. We do not want to lower this value to much. For example a value of 0.8 would mean that 20% of our positive object training data can be misclassified, which would be a disaster. Using a rate of 1% misclassification is a common value used in research.
A maxFalseAlarmRate is used to define how much features need to be added. Actually we want each weak classifier to have a very good hit rate on the positives, and then to allow them to remove negative windows, as fast as possible, but doing better then random guessing. 0.5 means you apply a random guess, better than that means you successfully remove negative windows as negatives very early using only a few feature evaluations, letting other negatives be discarded by the following stages.
'''

# recommend using when training with big data
nohup opencv_traincascade -data data -vec positives.vec  -bg bg.txt \
-numPos 1000 -numNeg 600 -numStages 20 -w 50 -h 50 \
-featureType HAAR -mode ALL \
-precalcValBufSize 1024 -precalcIdxBufSize 1024 \
-minHitRate 0.995 -maxFalseAlarmRate 0.5 &

## MEANINGS: 
-minHitRate is set to 0.995 by default. This means that for this current
model, it allows 5 out of 1000 positive samples to get wrongly classified 
during the training process
-maxFalseAlarmRate is set to 0.5 by default. Each stage needs to reach 
an individual false acceptance rate (good classification of negs)




### 
Gathering more negative images 
Combine between game scene and gathered images 
Mostly, 7,500 pos , 3,000 neg 

### 
saved !! 
