import csv
import re
import sqlite3
import pandas as pd
from collections import defaultdict
import numpy as np
# Use svg backend for better quality
import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
# AUTOLAB_IGNORE_START
plt.style.use('ggplot')
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0) # you should adjust this to fit your screen
# AUTOLAB_IGNORE_STOP

"""
Q1. Task A: Load Twitter data into SQLite database
Your first task is to use the csv and sqlite3 python packages to load the three csv files we give you as relations (or tables) into an SQLite in-memory database.
Loading the data from csv file into the database involves the following steps:
1. Identify the schema of the table (the csv files should contain this information)
2. Create a table with the identified schema
3. Load the contents of csv in memory
4. Insert every row of csv file as a record in the table
You can refer to sqlite3 documentation and the class lecture for steps 2 and 4. For step 3, refer to the csv documentation.
Make sure to commit (the equivalent of Ctrl+S for databases) any changes you make to the database. This page should give you an idea about why commit is essential.
"""

def load_twitter_data_sqlite3(conn, users_filepath, edges_filepath, tweets_filepath) :
    """ Load twitter data in the three files as tables into an in-memory SQLite database
    Input:
        conn (sqlite3.Connection) : Connection object corresponding to the database; used to perform SQL commands.
        users_filepath (str) : absolute/relative path to users.csv file
        edges_filepath (str) : absolute/relative path to edges.csv file
        tweets_filepath (str) : absolute/relative path to tweets.csv file
    Output:
        None
    """
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE table users
    (name text, screen_name text, location text, created_at text, friends_count integer,
    followers_count integer, statuses_count integer, favourites_count integer);

    CREATE table edges
    (screen_name text, friend text);

    CREATE table tweets
    (screen_name text, created_at text, retweet_count integer, favorite_count integer, text text);
    """)
    load_data_to_db(cursor, edges_filepath, "edges")

    t_name = 'tweets'
    with open(tweets_filepath, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        reader.next()
        for row in reader:
            cursor.execute('INSERT INTO {0} VALUES (?, ?, ?, ?, ?);'.format(t_name,), (row[0], row[1], int(row[2]), int(row[3]), row[4]))
        conn.commit()

    t_name = 'users'
    with open(users_filepath, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        reader.next()
        for row in reader:
            cursor.execute("INSERT INTO {0} VALUES ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8});".format(t_name, add_quotes(row[0]), add_quotes(row[1]), add_quotes(row[2]), add_quotes(row[3]), row[4], row[5], row[6], row[7]))
        conn.commit()

def add_quotes(s):
    return '"' + s + '"'

def load_data_to_db(cursor, f_path, t_name):
    with open(f_path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        reader.next()
        for row in reader:
            row_new = ["'" + e + "'" if re.search(r'[a-zA-Z]', e) else e for e in row]
            values = ','.join(row_new)
            cursor.execute("INSERT INTO {0} VALUES ({1});".format(t_name, values))
        conn.commit()

# AUTOLAB_IGNORE_START
# connect to an in memory database
conn = sqlite3.connect(":memory:")
conn.text_factory = str
# call to your function
load_twitter_data_sqlite3(conn, 'twitter/users.csv', 'twitter/edges.csv', 'twitter/tweets.csv')
# make sure to change the path to csv files appropriately
cursor = conn.cursor()
# prints all tables in the database
for row in cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';"):
    print row
# AUTOLAB_IGNORE_STOP

"""
Q1. Task B: Trending tweets in a topic
Twitter is regarded as an invaluable source of valuable information. Hence, one of the favorite tasks of data miners is the analyse the trending tweets in a given topic.
This task requires you to retrieve the top N most trending tweets (in descending order of retweet count) about a given topic (which is a list of keywords). The following information may be useful:
1. A tweet is said to be about a given topic if it contains any of the given topical phrases/keywords.
2. We will use the following simple trending_score: retweet_count + favorite_count. Tweets with higher trending_score must be ranked before the ones with lower trending_score.
3. Your result must contain unique tweets. If a tweet text occurs multiple times, display it only once with its highest trending_score.
4. Break ties by sorting the tweets in alphabetical order.
"""

def trending_tweets(cursor, topical_phrases=['Hillary', 'Clinton'], N=5):
    """ Retrieves the top N trending tweets containing one or more of the given topical phrases.
    Input:
        cursor (sqlite3.Cursor): Cursor object to query the database.
        topical_phrases (list of strings): A list of keywords identifying a topic.
        N: Number of trending tweets to retrieve
    Output:
        results (sqlite3.Cursor): Cursor object which can be used to iterate over the retrieved records/tuples.
    """
    template = "text Like '%{0}%'"
    phrases = " OR ".join([template.format(w) for w in topical_phrases])
    query = "SELECT tweet, MAX(trending_score) FROM (SELECT text AS 'tweet', (retweet_count + favorite_count) AS 'trending_score' FROM tweets WHERE {0}) GROUP BY tweet ORDER BY tweet LIMIT {1};".format(phrases, N) # your query here
    results = cursor.execute(query)
    return results

results = trending_tweets(conn.cursor())
for row in results:
    print row

"""
Q1. Task C: Tweet recommendation
How does Twitter go about populating the feed for a user? While Twitter may use a comple models to do this, in this task, we will use a Simple Tweet Recommender (STR), which recommends a user's tweets to all users who follow him/her.
In this task, you will write a query to determine the number of tweets recommended to each user.
"""

def num_tweets_in_feed(cursor):
    """ Retrieves the number of tweets STR recommends to each Twitter user.
    Input:
        cursor (sqlite3.Cursor): Cursor object to query the database.
    Output:
        results (sqlite3.Cursor): Cursor object which can be used to iterate over the retrieved records/tuples.
    """
    query = """SELECT t3.screen_name, IFNULL(t4.num_tweets, 0) FROM
                users t3
                LEFT JOIN
                (SELECT friend, SUM(count) AS 'num_tweets' FROM
                edges t1
                INNER JOIN
                (SELECT screen_name, COUNT(text) AS 'count' FROM tweets GROUP BY screen_name) t2
                ON t1.screen_name = t2.screen_name
                GROUP BY t1.friend) t4
                ON t3.screen_name = t4.friend
    """ # your query here
    return cursor.execute(query)

# AUTOLAB_IGNORE_START
results = num_tweets_in_feed(conn.cursor())
for row in results:
    print row
# AUTOLAB_IGNORE_STOP
#
"""
Q2. Task A: Load Twitter data using pandas
Fill in the following method stub and return the data frames for users, edges and tweets.
"""
def load_twitter_data_pandas(users_filepath, edges_filepath, tweets_filepath):
    """ Loads the Twitter data from the csv files into Pandas dataframes
    Input:
        users_filepath (str) : absolute/relative path to users.csv file
        edges_filepath (str) : absolute/relative path to edges.csv file
        tweets_filepath (str) : absolute/relative path to tweets.csv file
    Output:
        (pd.DataFrame, pd.DataFrame, pd.DataFrame) : A tuple of three dataframes, the first one for users,
                                                    the second for edges and the third for tweets.
    """
    users = pd.read_csv(users_filepath, parse_dates=True)
    edges = pd.read_csv(edges_filepath)
    tweets = pd.read_csv(tweets_filepath, parse_dates=True)
    return (users, edges, tweets)

# AUTOLAB_IGNORE_START
(users_df, edges_df, tweets_df) = load_twitter_data_pandas('twitter/users.csv', 'twitter/edges.csv', 'twitter/tweets.csv')
# make sure to change the path to csv files appropriately
print users_df.head()
print edges_df.head()
print tweets_df.head()
# AUTOLAB_IGNORE_STOP

"""
Q2. Task B: Correlation
Statisticians and data analysts usually like to study about correlation between different observed variables. This helps uncover interesting patterns in the data such as causal relationships (e.g., snow on the road leads to increase in number of accidents). Correlation studies are important for multiple reasons:
While correlation does not imply causation, a lack of correlation implies a lack of causation. This can be used to rule out many causal relationships.
Correlation helps with prediction. The more closely related two variables are, the easier it is to predict one from the other.
In this task, we ask you to plot the friends_count (on y-axis) vs the followers_count (on x-axis) using the matplotlib package.
"""

def plot_friends_vs_followers(users_df):
    """ Plots the friends_count (on y-axis) against the followers_count (on x-axis).
    Input:
        users_df (pd.DataFrame) : Dataframe containing Twitter user attributes,
                                    as returned by load_twitter_data_pandas()
    Output:
        (matplotlib.collections.PathCollection) : The object returned by the scatter plot function
    """
    x, y = users_df.loc[:, "followers_count"], users_df.loc[:, "friends_count"]
    N = len(x)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2
    plt.scatter(x, y, c=colors, alpha=0.2, s=area)
    plt.show()

# AUTOLAB_IGNORE_START
plot_friends_vs_followers(users_df)
# AUTOLAB_IGNORE_STOP

"""
Do you see a correlation between these two variables from your scatter plot? Let's measure this quantitatively using the Pearson's correlation coefficient.
For a set of observations (X,Y)=[(x1,y1),(x2,y2),...,(xn,yn)], the Pearson's correlation coefficient is a measure of the linear dependence between two variables X and Y, giving a value between +1 and −1 inclusive, where 1 is total positive correlation, 0 is no correlation, and −1 is total negative correlation.
r=rxy=n∑xiyi−∑xi∑yin∑x2i−(∑xi)2√ n∑y2i−(∑yi)2√
Now, fill in the following function to compute the Pearson's correlation coefficient between friends_count and followers_count.
"""

def correlation_coefficient(users_df):
    """ Plots the friends_count (on y-axis) against the followers_count (on x-axis).
    Input:
        users_df (pd.DataFrame) : Dataframe containing Twitter user attributes,
                                    as returned by load_twitter_data_pandas()
    Output:
        (double) : correlation coefficient between friends_count and followers_count
    """
     X, Y = users_df.loc[:, "followers_count"], users_df.loc[:, "friends_count"]
    N = len(X)
    upper = sum(np.multiply(X, Y)) - N * np.mean(X) * np.mean(Y)
    bottom = np.sqrt(sum(np.square(X)) - N * np.mean(X)**2) * np.sqrt(sum(np.square(Y)) - N * np.mean(Y)**2)
    return round(upper / bottom, 3)
# round(np.corrcoef(X, Y)[0, 1], 3)

# AUTOLAB_IGNORE_START
print correlation_coefficient(users_df)
# AUTOLAB_IGNORE_STOP

"""
Q2. Task C: Degree distribution
If you are not familiar with graph theory and/or graph mining, skip the first paragraph.
As you're familiar with graphs, you might know that the degree of a node is the number of connections it has to other nodes. A common statistic to look out for in the case of real world graphs is the degree distribution. Literature says degrees of nodes in real world graphs follow a power law distribution. The implication is that a scatter plot of num_users versus k (as we will define below) yields an almost straight line. In this task, we shall verify whether the given crawl of Twitter network satisfies this property.
Let us call the number of friends a Twitter user has as his/her degree. The degree distribution is a histogram of the number of friends. Your task is to visualize this histogram.
"""

def degree_distribution(edges_df):
    """ Plots the distribution of .
    Input:
        users_df (pd.DataFrame) : Dataframe containing Twitter user attributes,
                        as returned by load_twitter_data_pandas()
    Output:
        (array, array, list of Patch objects) : Tuple of the values of the histogram bins,
                        the edges of the bins and the silent list of individual patches used to create the histogram.
    """
    screen_name = edges_df.loc[:, 'screen_name']
    d = defaultdict(int)
    for name in screen_name:
        d[name] += 1
    df = pd.DataFrame([[name, count] for name, count in d.items()], columns=["user_name", "degree"])
    print df.loc[:,'degree'].head()
    plt.hist(df.loc[:,'degree'], bins=df.loc[:,'degree'].max())
    plt.show()

# AUTOLAB_IGNORE_START
degree_distribution(edges_df)
# AUTOLAB_IGNORE_STOP