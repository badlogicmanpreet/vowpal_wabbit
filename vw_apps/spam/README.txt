ADCG SS14 Challenge 02 - Spam Mails Detection
=============================================
# dataset directory contains Training, Testing files and label file for training set.
# extraction of subject and content is done using ExtractContent to prepare for VW
# extracted content is shuffled and stored as 'spam_v3_shuffled_2500.txt'
# above input is split into train and validate set of 2000, 500 records respectively, files in input directory
# actual test file from kaggle without labels is 'kaggle_test_set_1827.txt'

# VWFormatter is used for cleanup and formatting emails to VW input format, 'spam_v3.txt' file is generated and shuffled
to create 'spam_v3_shuffled_2500.txt'
# labels are converted to 1 and -1, where -1 represents spam and 1 represents ham
# vw_run.py shows various models run with sqaured, logisitic and hinge loss. Logistic and Hinge does good as expected.
# predictions are stored in p_out as log values, but have been converted to binary for kaggle using --binary flag. Files
are present in output directory
# true labels are stored in labels file
# KaggleResult.py converts the the output to desired kaggle format

# All the models are stored in model directory under output

# Plots_Metrics.R helps to plot data and curves

*****************Metrics*****************
Accuracy achieved so far is 67.2
Precision - 0.94766
Recall - 0.98851
** Used perf tool to get the values for ACC, precision and recall
perf -ACC -files labels p_out.txt
perf -PRE -files labels p_out.txt
perf -REC -files labels p_out.txt

AUC - 0.9839591 on validation set
From curve i see, 0.7 threshold (log value) is really good cut off value for classification

*****************Plots*****************
# Plots are in plots directory
![ScreenShot](https://github.com/badlogicmanpreet/vowpal_wabbit/blob/ms_dev/vw_apps/spam/src/plots/AccuracyPlot_Valid.png)

*****************TODO*****************
If i use --binary flag, on what bases does it choose right probability threshold for classification?

1. Use hinge loss
2. Adjust weights
3. Work on data randomization




