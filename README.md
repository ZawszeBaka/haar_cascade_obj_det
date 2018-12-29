# Haar Cascade Training

## Gathering image from ImageNet (from urls )
'''
python3 gathering_pics_from_urls.py
'''

## Remove ugly images. Make sure u have already placed ugly images in directory 'uglies'
python3 remove_ugly_imgs.py

### Creating background text
python3 creating_bgtxt.py

### Creating positive images
python3 creating_pos_image.py

### Make sure creating_pos_image works properly
python3 check_info_lst.py

### Create positive vectors
#### -info <info file including information of positive images>
#### -num <max is num of pos images in info directory>
#### -w <recommend using 20>
#### -h <recommend using 20>

#### Note: copy info.lst into info/
'''
opencv_createsamples -info info/info.lst -num 1000 -w 50 -h 50 \
-vec positives.vec
'''

### start training
### -data <directory to store Haar classifier
### -bg <info of negative images>
### -numPos <max is value of -num>
### -numNeg <half of -numPos>
### empty the folder data/
'''
opencv_traincascade -data data -vec positives.vec  -bg bg.txt \
-numPos 1000 -numNeg 600 -numStages 20 -w 50 -h 50 \
-featureType HAAR \
-precalcValBufSize 1024 -precalcIdxBufSize 1024 \
-minHitRate 0.999 -maxFalseAlarmRate 0.2
'''
#####refs:http://answers.opencv.org/question/64431/number-of-stages-or-maxfalsealarmrate/
  
### A minHitRate is the parameter that ensures us that our positive training data yields at least a decent detection output. We do not want to lower this value to much. For example a value of 0.8 would mean that 20% of our positive object training data can be misclassified, which would be a disaster. Using a rate of 1% misclassification is a common value used in research.
### A maxFalseAlarmRate is used to define how much features need to be added. Actually we want each weak classifier to have a very good hit rate on the positives, and then to allow them to remove negative windows, as fast as possible, but doing better then random guessing. 0.5 means you apply a random guess, better than that means you successfully remove negative windows as negatives very early using only a few feature evaluations, letting other negatives be discarded by the following stages.


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


# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc



----------------------------------------------------------------


Refs:
  https://memememememememe.me/post/training-haar-cascades/
  https://github.com/mrnugget/opencv-haar-classifier-training

[=] Haar Cascade Training

# gathering image from ImageNet (from urls )
''' python3 gathering_pics_from_urls.py '''

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
