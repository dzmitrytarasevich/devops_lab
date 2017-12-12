import argparse
import requests
import getpass

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-u', '--user', type=str, help='user whom data you want go get, how to use: '
                                                   '(-u {name of the user})')
parser.add_argument('-o', '--opnd', type=str, help='display number of opened and closed repos, how to use: (-m opnd)')
parser.add_argument('-l', '--label', type=str, help='display number of labels, how to use: (-l label)')
parser.add_argument('-p', '--pull', type=str, help='display numbers of users pull requests, how to use: (-p pull)')
parser.add_argument('-t', '--time', type=str, help='display creation time of pull requests, how to use: (-t time)')
parser.add_argument('-w', '--body', type=str, help='display user commits names, how to use: (-w body)')
parser.add_argument('-d', '--id', type=str, help='display user pull ids, how to use: (-d id)')
parser.add_argument('-user', '--gituser', type=str, help='git username, how to use: (-user {git username})')
parser.add_argument('-repo', '--gitrepo', type=str, help='git repo, how to use: (-repo {git repo})')
results = parser.parse_args()

gituser = str(results.gituser)
repo = str(results.gitrepo)
o = str(results.opnd)
label = str(results.label)
p = str(results.pull)
t = str(results.time)
w = str(results.body)
d = str(results.id)
user = str(results.user)
print(user + '\n')
print('Example how to use this script: $ python3 pr-stats.py -o opnd -l label -u k-koleda -p pull -t time -w body -d '
      'id -user alenapy -repo devops_lab'+'\n')

name = input("enter github username please: ")

password = getpass.getpass()

opened = 0
closed = 0
labels = 0


r = requests.get('https://api.github.com/repos/'+str(gituser)+'/'+str(repo)+'/pulls?state=all', auth=(name, password))
a = r.json()
nmbr = ((a[0]['number']) // 30) + 1

if o == 'opnd':

    for b in range(1, nmbr):
        r = requests.get('https://api.github.com/repos/'+str(gituser)+'/'+str(repo)+'/pulls?state=all&page='+str(b),
                         auth=(name, password))
        a = r.json()

        for i in a:
            if i['state'] == 'open':
                opened += 1
            elif i['state'] == 'closed':
                closed += 1

    print('Number of closed: ' + str(closed) + ' ' + 'Number of opened: ' + str(opened))

if label == 'label':

    for b in range(1, nmbr):
        r = requests.get('https://api.github.com/repos/'+str(gituser)+'/'+str(repo)+'/pulls?state=all&page='+str(b),
                         auth=(name, password))
        a = r.json()

        for i in a:
            if i['base']['label']:
                labels += 1

    print('Number of labels: ' + str(labels))


if p == 'pull':
    for b in range(1, nmbr):
        r = requests.get('https://api.github.com/repos/'+str(gituser)+'/'+str(repo)+'/pulls?state=all&page='+str(b),
                         auth=(name, password))
        a = r.json()

        for i in a:
            if i['user']['login'] == user:
                print('Pull request number: '+str(i['number']))


if t == 'time':
    for b in range(1, nmbr):
        r = requests.get('https://api.github.com/repos/'+str(gituser)+'/'+str(repo)+'/pulls?state=all&page='+str(b),
                         auth=(name, password))
        a = r.json()

        for i in a:
            if i['user']['login'] == user:
                print('Pull request of '+str(user)+' was created at: '+str(i['created_at']))

if w == 'body':
    for b in range(1, nmbr):
        r = requests.get('https://api.github.com/repos/'+str(gituser)+'/'+str(repo)+'/pulls?state=all&page='+str(b),
                         auth=(name, password))
        a = r.json()

        for i in a:
            if i['user']['login'] == user:
                print('Commits names is: '+str(i['body']))


if d == 'id':
    for b in range(1, nmbr):
        r = requests.get('https://api.github.com/repos/'+str(gituser)+'/'+str(repo)+'/pulls?state=all&page='+str(b),
                         auth=(name, password))
        a = r.json()

        for i in a:
            if i['user']['login'] == user:
                print('ID is: '+str(i['id']))
