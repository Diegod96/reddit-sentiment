# Perform sentiment analysis

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd



def sentiment_analyser_score(df):
    analyser = SentimentIntensityAnalyzer()
    df_sentiment = pd.DataFrame(columns=["neg", "neu", "pos", "compound"])
    values = list(df.values.flatten())
    for row in values:
        score = analyser.polarity_scores(row)
        print(score)
        df_sentiment = df_sentiment.append(
            {"neg": score["neg"], "neu": score["neu"], "pos": score["pos"], "compound": score["compound"]},
            ignore_index=True)
    # df_sentiment.to_csv("sentiment_rAll_topDay.csv", sep=",", index=False)

    return df_sentiment


# if __name__ == '__main__':
#     df = read_data()
#     sentiment_analyser_score(df)

def score_data(df):
    """
    """
    _df = sentiment_analyser_score(df)
    return _df