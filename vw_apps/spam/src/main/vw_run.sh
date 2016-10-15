#!/usr/bin/env bash

#head -500 spam_v3_shuffled_2000.txt > spam_v3_test_500.txt && sed -i '1,+499d' spam_v3_shuffled_2000.txt

#sed -n '1,499p' spam_v3_test_500.txt

#cut -d ' ' -f 1 spam_v3_test_500.txt | sed -e 's/^-1/-1/' > labels

#head -500 spam_v3_shuffled_2000.txt > spam_v3_test_500.txt; tail +500 spam_v3_shuffled_2000.txt > spam_v3_shuffled_2000.txt.tmp; cp spam_v3_shuffled_2000.txt.tmp spam_v3_test_500.txt; rm spam_v3_shuffled_2000.txt.tmp

#awk 'NR%2000==1{x="F"++i;}{print > x}'  spam_v3_shuffled_2000.txt

#perf -ACC -files labels p_out.txt -t 0.5

#perf -PRE -files labels p_out.txt /dev/stdin

perf -ACC -files ../output/labels ../output/p_out.txt

perf -PRE -files ../output/labels ../output/p_out.txt

perf -REC -files ../output/labels ../output/p_out.txt


