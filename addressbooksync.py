#!/usr/bin/python
from printers import Ricoh
import os 
import traceback
import requests

# Configuration settings

printers = ['10.0.0.10']
adminuser = 'admin'
password = 'password'
intrays = './testfolders/'
domain = '@example.org'
shareprefix = '\\\\fileserver\\vcintrays\\'

# Names that are not allowed to be in the address book
blacklist = set(['admin'])

# First get set of folders we have on the server
folders = set([f.name for f in os.scandir(intrays) if f.is_dir()])

print("Folders on Server:", len(folders))

# Compile list of truncated folder names (as printer is limited to 20 characters)
folderstrunc = {}
for s in folders:
   folderstrunc[s[:20]] = s 



# Access via context manager so that all connections are closed automatically.

for printerip in printers:
    print("== UPDATING PRINTER ", printerip, " ==")

    ricoh = None    
    try:
        with Ricoh(host=printerip,username=adminuser,password=password) as ricoh:
            print(repr(ricoh))

            remainingfolders = folders.copy()


            for user in ricoh:
                # Note: Deliberately check against the full list in case there are dupes
                if (user.name[:20] in folderstrunc):
                    # User exists on printer and on filesystem. Nothing to do
                    remainingfolders.remove(folderstrunc[user.name[:20]])
                else: 
                    print("Removing user: ", user.id, user.name)
                    ricoh.delete_user(user.id)


            # Now anything left in remainingfolders exists on the server, but not in this printer.  Lets go and add those

            for username in remainingfolders:
                if username in blacklist:
                    continue
                print ("Adding user: ", username)

                # Convert a user-id into a name
                fullname = username.replace('.',' ').title() 
                    
                # Convert user-id to an email address
                email = username + domain

                ricoh.add_user(userid=username[:20], name=username[:20], displayName=fullname[:16], email=email, path='\\\\virtualcabinet.stmgroup.network\\vcintrays\\' + username)


    except:
        print("Problem updating printer: ", printerip)
        print(traceback.format_exc())

print ("All Done")

