import json

thelist = ('tuscaloosanews', 'dothaneagle','arizonarepublic', 'TucsonStar', 'nwademgaz', 'TimesRecord', 'latimes', 'sfchronicle', 'denverpost', 'csgazette', 'hartfordcourant', 'nhregister','NewsWilmington', 'Doverpost', 'orlandosentinel', 'MiamiHerald', 'ajc', 'GwinnettDaily','MidWeekHawaii', 'StarAdvertiser','IdahoStatesman', 'twinfallstn','chicagotribune', 'Suntimes','indystar', 'nwi', 'DMRegister', 'gazettedotcom', 'kansasdotcom', 'CJOnline','courierjournal', 'heraldleader','theadvocatebr', 'shreveporttimes', 'sunjournal', 'PortlandPhoenix','baltimoresun', 'Baltimore_Times', 'BostonGlobe', 'bostonherald','freep', 'detroitnews', 'StarTribune', 'PioneerPress','clarionledger', 'DJournalnow','KCStar', 'stltoday', 'billingsgazette', 'GFTribune', 'OWHnews', 'JournalStarNews', 'reviewjournal', 'LasVegasSun', 'UnionLeader', 'laconiadailysun', 'starledger', 'TheRecordNJ', 'ABQJournal', 'thenewmexican', 'WSJ', 'nytimes', 'theobserver', 'newsobserver', 'theforum', 'bistrib', 'ThePlainDealer', 'Enquirer', 'TheOklahoman', 'tulsaworld', 'Oregonian', 'registerguard', 'PhillyDailyNews', 'PhillyInquirer', 'projo', 'TheValleyBreeze', 'GreenvilleNews', 'postandcourier', 'argusleader', 'RCJournal', 'Tennessean', 'newssentinel', 'dallasnews', 'HoustonChron', 'DeseretNews', 'sltrib', 'sevendaysvt', 'bfp_news', 'USATODAY', 'pilotnews', 'seattletimes', 'thenewstribune', 'GbrValleyWV', 'heralddispatch', 'journalsentinel', 'WiStateJournal', 'CSTribune', 'WTEnews')
with open("output22.csv","w") as out:
    for i in news:
        info = json.load(open(i+".json"))
        counter = 0
        for tweet in info['statuses']:
            text = tweet['text']
            if not text.startswith('RT'):
                print(text)
                counter += 1
        out.write("{} , {}\n".format(i,counter))
