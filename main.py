#!/bin/python

# IMPORTS
import requests
from requests.auth import HTTPBasicAuth
from eventbrite import Eventbrite
import hashlib
import re
import json

# VARIABLES
# edit below to define your own variables
# Mailchimp
mcprivatekey = ''
mcregion = ''
mchttppass = mcprivatekey + '-' + mcregion
mcchecklistid = ''
mcpostlistid = ''

#Eventbrite
eboauthtoken = ''
ebliveeventid = ''

# FUNCTIONS
# make md5 hash of email address
def mailchimp_call(hashedemail):
        url_base = 'https://' + mcregion + '.api.mailchimp.com/3.0/lists/' + mcchecklistid + '/members/'
        url = url_base + hashedemail
        user = HTTPBasicAuth('anystring', mchttppass)
        fields = {'fields': 'email_address'}
        r = requests.get(url, auth=user, params=fields)
        return r.content

# make json object for POST request
def makedatadict(listofemails):
        dictlist=[]
        for email in listofemails:
                m = {'email_address':email,'status':'subscribed'}
                dictlist.append(m)
        return dictlist

# send mailchimp POST request
def mailchimp_post(jsonobject):
        url  = 'https://' + mcregion + '.api.mailchimp.com/3.0/lists/' + mcpostlistid + '/members/'
        user = HTTPBasicAuth('anystring', mchttppass)
        request = requests.post(url, auth=user, data=json.dumps(jsonobject))
        return request.content

# MAIN PROGRAM
# get live event orders from Eventbrite
eventbrite = Eventbrite(eboauthtoken)
p = eventbrite.get_event_attendees(ebliveeventid)
lo_emails=[]
for index in range(len(p['attendees'])):
        g = p['attendees'][index]['profile']
        if 'email' in g:
                lo_emails.append(g['email'])

# hash those emails into md5
hashed_emails=[]
for email in lo_emails:
        s = hashlib.md5( email ).hexdigest()
        hashed_emails.append(s)

# check each address for presence on specified list
mailchimp_responses=[]
for email in hashed_emails:
        u = mailchimp_call(email)
        mailchimp_responses.append(u)
        
# edit the results to see which emails are on the list and which aren't
# note: mailchimp_responses is a list of dictionaries, so x is a dictionary!
mailchimp_edited=[]
for x in mailchimp_responses:
        if 'title' in x:
                mailchimp_edited.append('appears not to be on the mailing list. Check for typos')
        else:
                q = x.split(':')[1]
                y = q.split('\"')[1]
                mailchimp_edited.append(y)

#output
list_length=len(lo_emails)
print "There are", list_length, "RSVPs to live event", ebliveeventid

# make a list of only emails to be added
final_results=[]
for i in range(list_length):
        print(lo_emails[i] + ':' + mailchimp_edited[i])
        a = lo_emails[i]
        b =  mailchimp_edited[i]
        if a != b:
                final_results.append(a)

# print that list
print(final_results)
ps = makedatadict(final_results)
print(ps)

# post entries to mailchimp list
for dict in ps:
        t = mailchimp_post(dict)
        print(t)
