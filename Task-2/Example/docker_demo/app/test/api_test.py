# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 23:08:18 2023

@author: Neal
"""

import requests

header = { "accept":"application/json",
            "Content-Type": "application/json"}

test_data = ["According to Scanfil , demand for telecommunications network products has fluctuated significantly in the third quarter of 2006 , and the situation is expected to remain unstable for the rest of the year .",
             "From: boylan@sltg04.ljo.dec.com (Steve Boylan)\nSubject: Re: Christian Daemons? [Biblical Demons, the update]\nReply-To: boylan@ljohub.enet.dec.com (Steve Boylan)\nOrganization: Digital Equipment Corporation\nLines: 61\n\n\nIn article <1993Apr1.024850.20111@sradzy.uucp>, radzy@sradzy.uucp\n(T.O. Radzykewycz) writes:\n\n> >>swaim@owlnet.rice.edu (Michael Parks Swaim) writes:\n> >>>  666, the file permission of the beast.\n> \n> >radzy@sradzy.uucp (T.O. Radzykewycz) writes:\n> >> Sorry, but the file permission of the beast is 600.\n> >> \n> >> And the file permission of the home directory of the\n> >> beast is 700.\n> \n> boylan@sltg04.ljo.dec.com (Steve Boylan) writes:\n> >Hey, radzy, it must depend on your system's access policy.\n> >I get:\n> >\t$ ls -lg /usr/users\n> >\ttotal 3\n> >\tdrwxrwxrwx 22 beast    system       1536 Jan 01  1970 beast\n> >\tdrwxr-x--x 32 boylan   users        2048 Mar 31 09:08 boylan\n> >\tdrwxr-xr-x  2 guest    users         512 Sep 18  1992 guest\n> >\t$ su\n> >\tPassword:\n> >\troot $ su beast\n> >\tbeast $ umask\n> >\t111\n> >\tbeast $ ^D\n> >\troot $ ^D\n> >\t$ \n> \n> Just a minute....\n> \n> \t$ grep beast /etc/passwd\n> \tbeast:k5tUk76RAUogQ:497:0:Not Walt Disney!:/usr/users/beast:\n> \t$ mv /usr/users/beast/.profile /usr/users/beast/.profile,\n> \t$ echo umask 077 >> /usr/users/beast/.profile\n> \t$ cat > /usr/users/beast/.profile\n> \tchmod 700 /usr/users/beast\n> \tmv .mailrc .mailrc,\n> \techo beast logged in | mail radzy%sradzy@jack.sns.com\n> \tmv .mailrc, .mailrc\n> \tmv /usr/users/beast/.profile, /usr/users/beast/.profile\n> \t^D\n> \t$ chmod 777 /usr/users/beast/.profile\n> \t$ cat /usr/users/beast/.profile, >> /usr/users/beast/.profile\n> \n> <waits a while, finally gets mail.>\n> \n> I think you made a mistake.  Check it again.\n> \n\nI see . . . you're not running Ultrix!\n\n\t:-)\n\n\t\t\t\t- - Steve\n\n\n--\nDon't miss the 49th New England Folk Festival,\nApril 23-25, 1993 in Natick, Massachusetts!\n"]


#url = 'http://localhost:9000/predict'
url = 'http://10.31.167.99:9000/predict'

for title in test_data:
    myobj = {'news_title':  title}
    # print(myobj)
    x = requests.post(url, 
                      headers = header,
                      json = myobj)
    print(x.text)



