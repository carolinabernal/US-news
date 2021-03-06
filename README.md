# US-news
Final project - Programming for Public Policy

Carolina Bernal - Manuel Esquivel - Miriam Gonzalez

# Our Question

Have you ever thought about how much your perception of a particular topic could change when you’re
exposed to more or less information on that topic?

Our hypothesis is that differences in news coverage could explain some of the variation in how states behave regarding different topics.

Based on tweets from the last days, our app displays maps of the U.S. showing the coverage of different topics by the main newspapers per state.     

##The Data Source

For this project we used two main pieces of information:

1. Identifying major local newspapers per state:
Information about the top local newspapers in the U.S. can be found on the following websites:

https://www.mediamiser.com/resources/top-media-outlets/top-10-arizona-daily-newspapers-by-circulation/
http://www.cision.com/us/2010/05/top-10-daily-massachusetts-newspapers/

  We chose two newspapers for each state in the United States--except Alaska, Hawaii and District of Columbia.
  Then we searched for the twitter handles of the accounts of those newspapers. 

  The complete list of the newspapers that we analyzed in this project, their twitter handles, and corresponding States can be found on the file called "Twitter_accounts.csv".
 
2. Obtaining Tweets of local newspapers:
We used the [Twitter Search API](https://dev.twitter.com/rest/public/search) to get the tweets about specific topics on the days of interest. This API is part of Twitter’s REST API, which allows us to read and write Twitter data in JSON format. We decided to use the Twitter Search API instead of the Streaming API because we wanted to conduct specific historic searches, instead of keeping a persistent HTTP connection open to pull tweets as they are published.

### Obtaining the data from Twitter

1. To access the Twitter API you need to obtain your Twitter API keys (API key, API secret, Access token, Access token secret). We did that following these steps:
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
    
3. We generated a code in python to extract the data from Twitter. The code is in the repository under the name "search.py".
In general, our code contains the following elements:
  * Since the response from the Twitter Search API is in JSON format we imported json.
  * To initiate connection to Twitter Search API we included the credentials that we obtained by creating our Twitter App (API key, API secret, Access token, Access token secret).

  NOTE: Given the privacy agreement that we accepted when we created our Twitter Apps, we can't share our credentials. For this reason, the code that is in the repository DOES NOT contain them and will not run unless you introduce your own keys (OAuth settings).

  * To conduct queries in the Twitter Search API you must consider the following elements:
  
    - "q"            -   defines the query
    - "from"         -   allows you to get the tweets from a specific user/twitter accounts
    - "since/until"  -   allow you define the window for which you are conducting the search
    - "filter"       -   allows you to restrict the tweets that you get, based on a specific criteria (e.g. tweets linking to                          URL) 
    - "OR"           -   allows you to find tweets containing either “the first term” or “second term” (or both)
    - "-"            -   allows you to exclude tweets that contain specific terms

    Given the information above, the following is an example of the format:
    q='Hillary OR Clinton from:'+i+' since:2016-11-22 until:2016-11-23 filter:links -@'+i+'', count='100'
    
      - We searched the queries for the following words: Trump, Hillary OR Clinton, marihuana OR marijuana OR cannabis, and Cuba OR Cubans OR Fidel OR Castro
      - We filtered the tweets containing a link to an article to make sure that we were only counting information that was actually published by the newspapers, and not counting information that only went out thruough the newspaper's twitter account or information that was re-tweeted by/from the newspaper. The reason for this is that we are more interested in how information varies across newspapers from different states, than in information flows originated and subscribed to the Twitter environment. 
      - We obtained those queries from November 22 to 27.
      - We learned that the most convenient way to loop a list of accounts is using '+i+' instead of just 'i'. Tweet Tweet! (or pio pio in
        Spanish)

4. We downloaded the responses in JSON format and then generated a code to count the number of tweets per newspaper (we excluded retweets) and write the output on a csv file. This code can be found in the repository under the name of "counter.py". All the json files with tweets per topic, per date and per newspaper are in the file "Json - zips" of this repository.   


#### Some challenges with the data
The Twitter Search API has several restrictions on the information that you can obtain. The following were some of the challenges that we faced while we were extracting the information:

1. The Search API has API Rate Limits per user access token. As we created two apps in Twitter for this project, we could easier deal with some of the restrictions. In particular, this allowed us to retrive the double of the amount of information than a regular single user would have accessed. 

2. Restrictions are enforced in windows of 15 minutes. It means that every 15 minutes you can start a new search that meets the other restrictions. 

3. Within each limit window, Twitter Search API allows for 15 requests/calls. Thus, we had to split the twitter accounts that we were analyzing in different lists to conduct the searches by intervals. (An alternative to these lists created by us, would had been redefining the queries in such a way that they were restricted to retrive information from certain users included in a Twitter list. We dismissed this alternative because it required more work by hand and less coding). 

4. The Search API searches against a sampling of recent Tweets published in the past 7 days. For that reason we created a DataFrame using information only for the week of November 22 to 27.

Those restrictions on the amount of information that can be retrieved at once led us to:

  * Focus FOR NOW only on the tweets from the two (2) major newspapers of each state (when we have initially planned to use 5 newspapers per state).
  * Not weighting the number of tweets by the size of the newspaper, or by how active the newspaper is on twitter (to do this we would need the total number of tweets per newspaper).
  
##Creating our DataFrames
Our code to count the number of tweets per newspaper writes the output in csv files. We use this information to generate a new csv file per topic with the number of tweets per state and per day, as well as the sum of the tweets over the past week. Thus, we generated four DataFrames: "Trump_tweets.csv", "Hillary_tweets.csv", "Marihuana_tweets.csv" and "Cuba_tweets.csv".

Using Geopandas we merged each of the csv files mentioned above with the shapefile of U.S. states. We then plotted the merged dataset to show how the number of tweets about each of the topics varies across U.S. states.

We also added a base to our maps showing the cities of the states where the Republican party won in the past presidential election. We added this base because we initially expected Republican states to be less informed. Although that correlation ended up not being so clear in the plotted maps (maybe because we collected tweets after the elections) we decided to keep that base on our maps because we thought it could be cool having that information to identify variations in coverage correlated with Republican states. 

To do this we used the csv file "Locations.csv", which contains the latituted and longitude of the State Capitals in the United States. We obtained the information from http://www.arcgis.com/home/item.html?id=90977e1946e74416b6f7e304efed7bc7 and then we added a column with the results of the 2016 presidential elections. In order to merge the map of cities with the maps of states and media coverage, we needed to convert latitudes and longitudes in geometries. 

##Using Django
Once all the maps were generated, we used Django to display the results on a website. 

Our site is contained within the folder called 'news' in our repository. Once you access the 'news' folder, you will find the 'mysite' and 'myapp' folders. 

Within the 'myapp' folder you will find the relevant files and folder that we generated to create our site: 
  * url.py file
  * views.py file
  * templates folder with all the required .html files
    
Once you run the server (python manage.py runserver), you can access the site's homepage through http://localhost:8000/myapp/newshome/. For the style and design of this template, we used the open source "Black and White Photo Template" from w3schools (http://www.w3schools.com/w3css/w3css_templates.asp). However, we did have to make plenty of modifications to the template. 

On the homepage you will see a beautiful description of our project and instructions on how to navigate the rest of the website.
The first thing you need to do is click on one of the topics contained on the navigation bar. As an example, if you pick "Hillary", you will be transported to another page that we called "Hillarytab" under views. So you will now be in http://localhost:8000/myapp/newshome/Hillarytab. 

In this page you can: 
  * select the day for which you would like to see the maps with the results
  * see a map with the results of ALL the individual maps available for that particular topics
For content and formatting, this page uses the "Hillarytab.html" script under the "templates" folder, which contains the content of the page. This same process is followed when you access all the other topics. 

The scripts "Hillarytab.html", "Trumptab.html", "Cubatab.html", and "marihuanatab.html" all use the "yearstemp.html" template, which is a template that containes all the formatting for how we want those pages to look like.

Once you click on a particular day within a particular topic, you will be transported to http://localhost:8000/myapp/newshome/Hillarytab/"DAY OF INTEREST". This url in turn directs you to a view called "picget." This view uses the last portion of the url (i.e., the date of interest) and inserts it into an address to complete the direction of where the map of interest lives. In this case, all maps of interest live in our repository. The map of interest is then opened on a new tab. 

We hope you enjoy! Let us know if you would like to buy our code or pay a small consulting fee for us to run any other topics of interest.
