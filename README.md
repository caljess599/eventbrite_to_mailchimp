# eventbrite_to_mailchimp
python script that puts eventbrite RSVPs into specific mailchimp list

## Synopsis

This python script leverages the Mailchimp v3.0 API and Eventbrite v3 API (both usable with free accounts) to:
1) collect Eventbrite RSVPs to a specified live event and cross-references the email addresses against a specific list mailchimp list 
2) Adds the email addresses not on the first specified mailing list to a second specified mailchimp mailing list (could be the same list)

There is no need to worry about duplicates being added because the POST call automatically rejects them, so the script can be run at different points during the RSVP period with no worries.

## Motivation

My organization uses Eventbrite for event management but Mailchimp for communications. We wanted a way to invite people who RSVPed via Eventbrite to join our Mailchimp mailing list--if they weren't already on it--by adding those addresses to a separate mailchimp list that would be used to send invitations to join the mailing list.

I wrote this because there isn't a python wrapper for the v3.0 Mailchimp API because it is new.

## Installation

All you need is the script. Remember to change the variables (left blank) to reflect your account/lists.

# VARIABLES
# Mailchimp
# Getting started with mailchimp API: http://developer.mailchimp.com/documentation/mailchimp/guides/get-started-with-mailchimp-api-3/
mcprivatekey = '' #this is your api key that allows you access
mcregion = '' #this is the <dc> (datacenter) where your account is, us11, us6, etc. It's in your url when you are logged in.
mchttppass = mcprivatekey + '-' + mcregion
# How to find a mailchimp list id: http://kb.mailchimp.com/lists/managing-subscribers/find-your-list-id
mcchecklistid = '' #the first list, the one you want to check the RSVPs against
mcpostlistid = ''  #the second list, the one to which you want to post the RSVP emails not on the first list

#Eventbrite
# https://www.eventbrite.com/developer/v3/quickstart/
eboauthtoken = '' #Your OAthtoken
ebliveeventid = '' #The id of the live event

## Contributors

Just me so far.

## License

None.
