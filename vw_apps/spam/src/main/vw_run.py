import os
from random import shuffle

#https://github.com/JohnLangford/vowpal_wabbit/wiki/Tutorial
if __name__ == '__main__':
    # 0.54844 accuracy
    #os.system("/usr/local/bin/vw -d spam_v2.txt -k -f spamv1.vw --noconstant -b 14 --ngram B2 --binary")
    #os.system("/usr/local/bin/vw -t -d spam_test_v1.txt -i spamv1.vw --binary --predictions p_out.txt")

    # 0.54735 accuracy
    #os.system("/usr/local/bin/vw -d spam_v2.txt -k --loss_function logistic -f spamv2.vw --noconstant -b 14 --ngram B2 --binary")
    #os.system("/usr/local/bin/vw -t -d spam_test_v1.txt -i spamv2.vw --binary --predictions p_out.txt")

    # 0.54953 accuracy
    #os.system("/usr/local/bin/vw -d spam_v2.txt -k --loss_function hinge -f spamv3.vw --noconstant -b 14 --ngram B2 --binary")
    #os.system("/usr/local/bin/vw -t -d spam_test_v1.txt -i spamv3.vw --binary --predictions p_out.txt")

    #  0.54844 accuracy
    #os.system("/usr/local/bin/vw -d spam_v3.txt -c -k --passes 300 -b 24 --ngram 7 -f spamv5.vw --binary")
    #os.system("/usr/local/bin/vw -t -d kaggle_test_set_1827.txt -i spamv5.vw --binary --predictions p_out.txt")


    # shuffle dataset
    # import random
    # lines = open('spam_v3.txt', 'r').readlines()
    # random.shuffle(lines)
    # open('spam_v3_shuffled_2000.txt', 'w').writelines(lines)

    #  0.57909 accuracy
    #os.system("/usr/local/bin/vw -d spam_v3_shuffled_2000.txt -c -k -b 10 --ngram 2 -f spamv6.vw --binary")
    #os.system("/usr/local/bin/vw -t -d kaggle_test_set_1827.txt -i spamv6.vw --binary --predictions p_out.txt")

    # use spam iq model for prediction - accuracy 0.67214
    #os.system("/usr/local/bin/vw -t -d kaggle_test_set_1827.txt -i model_spam_community.vw --binary --predictions p_out.txt")

    # 0.54735 accuracy
    #os.system("/usr/local/bin/vw -d spam_v3_shuffled_2000.txt -k --loss_function logistic -f spam_final.vw --noconstant -b 14 --ngram 2 --link logistic")
    os.system("/usr/local/bin/vw -t -d spam_v3_test_500.txt -i spam_final.vw --predictions p_out.txt")
    #os.system("/usr/local/bin/vw -t -d kaggle_test_set_1827.txt -i spam_final.vw --predictions p_out_kaggle.txt")
