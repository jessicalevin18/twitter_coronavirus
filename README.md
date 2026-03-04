# Coronavirus twitter analysis

Developed a MapReduce procedure to analyze all geotagged tweets sent in 2020, about 1.1 billion tweets. Then, I examined how coronavirus related hashtags were used on twitter across different languages and countries to provide insights on the frequency and spread of social media discourse. 

## How it works 
### MapReduce
First, the mapper outputs two datasets for each day of the year. One that contains the number of tweets by country and one organized by language. Then, the reduce step creates two combined files: one with tweets organized by language and one with tweets organized by country. 

### Alternative MapReduce
Using the combined files from the mapping step, alternative mapreduce creates a dataset organized by the number of each hashtags per day in 2020. Then the script uses matplotlib functions to plot the data. These visualizations display the count of a hashtag each day in 2020.

Sample command used:
```
python alternative_reduce.py  --input_path outputs --output_path combined_hashtags.json  --hashtags "#flu" "#doctor" "#coronavirus" "#corona" --plot_output hashtag_plot.png
```

## Generated Plots

### Counts of Tweets with #coronavirus by Top 10 Countries
<img src=src/coronavirus_country.png />

### Counts of Tweets with #coronavirus by Top 10 Languages
<img src=src/coronavirus_lang.png />

### Counts of Tweets with #코로나바이러 by Top 10 Countries
<img src=src/코로나바이러스_country.png />

### Counts of Tweets with #코로나바이러 by Top 10 Languages
<img src=src/코로나바이러스_lang.png />

### Counts of the hashtags #flu, #doctor, #coronavirus, and #corona during 2020
<img src=src/hashtag_plot.png />
