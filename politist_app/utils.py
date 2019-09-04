import requests
import re
from requests_oauthlib import OAuth1
import json
from watson_developer_cloud import ToneAnalyzerV3


#URLS
tweets_url = 'https://api.twitter.com/1.1/search/tweets.json?q={}&result_type=pupular&result_type=mixed&until=2019-02-03&count=10&tweet_mode=extended'
tweets_url_popular = 'https://api.twitter.com/1.1/search/tweets.json?q={}&result_type=popular&until=2019-02-03&tweet_mode=extended'

#Twitter api keys
API_KEY='<insert api key here>'
API_SECRET='<insert api secret here>'
ACCESS_TOKEN='<insert access token here>'
ACCESS_TOKEN_SECRET='<insert access token secret here>'

def get_tweets(query):
    tweets = []
    pattern = r" "
    query = re.sub(pattern, "%20", query)
    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = requests.get(tweets_url.format(query),auth=auth)
    json_response = response.json()
    for tweet in json_response["statuses"]:
        tweets.append(tweet["full_text"])
    return list(set(tweets))

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey = "<insert api key here>",
    url= "https://gateway-lon.watsonplatform.net/tone-analyzer/api"
)

def get_related_tweets(query):
    pattern = r" "
    query = re.sub(pattern, "%20", query)
    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = requests.get(tweets_url_popular.format(query),auth=auth)
    json_response = response.json()
    return json_response

def sentiment_analyser(tweet_list):
    emotion_dict={"anger":{"score":0,"count":0},"fear":{"score":0,"count":0},"joy":{"score":0,"count":0},"sadness":{"score":0,"count":0},"confident":{"score":0,"count":0},"tentative":{"score":0,"count":0},"analytical":{"score":0,"count":0},}
    counter =0
    for i in range(0,len(tweet_list)):
        tone_analysis = tone_analyzer.tone(
            {'text': tweet_list[i]},
            'application/json'
        ).get_result()
        tones = tone_analysis["document_tone"]["tones"]
        for tone in tones:
            if tone["tone_id"] == "anger":
                emotion_dict["anger"]["score"] = emotion_dict["anger"]["score"] + tone["score"]
                emotion_dict["anger"]["count"] += 1
                counter=counter+1
            if tone["tone_id"] == "fear":
                emotion_dict["fear"]["score"] = emotion_dict["fear"]["score"] + tone["score"]
                emotion_dict["fear"]["count"] += 1
                counter=counter+1
            if tone["tone_id"] == "joy":
                emotion_dict["joy"]["score"] = emotion_dict["joy"]["score"] + tone["score"]
                emotion_dict["joy"]["count"] += 1
                counter=counter+1
            if tone["tone_id"] == "sadness":
                emotion_dict["sadness"]["score"] = emotion_dict["sadness"]["score"] + tone["score"]
                emotion_dict["sadness"]["count"] += 1
                counter=counter+1
            if tone["tone_id"] == "confident":
                emotion_dict["confident"]["score"] = emotion_dict["confident"]["score"] + tone["score"]
                emotion_dict["confident"]["count"] += 1
                counter=counter+1
            if tone["tone_id"] == "tentetive":
                emotion_dict["tentative"]["score"] = emotion_dict["tentative"]["score"] + tone["score"]
                emotion_dict["tentative"]["count"] += 1
                counter=counter+1
            if tone["tone_id"] == "analytical":
                emotion_dict["analytical"]["score"] = emotion_dict["analytical"]["score"] + tone["score"]
                emotion_dict["analytical"]["count"] += 1
                counter=counter+1


    anger = emotion_dict["anger"]["score"]
    fear = emotion_dict["fear"]["score"]
    joy = emotion_dict["joy"]["score"]
    confident = emotion_dict["confident"]["score"]
    tentative = emotion_dict["tentative"]["score"]
    sadness = emotion_dict["sadness"]["score"]
    analytical = emotion_dict["analytical"]["score"]

    emotion_list = [anger,joy,fear,sadness,analytical,tentative,confident]
    k = max(emotion_list)
    prob = k*100/counter
    reaction=''
    for emotion in emotion_dict.keys():
        if k == emotion_dict[emotion]["score"]:
            if emotion == "anger" or emotion == "fear" or emotion == "sadness" :
                reaction = "Negative"
            elif emotion == "confident" or emotion == "joy" :
                reaction = "Positive"
            elif emotion == "tentative" or emotion == "analytical" :
                reaction = "Neutral"


            return emotion,prob,emotion_dict,reaction

def get_related_tweets(query):
    pattern = r" "
    query = re.sub(pattern, "%20", query)
    auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    response = requests.get(tweets_url_popular.format(query),auth=auth)
    json_response = response.json()
    return json_response

def toi():
    r = requests.get("https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxx")

    z = r.json()
    return z