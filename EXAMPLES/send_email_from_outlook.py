#!/usr/bin/env python

"""
Created on Thu Aug 31 08:17:17 2017

@author: TRSGPL
"""

def email(recipient, subject='[No Subject]', body=' ', attachments=[], external_attachments=[]):
    import win32com.client
    from win32com.client import Dispatch, constants
    const = win32com.client.constants
    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.Subject = subject

    newMail.To = recipient

    for attachment in attachments:
        att = newMail.Attachments.Add(Source=attachment)

        imageCid = "png@123"
        att.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001E", imageCid)

        body = body + "<img src=\"cid:{0}\">".format(imageCid)

    for attachment in external_attachments:
        att = newMail.Attachments.Add(Source=attachment)

    newMail.HTMLBody = body
    return newMail.send


john_gmail = 'jstrickler' + gmail

recip = john_gmail

attach = 'you put something here...'

email(recip
      , subject='Automated Email: Hello from Matts Python Script'
      , body='I figured out how to send an email from python that is compatible with our version of Outlook'
      , external_attachments=[attach]
      )
