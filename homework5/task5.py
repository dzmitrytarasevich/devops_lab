import datetime
import requests

# github_api_name = input("Input Github_login: ")
# github_api_password = input("Input Github_password: ")


def help_f():
    """Display program manual"""
    print("""Usage:
   pr-stats [options] <user> [<repo>]
   pr-stats --version
   pr-stats (-h | --help)

Options:
   -h --help                     Show this screen.
   -q --quit                     Quit from the program.
      --version                  Print the program's installed version.
      --basic                    Basic statistics about merged/closed rate.
      --day-created              Analyze day of the week opened.
      --day-closed               Analyze day of the week closed.
      --hour-created             Analyze hour of the day opened.
      --hour-closed              Analyze hour of the day closed.
      --user-creating            Analyze user who opened.
      --attached-labels          Analyze attached labels.""")


help_f()

url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all'
request = requests.get(url, params={'page': 1, 'per_page': 10},
                       auth=(github_api_name, github_api_password))
output = []
output += request.json()

while 'next' in request.links.keys():
    url = request.links['next']['url']
    request = requests.get(url,
                           auth=(github_api_name, github_api_password))
    output += request.json()


def version():
    """Display program version"""
    print('The program version is 1.0')


def day_created(data, value):
    """Display day of the week when pr was created"""
    date = data[value][:10].split('-')
    print('Day of the week ' + value + ': ' + str(
        datetime.datetime(int(date[0]), int(date[1]), int(date[2])).strftime("%a")))
