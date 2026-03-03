# Coronavirus twitter analysis

Used MapReduce procedure to analyze all geotagged tweets sent in 2020 and examine how coronavirus related hashtags were used on social media across different languages and countries. 

## How it works 
### MapReduce
First, running the mapper outputs two datasets for each day of the year: one that contains the number of tweets by country and one organized by language. Then the reduce step creates two combined files: one with tweets organized by language and one with tweets organized by country. 

### Alternative MapReduce
Using the combined files from the mapping step, alternative mapreduce creates a dataset organized by the number of each hashtags per day in 2020. Then the program uses matplotlib functions to plot the data. These visualizations display the count of a hashtag each day in 2020.


## Generated Plots

### Counts of Tweets with #coronavirus by Top 10 Countries
<img src=#코로나바이러스_lang.png />

### Counts of Tweets with #coronavirus by Top 10 Languages

### Counts of Tweets with #코로나바이러 by Top 10 Countries

### Counts of Tweets with #코로나바이러 by Top 10 Languages

### Counts of the hashtags #flu, #doctor, #coronavirus, and #corona during 2020
<img src=#coronavirus_lang.png />
