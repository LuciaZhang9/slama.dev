#!/usr/bin/env python3

import os
import requests

try:
    from github import Github

    from secrets import github_token

    g = Github(github_token)

    # (GitHub name, override display name, override language)
    projects = [
        ("Florodoro", None, None),
        ("Donjun", None, None),
        ("Grafatko", "Grafátko", None),
        ("Voronoi", None, None),
        ("Robotics-Simplified-Website", "Robotics Simplified", "HTML"),
        ("PurePursuitAlgorithm", "Pure Pursuit", None),
        ("CV", "CV generator", None),
        ("Smichoff-Trophy", "Smíchoff Trophy", "Fusion 360"),
    ]

    result = ""
    i = 0
    for project, name, language in projects:
        repo = g.get_repo(f"xiaoxiae/{project}")

        result += f"""<table class="gh{'Right' if i % 2 == 1 else 'Left'}">
        <thead>
          <tr>
            <th class="ghName" colspan="2"><a href="{repo.html_url}">{name or repo.name}</a></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="ghDescription" colspan="2">{repo.description}</td>
          </tr>
          <tr>
            <td class="ghStars">{repo.stargazers_count} ⭐</td>
            <td class="ghLang">{language or repo.language}</td>
          </tr>
        </tbody>
        </table>"""

        i += 1

    base = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base, "../_includes/projects.md"), "w") as f:
        f.write(result)

    print("generated.", flush=True)
except requests.exceptions.ConnectionError:
    print("network could not be reached, projects not generated.", flush=True)
