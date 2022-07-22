# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:31:21 2022

@author: PC
"""

import requests, json
from collections import Counter
from dateutil.parser import parse

github_user = "rafa238"
endpoint = f"https://api.github.com/users/{github_user}/repos"

repos = json.loads(requests.get(endpoint).text)

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

last_5_repositories = sorted(repos,
                             key=lambda r: r["pushed_at"],
                             reverse=True)[:5]

last_5_languages = [repo["language"]
                    for repo in last_5_repositories]
