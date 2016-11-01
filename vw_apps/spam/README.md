# ADCG SS14 Challenge 02 - Spam Mails Detection

## Notes 
1. Dataset directory contains Training, Testing files and label file for training set.
2. Extraction of subject and content is done using ExtractContent to prepare for VW
3. Extracted content is shuffled and stored as 'spam_v3_shuffled_2500.txt'
4. Above input is split into train and validate set of 2000, 500 records respectively, files in input directory
5. Actual test file from kaggle without labels is 'kaggle_test_set_1827.txt'
7. VWFormatter is used for cleanup and formatting emails to VW input format, 'spam_v3.txt' file is generated and shuffled
   to create 'spam_v3_shuffled_2500.txt'
8. Labels are converted to 1 and -1, where -1 represents spam and 1 represents ham
9. vw_run.py shows various models run with sqaured, logisitic and hinge loss. Logistic and Hinge does good as expected.
10. Predictions are stored in p_out as log values, but have been converted to binary for kaggle using --binary flag. Files
   are present in output directory
11. True labels are stored in labels file
12. KaggleResult.py converts the the output to desired kaggle format

#####  All the models are stored in model directory under output

#####  Plots_Metrics.R helps to plot data and curves

##### *****************Metrics*****************
1. Accuracy achieved so far is 67.2
2. Precision - 0.94766
3. Recall - 0.98851
4. perf -ACC -files labels p_out.txt
5. perf -PRE -files labels p_out.txt
6. perf -REC -files labels p_out.txt

AUC - 0.9839591 on validation set
From curve i see, 0.7 threshold (log value) is really good cut off value for classification
![Accuracy Curve](https://github.com/badlogicmanpreet/vowpal_wabbit/blob/ms_dev/vw_apps/spam/src/plots/AccuracyPlot_Valid.png)
![Area Curve](https://github.com/badlogicmanpreet/vowpal_wabbit/blob/ms_dev/vw_apps/spam/src/plots/AreaCurve_Valid.png)
![Dataset](https://github.com/badlogicmanpreet/vowpal_wabbit/blob/ms_dev/vw_apps/spam/src/plots/Dataset.png)

##### *****************TODO*****************
If i use --binary flag, on what bases does it choose right probability threshold for classification?

1. Use hinge loss
2. Adjust weights
3. Work on data randomization




