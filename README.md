# US-news
Final project - Programming for Public Policy

# Our Question

Have you ever thought how much your perception of a particular topic could change when you’re
exposed to more or less information on that topic?

Our hypothesis is that differences in news’ coverage could explain some of the variation in how states behave regarding different topics.

Based on tweets from the lasts days, this app shows in maps difference in coverage of different topic among the main newspapers per state.


##The Data Source

For this project we use two main pieces of information:

1. Identify major local newspapers per state
You can get information about local newspapers in the U.S. in the following websites:

https://www.mediamiser.com/resources/top-media-outlets/top-10-arizona-daily-newspapers-by-circulation/
http://www.cision.com/us/2010/05/top-10-daily-massachusetts-newspapers/

  We choose two newspapers for each state in the United States--except Alaska, Hawaii and District of Columbia.
  Then we search for the twitter accounts of those newspapers in their websites.

  The complete list of the newspapers that we analyze in this project and their twitter accounts can be found on the file called "Twitter_accounts.csv".

2.Tweets of local newspapers
We used the [Twitter Search API](https://dev.twitter.com/rest/public/search) to get the tweets about specific topics on the days that we selected. This API is part of Twitter’s REST API, which allow us to read and write Twitter data in JSON format.

NOTE: We decided to use the Twitter Search API instead of the Streaming API in order to be able to conduct specific searches.

### Obtaining the data from Twitter

1. To access the Twitter API you need to obtain your Twitter API keys (API key, API secret, Access token, Access token secret). We did this following these steps:
    * Go to the [Twitter Development Site](https://dev.twitter.com/) and log in to your Twitter user account.
    * From the navigation bar choose <Myapps> then click on "Create New App"
    * Fill in your application details (name, description and website) and click "Create your Twitter application"
    * Click on the "Keys and Access Tokens" tab and click "Create my token"
    * Make a note of your OAuth settings (keys) --you will need to copy them to download information.

2. To connect to Twitter API and download the tweets you need to install a Twitter Library called [Python Twitter Tools](https://pypi.python.org/pypi/twitter)
  Once you downloaded the Python Twitter Tools package, type the following commands in your terminal:
    $ python setup.py --help
    $ python setup.py build     
    $ python setup.py install

3. We generated a code in python to extract the data from Twitter. The code is in the repository under the name "search_api.py".
In general, our code contains the following elements:
  * Since the response from the Twitter Search API is in JSON format we imported json.
  * To initiate connection to Twitter Search API we included the credentials that we obtained by creating our Twitter App (API key, API secret, Access token, Access token secret).

  NOTE: Given the privacy agreement that we accepted when we created our Twitter App, we can't share our credentials. For this reason, the code that is in the repository DOES NOT contain them and will not run unless you introduce your own keys (OAuth settings).

  * To conduct queries in the Twitter Search API you must consider the following elements:
    q            -   defines the query
    from         -   allows you to get the tweets from a specific user/twitter accounts
    since/until  -   allow you define the window for which you are conducting the search
    filter       -   allows you to restrict the tweets that you get, based on a specific criteria

    Given the information above, our queries had the following format:
    q='Hillary OR Clinton from:'+i+' since:2016-11-22 until:2016-11-23 filter:links -@'+i+'', count='100'

    In our case, we are filtering the tweets that contain a link to an article of each newspaper.

4. We downloaded the responses in JSON format and then generated a code to count the number of tweets (we excluded retweets) per newspaper and write it on a csv file. This code can be found in the repository under the name of "counter.py"


#### Some challenges with the data
The Twitter Search API has several restrictions on the information that you can obtain. The following were some of the challenges that we faced while we were extracting the information:

1. The Search API uses a sampling of Tweets published in the past 7 days, thus, we created a DataFrame using information only for the week of November 22 to 27.

2. It allows for 15 requests per rate limit window, then it allows 15 requests per window per access token, and rate limits are divided into 15 minute intervals. Thus, we split the twitter accounts that we are analyzing in different lists to conduct the searches by intervals.

Those restrictions on the amount of information that can be retrieved at once led us to:

  * Focus FOR NOW only on the tweets from the two (2) major newspapers of each state.
  * Not weighting the number of tweets by the size of the newspaper or by how active is the newspaper on twitter (to do this we would need the total number of tweets per newspaper).

##Using Django

