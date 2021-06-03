# Salty Tweets 
This is a "Salty Tweets" twitter   sentiment analysis. 

## How it works
- Gets trending topics and selects the top 10 topics with the most tweet volumes 
- get up to 100 tweets per topic according to twitter API 
- Performs Sentiment Analysis on each tweet to see the percentage of 'saltiness' as defined by a model trained on comments from Hacker News Website. Basically, twitter saltiness compared to Hacker News users. 
- Selects the Top 10 saltiest tweets and displays the tweets anda graph of the top 10 saltiest. Percentage are signed. Negative values are the saltiest. 
# Installation 
This package can be installed locally with pipenv virtual environment, uploaded to Heroku, AWS, or even shared hosting.
- Follow installation for heroku or AWS according to their instructions. 
- For shared Hosting FCGI. you need access to SSH Shell, be able to have Python on the server, and be able to install joblib, scikit-learn, category_encoders . 
# FCGI installation 
- Create a virtual Environment accordingly to your server instruction with venv follow this example
Create virtual environment on home directory with 

```$> source home/venv/bin/activate```

Clone Respository

cd into repository

```chmod +x index.fcgi```
```pip install joblib scikit-learn category_encoders```

Create a subdomain and point to the folder. 

This should get it running. 

# Known Issues 
- ON FCGI some servers may timeout do to memory usage during prediction. 
- FCGI version has the entire code in flat_cgi.py 
- Unable to succesfully use getenv() for twitter credentials on FCGI as well. 
# Links: 
Heroku Deployment: https://tweetsalty.herokuapp.com/

FCGI Deployment: http://saltytweets.lcsitmedia.com/

### TODO
- Update a requirements.txt file for easier FCGI installation 
- use getenv() for FCGI deployment for twitter credentials. 
