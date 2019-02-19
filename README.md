# Predicting Genre using Machine Learning

## Abstract 
We are interested in accurately predicting the genre of songs using numerous methods of machine learning. Using the Spotify and Genius API, we acquired audio features and lyrics of songs from three genres: metal, rap, and country. Once the datapreprocessing was finished, we were interested at two things: what topics were prevalent in all three genres using topic modeling (LDA and NMF) and what methods would provide us with the best prediction (Gradient Boosting, Random Forest, Logistic Regression, and K-Nearest Neighbors). We would test our prediction on audio features, lyrics, and an ensemble of the two to answer our question.

## Contributors
- Grant Nolasco
- Candace McKeag 

## Tasks
### Data Acquistion

First, we generated samples of songs from the three genres using the Spotify API search engine. After searching through 5000 pages, we were able to get 4629 unique rap songs, 4476 unique country songs, and 4403 unique metal songs. The features given to us from Spotify API that we plan on using for our analysis are

- duration_ms (The duration of the track in milliseconds)
- key (The estimated overall key of the track)
- mode (The type of scale from which its melodic content is derived)
- time_signature (The time signature is a notational convention to specify how many beats are in each bar)
- acousticness (Confidence measure from 0.0 to 1.0 of whether the track is acoustic)
- danceability (Danceability describes how suitable a track is for dancing) 
- energy (Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity)
- instrumentalness (Predicts whether a track contains no vocals)
- loudness (The overall loudness of a track in decibels)
- speechiness (Speechiness detects the presence of spoken words in a track)
- valence (A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track)
- tempo (The overall estimated tempo of a track in beats per minute)

Using the song title and artist, we searched through the Genius API for the lyrics. Our final dataframe, which can be seen on our repo, has a total of 13508 rows and 13 columns. This process was done solely on Python.

### Exploratory Analysis
#### Numeric Features
We were interested in seeing whether there was a difference in the audio features between the genres.

![Alt text](https://github.com/grantnolasco/Spotify-Genre-ML/blob/master/EDA_Stuff/country_cloud.png?raw=true)

![Alt text](https://github.com/grantnolasco/Spotify-Genre-ML/blob/master/EDA_Stuff/rap_cloud.png?raw=true)

![Alt text](https://github.com/grantnolasco/Spotify-Genre-ML/blob/master/EDA_Stuff/metal_cloud.png?raw=true)

#### Lyrics 
LDA:
![Alt text](https://github.com/grantnolasco/Spotify-Genre-ML/blob/master/EDA_Stuff/LDA_Prelim.png?raw=true)

NMF:
![Alt text](https://github.com/grantnolasco/Spotify-Genre-ML/blob/master/EDA_Stuff/NMF_Prelim.png?raw=true)

EDA on numeric features and lyrics were done on R and Python respectively.

### Topic Modeling 
We are interested in examining the structure of the lyrics for all three genres. The two methods we wanted to test are LDA and NMF. But before we can start any topic modeling, we must performing data preprocessing on the text columns. Common text preprocessing methods we did includes:
  - Changing the text case: We made all the words lowercase to make sure the same word doesn’t appear as different words. 
  - Removing punctuation: Since programming languages includes both the letters and punctuation inside a token, we needed to remove any punctuation to make sure same words appear as the same token. Also, punctuations don’t offer any information for us.
  - Removal of stop words: scikit-learn has 318 stop words but the R package called tm has 488 words. Therefore, we plan on importing the all the stop words from tm package to Python and create a union set of stop words. By doing this, we will be removing a lot of noise that could create some problems for us during the modeling process as these words do not provide us any valuable information.
  - Frequent/rare words: First, we removed the top 10 words that appeared in our columns. The reason for this is because that these words must be general for it to appear so many times. Since we want very specific topics for our modeling, these words won’t be contributing anything valuable for our analysis. Regarding rare words, we’ve only deleted ten thousand of the most infrequent words that appeared in the dataset so far. 
  - Stemming: Once we finished removal of uninformative words, we used a process called stemming to change words back to their core meaning. For example, the word “playing” has the same meaning as “play” for the purposes of our analysis. Analyzing these words separately is pointless and only slows the process down, so we used stemming and lemmatization to reduce the complexity of the model. While stemming and lemmatization both reduces the word to its base form, lemmatization checks whether the base form is in the dictionary. For example, stemming would reduce the word “having” to “hav” while lemmatization would reduce it to “have”.  
  - Manually deleted words: Because many words don't appear in the list of stop words like "oh" or "ahh", we would have look over some of the rows or look at the word clouds to delete more words that don't have any context for us. This process is still happening.
  
Once we've completed text preprocessing, we can begin our topic modeling. For LDA, we used GridSearchCV to acquire the best parameters. Currently, we're still messing around with the parameters because we are still deleting many useless words, which might take some time. For NMF, it will be much harder to determine the best parameters because NMF function doesn't have a scoring output. So, we might just have to mess around with it until the topics look good. 

Here are examples of the current topics for LDA and NMF that we have so far:


#### Predictive Modeling
Our plan for predictive modeling is to test out numerous methods to determine which is the best. Currently, we're still working on predictions using only the audio features using the following methods: Gradient Boosting, Random Forest, Logistic Regression, and K-Nearest Neighbors. Once we've finished this step and the topic modeling, we want to know whether using the probability distributions for each "document" (lyrics of song) or TFIDF would work better as our features. Then, we plan on using the same algorithms to test the performance on just using song lyrics. Then, we can use an ensemble of both types of features for our test. 

### Possible Ideas 
This section includes possible ideas to work on once we've finished the main ideas for our project. This includes adding more songs to our database since the max number of pages we can search on Spotify API is 10,000. Also, we can increase the number of genres like pop or classical and test out other methods such as neural networks. 
