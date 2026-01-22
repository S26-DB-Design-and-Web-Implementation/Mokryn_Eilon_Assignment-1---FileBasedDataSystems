#Air Quality in NYC
#Ed Workspaces Link: https://edstem.org/us/courses/91931/workspaces/pknWwphmUbjOtXxD3IagZTusihZfWhQ8

#Why I chose this data set
I chose the Air Quality dataset from #https://data.cityofnewyork.us/ 
because it is an important topic that affects over 8 million people.
When I picked the topic I didn't realize that it would be challenging for me to pick questions,
and brainstorming which questions to ask, interestingly, took the majority of my time for the assignment

#First question: How many location types are boroughs?
The output was 880. Obviously NYC only has 5 boroughs, which begs the question what does the answer actually mean?
Some tests were done at specific neighborhoods, and some tests were done for entire boroughs. 
Hence, the dataset has overlapping data, which we also can infer given the dataset includes tests that 
were done over decades.

#Second question: How many tests were done in 2005?
The output was 417. That is an average of over 1.1 tests a day. 
The dataset is tracking the time period of the tests, so this question is simple to answer

#Third question: Were more tests done in 2005 or all other years combined?
Output: More tests were done in other time periods combined:  18445
Expected that more tests would be done in all other years combined than just 2005. 
I was able to manipulate the data in the Time Periods column to simply create
a variable that tracks all the tests that were done in other years/periods than 2005.


#I wish I could answer the quetsion "How long does it take to conduct each test?"
I cannot answer this question using the data because there is no indication or measurement of 
the time it takes to conduct each test.
It would be misleading to assume that a certain test takes less time than another because there are 
more of that test in certain periods of time (or on average) than other tests.

