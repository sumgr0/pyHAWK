#!/usr/bin/env python
# -*- coding:  latin_1 -*-
# Inspired by Ice3man543's hawkeye 
# https://github.com/Ice3man543/hawkeye (GO)
# just a python adaptation 
# CODED MY METACHAR <TRED LIGHTLY>


#Imports
import os 
import sys
import datetime
from optparse import OptionParser

#Some Things
reload(sys)  
sys.setdefaultencoding('utf8')
now = datetime.datetime.now()

#Graphics
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'

hawk = color.BOLD + color.RED + '''
██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗  
██║  ██║██╔══██╗██║    ██║██║ ██╔╝  
███████║███████║██║ █╗ ██║█████╔╝   
██╔══██║██╔══██║██║███╗██║██╔═██╗   
██║  ██║██║  ██║╚███╔███╔╝██║  ██╗  
╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
[{0}-{1}]──> Coded by Metachar
[{2}-{3}]──> https://github.com/MetaChar
[{4}-{5}]──> version: {6}1.0.0   '''.format(color.CWHITE,color.RED,color.CWHITE,color.RED,color.CWHITE,color.RED,color.GREEN)
logo = hawk.encode('utf8')


# Vars / def #
CryptoFiles  = [".pem",".pkcs12",".p12",".pfx",".asc",".jks",".keychain"]
PasswordFile = [".agilekeychain","credentials.xml",".kwallet", "robomongo.json","filezilla.xml","recentservers.xml", "ventrilo_srv.ini","terraform.tfvars",".bek",".tpm",".psafe3","secret_token.rb","carrierwave.rb","omniauth.rb","settings.py",".exports",".functions",'.extra',".agilekeychain","database.yml"]
DatabaseFile = [".sdf",".sqlite",".fve",".pcap", ".gnucash",".dayone","journal.txt","Favorites.plist",".mdf",]
MiscFile = [ ".log","root.txt","user.txt",'passwords.txt','login.txt']
ConfigurationFile = [".cscfg",".rdp","jenkins.plugins.publish_over_ssh.BapSshPublisherPlugin.xml","LocalSettings.php",".tblk", "configuration.user.xpl","knife.rb",".ovpn",]

#Args
parser = OptionParser()
parser.add_option('--directory','-d',help='Choosen Directory', dest="directory",metavar='directory',action="store", type="string")
(options,args) = parser.parse_args()
if options.directory == None:
    print color.RED + '[!] '+color.CWHITE + 'A directory needs to be defined use '+color.RED + '"-d <directory>" or "--directory <directory>"'+color.END

#Funcs
def time(text):
    print color.GREEN + '[{0}:{1}] {2}'.format(now.hour, now.minute, text)

#Main

def main():
    count = 0
    print logo + '\n'
    try:
        time(color.GREEN + ' [!] '+color.CWHITE+'Directory loaded')
        t = os.listdir(options.directory)
    except OSError:
        time(color.RED + ' [!] ' +color.CWHITE + 'This directory does not exist.')
        exit()
    except TypeError:
        time(color.RED + ' [!] ' +color.CWHITE + 'Use -d or --directory to set a directory.')
        exit()        
    while True:
        count2 = 0
        try:
            filename, file_extension = os.path.splitext(t[count])
            if file_extension in CryptoFiles:
                time(color.GREEN +' [!]'+color.CWHITE +' Crypto file Found in dir '+filename+file_extension)
            if file_extension in PasswordFile:
                time(color.GREEN +' [!]'+color.CWHITE +' Password file Found in dir '+filename+file_extension)
            if file_extension in DatabaseFile:
                time(color.GREEN +' [!]'+color.CWHITE +' Database file Found in dir '+filename+file_extension)
            if file_extension in MiscFile:
                time(color.GREEN +' [!]'+color.CWHITE +' Misc file Found in dir '+filename+file_extension)
            if file_extension in ConfigurationFile:
                time(color.GREEN +' [!]'+color.CWHITE +' Configuration file Found in dir '+filename+file_extension)
            count += 1
        
        except IndexError:
            file_check(count)
def file_check(count):
    t = os.listdir(options.directory)
    count2 = 0
    while True:
        try:
            if t[count2] in CryptoFiles:
                time(color.GREEN +' [!]'+color.CWHITE +' Crypto file Found in dir '+options.directory + '/' + t[count2])
            if t[count2] in PasswordFile:
                time(color.GREEN +' [!]'+color.CWHITE +' Password file Found in dir '+options.directory + '/' + t[count2])
            if t[count2] in DatabaseFile:
                time(color.GREEN +' [!]'+color.CWHITE +' Database file Found in dir '+options.directory + '/' + t[count2])
            if t[count2] in MiscFile:
                time(color.GREEN +' [!]'+color.CWHITE +' Misc file Found in dir '+options.directory + '/' + t[count2])
            if t[count2] in ConfigurationFile:
                time(color.GREEN +' [!]'+color.CWHITE +' Config file Found in dir '+options.directory + '/' +t[count2])
            count2 += 1
        except KeyboardInterrupt:
			exit()
        except IndexError:
            if count == 0:
                if count2 == 0:
                    time(color.RED + ' [!] '+color.CWHITE + "Nothing was found")
            if count > 0:
                time(color.GREEN + ' [!] '+color.CWHITE + 'All Files Scanned!')
                exit()
        except OSError:
            pass
#start
main()