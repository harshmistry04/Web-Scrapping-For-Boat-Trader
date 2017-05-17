# In Python
import requests
from bs4 import BeautifulSoup, SoupStrainer

def get_raw_html(url):
    r = requests.get(url)
    return_html = r.text
    return return_html
    pass

start = 1
counter = 0
number_of_ads = 0

f = open('workfile', 'w')

while start < 21: #search vriteria gives 20 pages 
    #raw_html = get_raw_html("http://www.boattrader.com/search-results/NewOrUsed-any/Type-any/Category-all/Zip-33647/Radius-200/Sort-Length:DESC/Page-%s,28?" % start) 
    raw_html = get_raw_html("http://www.boattrader.com/search-results/NewOrUsed-any/Type-any/Category-all/Zip-33702/Radius-10/Sort-Length:DESC/Page-%s,28?" % start)
    #  we start with getting the soup for each page.
    bs_struct = BeautifulSoup(raw_html, "html.parser")
    #  we then look for all the URL
    for sellerlink in bs_struct.find_all('div',{'class': 'contact'}): 
        #print('new iteration')
        #  followed by finding the <a> for each of the <div> element (URL)
        links = sellerlink.find_all('a', href=True)
        if len(links) != 0: # make sure it found something.
            link = links[0].get('href') # getting link mentioned in href
            #print(start)
            #print('http:'+link)
            if link == 'javascript:void(0);': # capture and removal of advertisement
                number_of_ads = number_of_ads + 1
                ad_temp = str(number_of_ads)
                print('ad'+ad_temp)
                continue
            visit_seller = 'http:'+link # making capture URL readable by browser
            visit_seller = visit_seller.encode('utf-8')
            html_seller = get_raw_html(visit_seller)
            soup_seller = BeautifulSoup(html_seller, "html.parser")
            # capturing year of production
            boat_year_raw = soup_seller.find_all('span',{'class': 'bd-year'})
            if len(boat_year_raw)==0:
                #print('inside if')
                boat_year = 'year not specified'
                continue
            else:
                boat_year = boat_year_raw[0].get_text()
            # capturing maker of boat
            #print('make')
            boat_maker_raw = soup_seller.find_all('span',{'class': 'bd-make'})
            boat_maker = boat_maker_raw[0].get_text()
            # capturing model of the boat
            #print('model')
            boat_model_raw = soup_seller.find_all('span',{'class': 'bd-model'})
            boat_model = boat_model_raw[0].get_text()
            #print(boat_model)
            # capturing details
            boat_details_raw = soup_seller.find_all('div',{'class': 'collapsible open'})
            boat_class_raw = boat_details_raw[0].find_all('th',text='Class')
            if len(boat_class_raw)==0:
                boat_class = ' '
            else:
                boat_class = boat_class_raw[0].findNext('td').text
            boat_category_raw = boat_details_raw[0].find_all('th',text='Category')
            if len(boat_category_raw)==0:
                boat_class = ' '
            else:
                boat_category = boat_category_raw[0].findNext('td').text
            boat_length_raw = boat_details_raw[0].find_all('th',text='Length')
            if len(boat_length_raw)==0:
                boat_length
            else:
                boat_length = boat_length_raw[0].findNext('td').text
            boat_proptype_raw = boat_details_raw[0].find_all('th',text='Propulsion Type')
            if len(boat_proptype_raw)==0:
                boat_proptype = ' '
            else:
                boat_proptype = boat_proptype_raw[0].findNext('td').text
            boat_fueltype_raw = boat_details_raw[0].find_all('th',text='Fuel Type')
            if len(boat_fueltype_raw)==0:
                boat_fueltype = ' '
            else:
                boat_fueltype = boat_fueltype_raw[0].findNext('td').text
            boat_location_raw = boat_details_raw[0].find_all('th',text='Location')
            if len(boat_location_raw)==0:
                boat_location = ' '
            else:
                boat_location = boat_location_raw[0].findNext('td').text
            # engine details
            boat_engdetails_raw = soup_seller.find_all('div',{'class': 'collapsible'})
            if len(boat_engdetails_raw)<=3:
                continue
            boat_engmake_raw = boat_engdetails_raw[3].find_all('th',text='Engine Make')
            if len(boat_engmake_raw)==0:
                boat_engmake = ' '
            else:
                boat_engmake = boat_engmake_raw[0].findNext('td').text
            boat_totpwr_raw = boat_engdetails_raw[3].find_all('th',text='Total Power')
            if len(boat_totpwr_raw)==0:
                boat_totpwr = ' '
            else:
                boat_totpwr = boat_totpwr_raw[0].findNext('td').text
            boat_enghrs_raw = boat_engdetails_raw[3].find_all('th',text='Engine Hours')
            if len(boat_enghrs_raw)==0:
                boat_enghrs = ' '
            else:
                boat_enghrs = boat_enghrs_raw[0].findNext('td').text
            boat_engtype_raw = boat_engdetails_raw[3].find_all('th',text='Engine Type')
            if len(boat_engtype_raw)==0:
                boat_enghrs == ' '
            else:
                boat_engtype = boat_engtype_raw[0].findNext('td').text
            # Capturing price of the boat
            boat_price_raw = soup_seller.find_all('span',{'class': 'bd-price contact-toggle'})
            boat_price = boat_price_raw[0].get_text()
            #print(boat_price)
            # capturing contact number of the seller
            boat_contact_raw = soup_seller.find_all('div',{'class': 'contact'})
            boat_contact = boat_contact_raw[0].get_text()
            #print(boat_contact)
            counter = counter + 1
            number = str(counter)
            #print(number+";"+boat_year.strip('\n')+";"+boat_maker.strip('\n')+";"+boat_model.strip('\n')+";"+boat_contact.strip('\n')+";"+boat_price.strip('\n'))
            print(number)
            file_record = (number+";"+boat_year.strip('\n')+";"+boat_class.strip('\n')+";"+boat_category.strip('\n')+";"+boat_length.strip('\n')+";"+
            boat_proptype.strip('\n')+";"+boat_fueltype.strip('\n')+";"+boat_engmake.strip('\n')+";"+boat_totpwr.strip('\n')+";"+boat_enghrs.strip('\n')+";"+
            boat_engtype.strip('\n')+";"+boat_location.strip('\n')+";"+boat_maker.strip('\n')+";"+boat_model.strip('\n')+";"+boat_contact.strip('\n')+";"+
            boat_price.strip('\n')+"\n")
            f.write(file_record) # writing the same into file
    start = start + 1
number_of_ads = str(number_of_ads)
advertisement_record = 'Total number of ads for search criteria'+number_of_ads
f.close()       


