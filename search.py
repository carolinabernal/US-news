# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '239975265-O503ejQ2tuo0xwzV61weVENgvgsgJeHKJzz1iykH'
ACCESS_SECRET = 'bOpsAgRscAkXpvGrQWmxuKUrE8W822FXuu6abxBM43i8i'
CONSUMER_KEY = 'GR2cYySpruyeRmgrQQNuEU8c0'
CONSUMER_SECRET = 'ThlRpJhdTkxmbTMIQFhr6iCOktmxRyBDM5koXiihkKIB4gs4JV'


oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth)

listA = ('tuscaloosanews', 'dothaneagle','arizonarepublic', 'TucsonStar', 'nwademgaz', 'TimesRecord', 'latimes', 'sfchronicle', 'denverpost', 'csgazette', 'hartfordcourant', 'nhregister')
for i in listA:
    j = twitter.search.tweets(q='Hillary OR Clinton from:'+i+' since:2016-11-22 until:2016-11-23 filter:links -@'+i+'', count='100')
    file_name=i+".json"
    with open(file_name,"w") as out:
        out.write(json.dumps(j, indent=4))

#Due to the restrictions of the Twitter Search API, we couldn't make a loop over
#all the users, so we had to create several lists and then run the code for each list

listB = ('NewsWilmington', 'Doverpost', 'orlandosentinel', 'MiamiHerald', 'ajc', 'GwinnettDaily','MidWeekHawaii', 'StarAdvertiser','IdahoStatesman', 'twinfallstn','chicagotribune', 'Suntimes')
listC = ('indystar', 'nwi', 'DMRegister', 'gazettedotcom', 'kansasdotcom', 'CJOnline','courierjournal', 'heraldleader','theadvocatebr', 'shreveporttimes', 'sunjournal', 'PortlandPhoenix')
listD = ('baltimoresun', 'Baltimore_Times', 'BostonGlobe', 'bostonherald','freep', 'detroitnews', 'StarTribune', 'PioneerPress','clarionledger', 'DJournalnow','KCStar', 'stltoday')
listE = ('billingsgazette', 'GFTribune', 'OWHnews', 'JournalStarNews', 'reviewjournal', 'LasVegasSun', 'UnionLeader', 'laconiadailysun', 'starledger', 'TheRecordNJ', 'ABQJournal', 'thenewmexican', 'theobserver', 'newsobserver')
listF = ('WSJ', 'nytimes', 'theforum', 'bistrib', 'ThePlainDealer', 'Enquirer', 'TheOklahoman', 'tulsaworld')
listG = ('Oregonian', 'registerguard', 'PhillyDailyNews', 'PhillyInquirer', 'projo', 'TheValleyBreeze', 'GreenvilleNews', 'postandcourier', 'argusleader', 'RCJournal', 'Tennessean', 'newssentinel', 'dallasnews', 'HoustonChron')
listH = ('DeseretNews', 'sltrib', 'sevendaysvt', 'bfp_news', 'USATODAY', 'pilotnews', 'seattletimes', 'thenewstribune', 'GbrValleyWV', 'heralddispatch', 'journalsentinel', 'WiStateJournal', 'CSTribune', 'WTEnews')
