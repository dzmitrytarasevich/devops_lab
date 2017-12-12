import requests
import argparse
import getpass

countM = 0
countC = 0
parser = argparse.ArgumentParser(description='''EXAMPLES: "python script.py -st k-koleda", info only for 1 student
"python script.py -co" for all use and output merged/closed info
"python script.py -ow alenaPy -re devops_lab -co -cm" for another repo with merged/closed info and without
comment count info''', formatter_class=RawTextHelpFormatter)
parser.add_argument('-st', action='store', dest='student', help='Enter student login ex: "kiryl_k" or "all" for all '
                                                                'students', type=str, default="all")
parser.add_argument('-ow', action='store', dest='owner', help='Enter login repo owner default: alenaPy',
                    type=str, default="alenaPy")
parser.add_argument('-re', action='store', dest='repo', help='Store a simple value default: devops_lab', type=str,
                    default="devops_lab")
parser.add_argument('-co', action='store', dest='count', help='merged/closed default: NO', type=str, default="no")
parser.add_argument('-cm', action='store', dest='comm', help='Enable count of comment default: YES', type=str,
                    default="yes")
parser.add_argument('-lb', action='store', dest='label', help='Enable label of PR default: YES', type=str,
                    default="yes")
parser.add_argument('-cr', action='store', dest='created', help='Enable creation date of PR default: YES', type=str,
                    default="yes")
parser.add_argument('--version', '-v', action="version", version="version 0.9")
parser.add_argument('-cl', action='store', dest='closed', help='closed date default: YES', type=str, default="yes")
args = parser.parse_args()
st = args.student
ow = args.owner
re = args.repo
co = args.count
cm = args.comm
lb = args.label
cr = args.created
login = str(input('login: '))
p = getpass.getpass()
r = requests.get('https://api.github.com/repos/'+str(ow)+'/'+str(re)+'/pulls?state=all&per_page=1000', auth=(str(login),
                                                                                                             p))
first_ind = r.json()[0]['number']
for i in range(first_ind):
    if st == "all":
        print("Number of pull request: ", r.json()[i]['number'])
        print("Created by: ", r.json()[i]['head']['user']['login'])
        print("Title: ", r.json()[i]['title'])
        print("Current state: ", r.json()[i]['state'])
        if cr == "yes":
            print("Created at: ", r.json()[i]['created_at'])
        if r.json()[i]['state'] == "closed":
            countC += 1
        if r.json()[i]['merged_at'] != None:
            countM += 1
        if lb == "yes":
            ll = requests.get('https://api.github.com/repos/'+ow+'/'+re+'/issues/' + str(r.json()[i]['number']),
                              auth=(str(login), p))

           if ll.json()['labels'] != []:
               print("There is label: ", ll.json()['labels'][0]['name'])
        if r.json()[i]['state'] == 'closed':
            if cm == "yes":
                print("Closed by: ", r.json()[i]['base']['user']['login'])
                print("Closed at: ", r.json()[i]['closed_at'])
                c = requests.get(
                'https://api.github.com/repos/'+ow+'/'+re+'/issues/' + str(r.json()[i]['number']) + '/comments',
                auth=(str(login), p))
                print("Number of comments: ", len(c.json()[:]))
            print(" ")
        else:
            if cm == "yes":
                c = requests.get(
                'https://api.github.com/repos/'+ow+'/'+re+'/pulls/' + str(r.json()[i]['number']) + '/comments',
                auth=(str(login), p))
                print("Number of comments: ", len(c.json()[:]))
                print(" ")
                print(" ")
    elif st == r.json()[i]['head']['user']['login']:
        print("Number of pull request: ", r.json()[i]['number'])
        print("Created by: ", r.json()[i]['head']['user']['login'])
        print("Title: ", r.json()[i]['title'])
        print("Current state: ", r.json()[i]['state'])
        if cr == "yes":
             print ("Created at: ", r.json()[i]['created_at'])
        if r.json()[i]['state'] == 'closed':
             if cm == "yes":
                 print("Closed by: ", r.json()[i]['base']['user']['login'])
                 print("Closed at: ", r.json()[i]['closed_at'])
        if lb == "yes":
           ll = requests.get(
            'https://api.github.com/repos/'+ow+'/'+re+'/issues/' + str(r.json()[i]['number']),
            auth=(str(login), p))
           if ll.json()['labels'] != []:
               print("There is label: ", ll.json()['labels'][0]['name'])
        print(" ")
        print(" ")
if co == "yes":
   print ("Count merged: ", countM)
   print ("Count: closed: ", countC)