

## Performing a simple text analysis

# !pip install textblob
# !pip install newspaper3k

## Libraries
from textblob import TextBlob
from newspaper import Article
import nltk as nltk

# nltk.download('punkt')

## URLs
url = 'https://en.wikipedia.org/wiki/Data_science'
# url = 'https://gadgets.ndtv.com/apps/features/whatsapp-pay-india-launch-payment-update-apk-feature-how-to-send-money-2321769'
# url = 'https://gadgets.ndtv.com/mobiles/news/oneplus-9-pro-launch-rumour-details-no-third-model-qualcomm-snapdragon-875-soc-2323937'

article = Article(url)

article.download()
article.parse()
article.nlp()

# text = article.text           # Taking the whole text
text = article.summary          # Taking only the summary from the text

print('-'*100)
print(text)

blob = TextBlob(text)
pol = blob.sentiment.polarity                 # -1(Neg) to +1(Pos)

print('\nPolarity:', pol)
print('-'*100)
