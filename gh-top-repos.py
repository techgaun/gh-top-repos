#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
gh-top-repos

Author: https://github.com/techgaun

"""

import github3 as github
import os
import argparse
import json
from datetime import datetime, timedelta


gh_user = os.getenv('GH_USER', None)
gh_pass = os.getenv('GH_PWD', None)
gh_token = os.getenv('GH_TOKEN', None)

gh = github.GitHub(username=gh_user, password=gh_pass, token=gh_token)


def search(
    days_count=None, num_of_repos=None, star_repos=None,
        fork_repos=None, custom_query=None):
    if not days_count:
        days_count = 7

    if not num_of_repos:
        num_of_repos = 3

    initial_date = datetime.now() - timedelta(days=days_count)
    initial_date = initial_date.strftime('%Y-%m-%d')

    query = 'created:>' + initial_date
    if custom_query and isinstance(custom_query, str):
        query = ' '.join([query, custom_query])
    try:
        search_results = gh.search_repositories(
            query,
            sort='stars',
            order='desc',
            number=num_of_repos
        )
        repos_found = []
        for search_result in search_results:
            repo = {
                'name': search_result.repository.full_name,
                'desc': search_result.repository.description,
                'lang': search_result.repository.language,
                'stargazers_count': search_result.repository.stargazers_count,
                'forks_count': search_result.repository.forks_count,
                'url': search_result.repository.html_url
            }

            if gh.session.auth:
                if fork_repos:
                    search_result.repository.create_fork()

                if star_repos:
                    gh.star(search_result.repository.owner,
                            search_result.repository.name)

            repos_found.append(repo)

        if not repos_found:
            print "No repositories found for your search."
            return

        print(json.dumps(repos_found, indent=4, separators=(',', ': ')))

    except github.exceptions.GitHubError as e:
        print("GitHub related error occurred")
        print(e)

    except Exception as e:
        print(e)


def main():
    parser = argparse.ArgumentParser(
        description='Search github for top repositories',
        epilog='With love, from Nepal'
    )

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s 0.1.0'
    )

    parser.add_argument(
        '-c',
        '--count',
        dest='days_count',
        type=int,
        action='store',
        help='Number of days before today to begin search with'
    )

    parser.add_argument(
        '-n',
        '--num',
        dest='num_of_repos',
        type=int,
        action='store',
        help='Number of repositories to return',
    )

    parser.add_argument(
        '-s',
        '--star',
        dest='star_repos',
        action='store_true',
        help='Star the repos returned by search'
    )

    parser.add_argument(
        '-q',
        '--query',
        dest='custom_query',
        action='store',
        help='Provide custom query for search eg. language:javascript'
    )

    parser.add_argument(
        '-f',
        '--fork',
        dest='fork_repos',
        action='store_true',
        help='Fork the repos returned by search'
    )

    args = parser.parse_args()
    search(
        days_count=args.days_count,
        num_of_repos=args.num_of_repos,
        star_repos=args.star_repos,
        fork_repos=args.fork_repos,
        custom_query=args.custom_query
    )

if __name__ == '__main__':
    main()
