# Github Top Repos

> Get the most starred repositories among the ones created in last X days

### Installation
This tool uses [github3.py](https://github.com/sigmavirus24/github3.py) to talk with GitHub Search API.

Clone this repository and run:
```shell
pip install -r requirements.txt
```

#### Usage
```
GH_USER  - Environment variable to specify github user
GH_PWD   - Environment variable to specify password
GH_TOKEN - Environment variable to specify github token
```

Some example usages are listed below:

```shell
$ python gh-top-repos.py --help                                        # help screen
usage: gh-top-repos.py [-h] [-v] [-c DAYS_COUNT] [-n NUM_OF_REPOS] [-s]
                       [-q CUSTOM_QUERY] [-f]

Search github for top repositories

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -c DAYS_COUNT, --count DAYS_COUNT
                        Number of days before today to begin search with
  -n NUM_OF_REPOS, --num NUM_OF_REPOS
                        Number of repositories to return
  -s, --star            Star the repos returned by search
  -q CUSTOM_QUERY, --query CUSTOM_QUERY
                        Provide custom query for search eg.
                        language:javascript
  -f, --fork            Fork the repos returned by search

$ python gh-top-repos.py -q "language:javascript"                       # Sample output example
[
    {
        "lang": "JavaScript",
        "name": "ruanyf/react-babel-webpack-boilerplate",
        "url": "https://github.com/ruanyf/react-babel-webpack-boilerplate",
        "forks_count": 35,
        "stargazers_count": 331,
        "desc": "a boilerplate for React-Babel-Webpack project"
    },
    {
        "lang": "JavaScript",
        "name": "hustcc/redis-monitor",
        "url": "https://github.com/hustcc/redis-monitor",
        "forks_count": 27,
        "stargazers_count": 235,
        "desc": "A web visualization redis monitoring program. Performance optimized and very easy to install and deploy, base on Flask and sqlite."
    },
    {
        "lang": "JavaScript",
        "name": "chinchang/code-blast-codemirror",
        "url": "https://github.com/chinchang/code-blast-codemirror",
        "forks_count": 30,
        "stargazers_count": 109,
        "desc": "Particles blasts while typing in Codemirror"
    }
]

python gh-top-repos.py                                                  # default search; does not star or fork

python gh-top-repos.py -c 30                                            # look for repos created in last 30 days, default: 30

python gh-top-repos.py -n 3                                             # search all repos of an organization, default: 3

GH_USER=techgaun GH_PWD=<mypass> python gh-top-repos.py -n 1 -s         # Star the highest starred repo automatically

GH_TOKEN=<github_token> python gh-top-repos.py -n 1 -f                  # For the highest starred repo automatically

python gh-top-repos.py -n3 -q "language:javascript"                     # Find top 3 starred repos written(mainly) in javascript
```

### Contribution
Any cool/useful feature/idea on this project is warmly welcomed.

### Author

Samar Dhwoj Acharya
