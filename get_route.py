import urllib2
from HTMLParser import HTMLParser
from time import strftime



mb_api = 'http://us.megabus.com/JourneyResults.aspx?originCode={0}&destinationCode={1}&outboundDepartureDate={2}%2f{3}%2f{4}&inboundDepartureDate=&passengerCount=1&transportType=0&concessionCount=0&nusCount=0&outboundWheelchairSeated=0&outboundOtherDisabilityCount=0&inboundWheelchairSeated=0&inboundOtherDisabilityCount=0&outboundPcaCount=0&inboundPcaCount=0&promotionCode=&withReturn=0'

Buses = {'Des Moines, IA': '106', 'Milwaukee, WI': '121', 'Frederick, MD': '109', 'Minnesota': '23', 'Illinois': '13', 'Chattanooga, TN': '290', 'Indiana': '14', 'Louisiana': '18', 'Texas': '43', 'Giddings, TX': '401', 'Galveston, TX': '325', 'Dallas/Fort Worth, TX': '317', 'Knoxville, TN': '118', 'New Brunswick, NJ': '305', 'Connecticut': '7', 'Rochester, NY': '134', 'Atlanta, GA': '289', 'West Virginia': '48', 'Texarkana, AR': '407', 'La Grange, TX': '333', 'Ridgewood, NJ': '133', 'Kansas City, MO': '117', 'El Paso, TX': '397', 'Harrisburg, PA': '111', 'Big Spring, TX': '393', 'East Lansing, MI': '330', 'Toronto, ON': '145', 'Missouri': '25', 'South Bend, IN': '368', 'Fairhaven, MA': '316', 'Kenton, OH': '362', 'Carthage, TX': '395', 'New Jersey': '30', 'Valparaiso, IN': '376', 'Gainesville, FL': '296', 'Iowa City, IA': '116', 'Lufkin, TX': '404', 'Houston, TX': '318', 'San Antonio, TX': '321', 'Eagle Pass, TX': '327', 'Shreveport, LA': '332', 'Maryland': '20', 'Oklahoma City, OK': '323', 'Wisconsin': '49', 'Syracuse, NY': '139', 'Michigan': '22', 'Del Rio, TX': '328', 'New York': '32', 'Massachusetts': '21', 'Mobile, AL': '294', 'Richmond, IN': '371', 'Boston, MA': '94', 'Florida': '10', 'Rhode Island': '39', 'Sparks, NV': '419', 'Nashville , TN': '291', 'Memphis, TN': '120', 'Livingston, TX': '402', 'Ohio': '35', 'State College, PA': '137', 'Burlington, VT': '96', 'North Carolina': '33', 'Athens, GA': '302', 'District of Columbia': '9', 'Birmingham, AL': '292', 'Van Wert, OH': '364', 'Elkhart, IN': '367', 'Maine': '19', 'Christiansburg, VA': '101', 'Ontario': '51', 'Detroit, MI': '107', 'Norman, OK': '322', 'Oklahoma': '36', 'Delaware': '8', 'Champaign, IL': '98', 'Madison, U of Wisc, WI': '300', 'La Marque, TX': '337', 'Arkansas': '4', 'Humble, TX': '334', 'New Haven, CT': '122', 'Secaucus, NJ': '135', 'Indianapolis, IN': '115', 'Newark, DE': '389', 'Lima, OH': '363', 'Sacramento, CA': '415', 'Durham, NC': '131', 'Midland, TX': '405', 'Pittsburgh, PA': '128', 'Washington, DC': '142', 'California': '5', 'Uvalde, TX': '326', 'Providence, RI': '130', 'Georgia': '11', 'Columbia City, IN': '373', 'San Jose, CA': '412', 'Pennsylvania': '38', 'San Francisco, CA': '414', 'Toledo, OH': '140', 'Montgomery, AL': '293', 'Hampton, VA': '110', 'Philadelphia, PA': '127', 'Nacogdoches, TX': '406', 'Riverside, CA': '416', 'Louisville, KY': '298', 'Buffalo Airport, NY': '273', 'Little Rock, AR': '324', 'Ft. Wayne, IN': '365', 'Columbus, OH': '105', 'Dayton-Trotwood, OH': '370', 'Hartford, CT': '112', 'Cincinnati, OH': '102', 'Storrs, CT': '138', 'Buffalo, NY': '95', 'Brenham, TX': '335', 'Nevada': '28', 'Ann Arbor, MI': '91', 'Omaha, NE': '126', 'Cleveland, OH': '103', 'Charlotte, NC': '99', 'Madison, WI': '119', 'Princeton, NJ': '304', 'St Louis, MO': '136', 'Springfield, MO': '411', 'New York, NY': '123', 'Lubbock, TX': '403', 'San Angelo, TX': '329', 'Richmond, VA': '132', 'Baltimore, MD': '143', 'Albany, NY': '89', 'Minneapolis, MN': '144', 'Virginia': '46', 'Las Vegas, NV': '417', 'Binghamton, NY': '93', 'Oakland, CA': '413', 'Los Angeles, CA': '390', 'Austin, TX': '320', 'Vermont': '45', 'Grand Rapids, MI': '331', 'Warsaw, IN': '374', 'Columbia, MO': '104', 'Kentucky': '17', 'Morgantown, WV': '299', 'Nebraska': '27', 'New Orleans, LA': '303', 'Iowa': '15', 'Alabama': '53', 'Angola, IN': '366', 'Prairie View, TX': '336', 'Abilene, TX': '391', 'Chicago, IL': '100', 'Plymouth, IN': '375', 'Jacksonville, FL': '295', 'Tennessee': '42', 'Gary, IN': '369', 'Amherst, MA': '90', 'Portland, ME': '129', 'Muncie, IN': '372', 'Orlando, FL': '297', 'Saratoga Springs, NY': '301', 'Reno, NV': '418'}


month_d = [32,29,32,31,32,31,32,32,31,32,31,32]
months = [[i for i in range(1, e)] for e in month_d]


# currently unused and purposeless within the scope of this programs functionality
# yet a good reference of where things started

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print ("Start tag: ", tag)
	def handle_endtag(self, tag):
		print ("End tag: ", tag)
	def handle_data(self, data):
		print ("Data: ", data)


# To manipulate our data we need routes in which to manipulate.  These algorithms grab the data and manipulate it.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## given the xml file url, open and turn into a searchable, iterable document

def get_doc(url):
    f = open(url)
    xml_doc = f.read().split('\n')
    f.close()
    xmldoc = [i.split('\r') for i in xml_doc]
    return xmldoc


## thexml = get_doc(url)
## use thexml generated by get_doc and plug into this algorithm to
## generate all the indices of <titlecities>, which is the city item
## with all said city item's possible destinations as <cityitems>


def get_title_locations_map(thexml):
    city_loc_map = {}
    titles = []
    for i in thexml:
        for e in i:
            if '<titlecity>' in e:
                if thexml.index(i) not in titles:
                    titles.append(thexml.index(i))
                else:
                    if thexml.index(i, titles[-1]+1) not in titles:
                        titles.append(thexml.index(i, titles[-1]+1))
    for e in titles:
        start = thexml[e][0].find('>') + 1
        stop = thexml[e][0].find('</')
        city = thexml[e][0][start:stop]
        city_loc_map[city]=e
    return city_loc_map, titles

def get_title_locations(thexml):
    titles = []
    for i in thexml:
        for e in i:
            if '<titlecity>' in e:
                if thexml.index(i) not in titles:
                    titles.append(thexml.index(i))
                else:
                    if thexml.index(i, titles[-1]+1) not in titles:
                        titles.append(thexml.index(i, titles[-1]+1))
    return titles


## thexml = get_doc(url) and
## titles = get_title_locations(thexml) 
## using the prior defined algorithms to get the necessary data
## to be plugged into generate_routes2 whose purpose is to generate
## a dictionary with each city's name as a key and all of that
## key city's possible destinations as values; created dict returned



def generate_routes2(xml, titles):
    the_dict = {}
    for i in range(len(titles)):
        current_start = xml[titles[i]][0].find('>')+1
        current_stop = xml[titles[i]][0].find('</')
        current_city = xml[titles[i]][0][current_start:current_stop]
        the_dict[current_city] = []
    for i in range(len(titles)):
        current_start = xml[titles[i]][0].find('>')+1
        current_stop = xml[titles[i]][0].find('</')
        current_city = xml[titles[i]][0][current_start:current_stop]
        if i != len(titles)-1:
            current_block = xml[titles[i]:titles[i+1]]
            start = 2
            stop = len(current_block)-3
        elif i == len(titles)-1:
            current_block = xml[titles[i]:]
            start = 2
            stop = len(current_block)-6
        for e in range(start, stop):
            citS = current_block[e][0].find('>')+1
            citST = current_block[e][0].find('</')
            cityitem = current_block[e][0][citS:citST]
            the_dict[current_city] += [cityitem]
    return the_dict

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## one we have run the above functions to parse our xml file and get what we need
## we can iterate through the generated dictionary of city's ard run the below
## algorithms as needed to get pertinent trip itenerary information





# function so we don't repeat any indices
def get_locations(cared_about, from_c):
    city_indices = []
    n = 0
    latest = 0
    for i in cared_about:
            for e in i:
                    if from_c in e.decode('utf-8'):
                            if len(city_indices) == 0:
                                    city_indices.append(cared_about.index(i))
                            else:
                                    latest = city_indices[len(city_indices)-1]
                                    if cared_about.index(i, latest+1) not in city_indices:
                                            city_indices.append(cared_about.index(i, latest+1))	
    return city_indices




# get the cared about portion of the data
def get_cared_about(mb_api, from_city, to_city, d, m, y):
    import urllib2
    data = urllib2.urlopen(mb_api.format(Buses[from_city], Buses[to_city], m, d, y)).read().split('\n')
    new_data = [i.split('\r') for i in data]
    start = 0
    stop = 0
    for i in new_data:
            for e in i:
                    if 'JourneyResylts_OutboundList_GridViewResults_ctl00_row_item' in e:
                            start = new_data.index(i)
                    elif 'footer' in e:
                            stop = new_data.index(i)
    return new_data[start:stop]


# get_cared_about2 is for the new trip purchasing functionality.  We need it to not only return what we care about,
# but also return the URL we got what we care about from so we can pass the URL on to our other functions for use.
# In the end, the URL get_cared_about2 returns will the what the Browser() instance will utilize on the backend to
# literally select and add a trip to a user's basket.

def get_cared_about2(mb_api, from_city, to_city, d, m, y):
	import urllib2
	f = urllib2.urlopen(mb_api.format(Buses[from_city], Buses[to_city], m, d, y))
	data = f.read().split('\n')
	new_data = [i.split('\r') for i in data]
	actual_url = f.geturl()
	start = 0
	stop = 0
	for i in new_data:
    		for e in i:
			if 'JouneyResylts_OutboundList_GridViewResults_ctl00_row_item' in e:
				start = new_data.index(i)
			elif 'footer' in e:
				stop = new_data.index(i)
    	cared = new_data[start:stop]
	return cared, actual_url








# function to take cared_about and get the times

def find_times(cared_about, from_city):
    city_indices = get_locations(cared_about, from_city)
    times = {}
    iteration = 1
    dep_str = ''
    arr_str = ''
		# this lines purpose would be to compensate for re-iterating over the same data
			    #del cared_about[cared_about.index(i)]
    while len(city_indices) > 0:
	#dep_str = ''
	#arr_str = ''
    	curr = city_indices[0]
        del city_indices[0]
        for i in cared_about[curr-2][0]:
        	if i.isdigit():
                	dep_str += i
                elif i.isupper():
                        dep_str += i
        for e in cared_about[curr+7][0]:
                if e.isdigit():
                        arr_str += e
                elif e.isupper():
                        arr_str += e
        times[str(iteration)] = [dep_str, arr_str]
        iteration += 1
	dep_str = ''
	arr_str = ''
    return times
    



# the more correctly formatted find_times algorithm

def find_times2(cared_about, from_city):
    city_indices = get_locations(cared_about, from_city)
    times = {}
    times_list = []
    iteration = 1
    dep_str = ''
    arr_str = ''
    while len(city_indices) > 0:
        #dep_str = ''
        #arr_str = ''
        curr = city_indices[0]
        del city_indices[0]
        for i in cared_about[curr-2][0]:
                if i.isdigit():
                        dep_str += i
                elif i.isupper():
                        dep_str += i
        for e in cared_about[curr+7][0]:
                if e.isdigit():
                        arr_str += e
                elif e.isupper():
                        arr_str += e
        times[str(iteration)] = [dep_str, arr_str]
        iteration += 1
        dep_str = ''
        arr_str = ''
    for i in times.keys():
        times_list.append(times[i][0] + '-' + times[i][1])
    return times_list

# original

def find_times_and_price(cared_about, from_city):
    city_indices = get_locations(cared_about, from_city)
    times = {}
    prices = {}
    times_list = []
    iteration = 1
    dep_str = ''
    arr_str = ''
    price_str = ''
    while len(city_indices) > 0:
        #dep_str = ''
        #arr_str = ''
        curr = city_indices[0]
        del city_indices[0]
        for i in cared_about[curr-2][0]:
                if i.isdigit():
                        dep_str += i
                elif i.isupper():
                        dep_str += i
        for e in cared_about[curr+7][0]:
                if e.isdigit():
                        arr_str += e
                elif e.isupper():
                        arr_str += e
        times[str(iteration)] = [dep_str, arr_str]
        price_string = cared_about[curr+27][0]
        period = price_string.find('.')
        dollars_part = price_string[0:period]
        cents_part = price_string[period:]
        price_str += '$'
        for j in dollars_part:
            if j.isdigit():
                price_str += j
        price_str += '.'
        for n in cents_part:
            if n.isdigit():
                price_str += n
        prices[str(iteration)] = price_str
        iteration += 1
        dep_str = ''
        arr_str = ''
        price_str = ''
    for i in times.keys():
        times_list.append((times[i][0] + '-' + times[i][1], prices[i]))
    return times_list


# new

def find_times_and_price2(cared_about, from_city):
    city_indices = get_locations(cared_about, from_city)
    # when using get_cared_about2 we need the next line
    #del city_indices[0]
    times = {}
    prices = {}
    IDS = {}
    times_list = []
    iteration = 1
    dep_str = ''
    arr_str = ''
    price_str = ''
    ID_str = ''
    while len(city_indices) > 0:
        #dep_str = ''
        #arr_str = ''
        curr = city_indices[0]
        del city_indices[0]
        for i in cared_about[curr-2][0]:
                if i.isdigit():
                        dep_str += i
                elif i.isupper():
                        dep_str += i
        for e in cared_about[curr+7][0]:
                if e.isdigit():
                        arr_str += e
                elif e.isupper():
                        arr_str += e
        times[str(iteration)] = [dep_str, arr_str]
        price_string = cared_about[curr+27][0]
        period = price_string.find('.')
        dollars_part = price_string[0:period]
        cents_part = price_string[period:]
        price_str += '$'
        for j in dollars_part:
            if j.isdigit():
                price_str += j
        price_str += '.'
        for n in cents_part:
            if n.isdigit():
                price_str += n
        prices[str(iteration)] = price_str 
        id_item = cared_about[curr-8][0]
        id_start = id_item.find('value=') + 7
	id_end = id_item.find('"', id_start+1)
	ID_str = id_item[id_start:id_end]
        IDS[str(iteration)] = ID_str
        iteration += 1
        dep_str = ''
        arr_str = ''
	price_str = ''
        ID_str = ''
    for i in times.keys():
        times_list.append([times[i][0] + '-' + times[i][1], prices[i], IDS[i]])
    return times_list


## Last but most importantly, my algorithm to combine the
## data mining tool algorithms into my final data mining
## machine.  As is true in life, tools are components of
## all machines.


def get_future_data(mb_api, from_city, to_city, m, d, months, json_lib):
    #m = int(strftime('%m'))
    #d = int(strftime('%d'))
    y = strftime('%Y')
    for i in range(d, d+1):
        if str(m) == '2':
            if i in months[1]:
                cared_about = get_cared_about(mb_api, from_city, to_city, str(i), str(m), y)
                times = find_times2(cared_about, from_city)
                key = from_city + '-' + to_city + '-' + str(m) + '-' + str(d)
                val = {key: times}
                json_lib.update(val)
            elif i not in months[1]:
                curr = months[m][abs(i-len(months[1]))-1]
                cared_about = get_cared_about(mb_api, from_city, to_city, str(curr), str(int(m)+1), y)
                times = find_times2(cared_about, from_city)
                key = from_city + '-' + to_city + '-' + str(m+1) + '-' + str(curr)
                val = {key: times}
                json_lib.update(val)
        elif str(m) != '2' and i in months[m-1]:
            cared_about = get_cared_about(mb_api, from_city, to_city, str(i), str(m), y)
            times = find_times2(cared_about, from_city)
            key = from_city + '-' + to_city + '-' + str(m) + '-' + str(d)
            val = {key: times}
            json_lib.update(val)
        else:
            curr = months[m][i%len(months[m])]
            cared_about = get_cared_about(mb_api, from_city, to_city, str(i), str(m+1), y)
            times = find_times2(cared_about, from_city)
            key = from_city + '-' + to_city + '-' + str(m+1) + '-' + str(d)
            val = {key: times}
            json_lib.update(val)
    return

  
def get_future_data2test(mb_api, from_city, to_city, months, json_lib):
	m = int(strftime('%m'))
	d = int(strftime('%d'))
	y = strftime('%Y')
	cared_about = get_cared_about(mb_api, from_city, to_city, str(d+1), str(m), y)
	times = find_times2(cared_about, from_city)
	key = from_city + '-' + to_city + '-' + str(m) + '-' + str(d+1)
	val = {key: times}
	json_lib.update(val)
	return "routes finished"


def get_data_from_future(mb_api, from_city, to_city, month, day, months, json_lib):
	y = strftime('%Y')
	cared_about = get_cared_about(mb_api, from_city, to_city, day, month, y)
	times = find_times2(cared_about, from_city)
	key = from_city + '-' + to_city + '-' + str(month) + '-' + str(day)
	val = {key: times}
	json_lib.update(val)
	return "routes for two weeks from now finished"





############################################################################################
# Algorithms to reoccur update event

def make_or_get_day2():
    import os
    from time import strftime
    day = str(int(strftime('%d')))
    try:
            f = open("day.txt").read()
            digits = ''
            for i in f:
                    if i.isdigit():
                            digits += i
            if digits == day:
                    return False
            elif int(day) > int(digits):
                    os.remove("day.txt")
                    f = open("day.txt", "wb")
                    f.write("%s" % day)
                    f.close()
                    return True
    except IOError:
            f = open("day.txt", "wb")
            f.write("%s" % day)
            f.close()
            return True



def update_data(data_dict):
    today = int(strftime('%d'))
    month = int(strftime('%m'))
    for i in data_dict.keys():
    	curr_key = i
        star = curr_key.find('-', curr_key.find('-')+1)
        third_hyph = curr_key.find('-', star+1)
        curr_key_month = int(curr_key[star+1:third_hyph])
        day = int(curr_key[third_hyph+1:])
        if curr_key_month < month:
        	del data_dict[i]
        elif curr_key_month == month:
        	if today > day:
                	del data_dict[i]
        for from_c in routes:
        	for to_c in from_c:
                    get_data_from_future(mb_api, from_c, to_c, month, today+1, months, data_dict) 
    return data_dict


def send_update_email(user_email):
    import smtplib
    import mimetypes
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    mypass = 'megadmin99'
    myacct = 'wesleymadrigal_99@hotmail.com'
    message = 'Hello from MegabusFinder Admin \nIf you are receiving this message it is because you just posted an update to one of our tracked bus routes.  You can view the status of your post and others related to the same trip at %s.\n\n\nRegards\nApp Admin'
    url = 'http://www.megabusfinder.appspot.com/updates/the_bus'
    to_send = message % url
    msg = MIMEMultipart()
    msg['From'] = myacct
    msg['To'] = user_email
    msg['Subject'] = 'Update Notification'
    msg.attach(MIMEText(to_send))
    mailServer = smtplib.SMTP('smtp.live.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(myacct, mypass)
    mailServer.sendmail(myacct, user_email, msg.as_string())
    return

def send_request_email(user_email, url, bus):
	tmp = url
        posit = tmp.find('com') + 3
        new_url = tmp[0:posit] + 'updates'
        bus_f = bus
        url_to_send = new_url + '%s' % bus_f
        message = mail.EmailMessage(sender="MegabusFinder Admin <wesley7879@gmail.com",
                                        subject="Delay Request Post Notification")
        message.to = user_email
        message_body = 'Hello from MegabusFinder Admin \nIf you are receiving this message it is because you just inquired about a particular bus delay status.  If nobody has posted updates regarding the bus you inquired about, please reply to this email with your particular departure and arrival city for your trip.\n\n\nRegards,\nApp Admin'
        message.body = message_body
        message.send()



def update_data2(routes, mb_api, months):
    import logging
    q = BusData.all().fetch(limit=1)
    curr_day = str(int(strftime('%d')))
    curr_m = str(int(strftime('%m')))
    if len(q) >= 1:
        db_day = ''
        db_data = ''
        for i in q:
            bd_day += i.bus_key
            bd_data += i.data
        if int(db_day) < int(curr_day):
            parsable_data = json.loads(db_data)
            for i in parsable_data.keys():
                sec_hyph = i.find('-', i.find('-')+1)
                third_hyph = i.find('-', sec_hyph + 1)
                this_month = i[sec_hyph + 1: third_hyph]
                this_day = i[third_hyph+1: ]
                if int(this_month) < int(curr_m):
                    del parsable_data[i]
                elif int(this_month) == int(curr_m):
                    if int(this_day) < int(curr_day):
                        del parsable_data[i]
            for title_c in routes:
                for item_c in routes[title_c]:
                    get_future_data(mb_api, title_c, item_c, int(curr_m), int(curr_day), months, parsable_data)
            logging.info("Routes Updated!!!")
	    q = BusData.all().filter('bus_key=', db_day)
	    BusData.delete(q)
            logging.info("old deleted")
            bd = BusData(bus_key = curr_day)
            bd.data = json.dumps(parsable_data)
            bd.put()
            return json.dumps(parsable_data)
        else:
            return json.dumps(db_data)
