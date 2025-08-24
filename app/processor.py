import pandas
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


class Text_proceessor():

    def __init__(self,data):
        self.data = data

    def to_df(self):
        self.df = pandas.DataFrame.from_dict(self.data)

    def get_df(self):
        return self.df
    
    def to_json(self):
        self.json = self.df.to_json(orient="records",default_handler=str)

    def get_json(self):
        return self.json
        



    def get_comp_level(self,comp)->str:
        if 0.5<= comp <=1:
            return "positive"
        if -0.5 < comp < 0.5:
            return "neutral"
        if -0.5 >= comp >-1:
            return "negative"
        
    def get_compound(self,tweet):
        score = SentimentIntensityAnalyzer().polarity_scores(tweet['Text'])
        return self.get_comp_level(score['compound'])
    
    def classification(self):
        self.df["sentiment"] = self.df.apply(self.get_compound,axis=1)
        




    def get_text_from_file(self,addres):
        with open(addres,'r') as f:
            tlist =(f.read().split('\n'))
            # print(tlist)
        return tlist
    
    def get_weapon_from_tweet(self,tweet):
        weapons = self.get_text_from_file(BASE_DIR / "data" / "weapons.txt")
        for word in tweet['Text'].split(' '):
            if word in weapons:
                return word
        return ""

    def weapons_detected(self):
        self.df["weapons_detected"] = self.df.apply(self.get_weapon_from_tweet,axis=1)


        

    def get_num_word_in_text(self,word,text)->int:
        return sum([i == word for i in text])


    def get_word_rarest_from_tweet(self,tweet)->str:
        text = tweet['Text'].split(' ')
        min_word = ''
        min_num  = 0
        for word in text:
            num = self.get_num_word_in_text(word,text)
            if num == 1:
                return word
            if num < min_num or min_num == 0:
                min_num = num
                min_word = word
        return min_word


    def word_rarest(self):
        self.df['word_rarest'] = self.df.apply(self.get_word_rarest_from_tweet,axis=1)



    def process_data(self):
        self.word_rarest()
        self.classification()
        self.weapons_detected()

