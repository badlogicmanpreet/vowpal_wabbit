# RCV1 Example
import os

#https://github.com/JohnLangford/vowpal_wabbit/wiki/Tutorial
if __name__ == '__main__':
    # train the model
    #os.system("/usr/local/bin/vw /Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/spamdetection/dataset/house_dataset -l 10 -c --passes 25 --holdout_off -f house.model")

    # learn and predict
    #os.system("/usr/local/bin/vw /Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/spamdetection/dataset/house_dataset -p /dev/stdout")

    # no learning, use the model and predict
    os.system("/usr/local/bin/vw -i /Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/spamdetection/house.model -t /Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/spamdetection/dataset/house_dataset -p /dev/stdout")
