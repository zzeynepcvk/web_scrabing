import pandas as pd

df = pd.read_csv('imdb.csv')

result =df.head(5)
#ilk 5 satırı getirir
result = df[['Title','Runtime'] ].head(5)
#5 ve 10 arası title ve imdbrating sütunlarını getirir
result = df[5:10][['Title','imdbRating'] ]
#imdb ratingi 7 den büyük olan filmleri getirir
result =df[df['imdbRating']>7.0][['Title','imdbRating'] ].head(20)
#yılı 2010 ile 2015 arasında olan filmleri getirir
result =df[(df['Year']>= 2010) & (df['Year']<=2015)][['Title','Year'] ].head(20)

print(result)
