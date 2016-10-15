#install.packages('ROCR')
library(ROCR)

# read dataset into dataframe
d = read.table('/Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/vw_apps/spam/src/spam_v3_shuffled.txt', header=F, sep="|", col.names=c("label", "text"))

plot(d)

print(sum(d$label == -1)) # spam 627
print(sum(d$label == 1)) # ham 1373

labels = d = read.table('/Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/vw_apps/spam/src/labels', header=F)
predictions = d = read.table('/Users/manpreet.singh/Sandbox/codehub/github/machinelearning/BeingDataScientist/vowpal_wabbit/vw_apps/spam/src/p_out.txt', header=F)
pred <- prediction(predictions, labels) # log odds and true values
perf <- performance(pred, measure = "tpr", x.measure = "fpr") 
plot(perf, col=rainbow(10))

acc.perf <- performance(pred, measure = "acc") 
plot(acc.perf, col=rainbow(10)) # 0.7 is really good cut off value

auc.perf = performance(pred, measure = "auc")
print(auc.perf@y.values) # 0.98
#plot(auc.perf, col=rainbow(10))

cm = as.matrix(table(Actual = labels, Predicted = predictions)) # create the confusion matrix
print(cm)

