# Download data from this link "https://grouplens.org/datasets/movielens/"

import pandas as pd
unames = ['user_id', 'age', 'gender', 'occupation']
users = pd.read_table("ml-1m/users.dat", sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table("ml-1m/ratings.dat", sep="::", header=None, names=rnames)

mnames = ['movie_id', 'title', 'genre']
movies = pd.read_table("ml-1m/movies.dat", sep="::", header=None, names=mnames)

data = pd.merge(pd.merge(ratings, users), movies)
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title > 250]
mean_ratings = mean_ratings.ix[active_titles]
top_female_titles = mean_ratings.sort_values(by='F', ascending=False)

# Measuring rating difference
mean_ratings['diff'] = mean_ratings['F'] - mean_ratings['M']
sorted_by_diff = mean_ratings.sort_values(by='diff', ascending=False)
# To reverse order of rows on sorted dataframe
sorted_by_diff[::-1][:5]
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.ix[active_titles]

