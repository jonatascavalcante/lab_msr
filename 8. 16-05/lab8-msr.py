from github import Github

TOKEN_SAMUEL = "a7ea3343e2e00529d1a27e4a00a93ca61d509fd3"
TOKEN_JONATAS = "a7575b8feaa470e3116995c2e50b2c8e2c12d46d"

g = Github(TOKEN_JONATAS)

print("\nQuestao 1")
print(g.get_repo("torvalds/linux").get_languages())

print("\nQuestao 2")
for tag in g.get_repo("torvalds/linux").get_tags()[:10]:
    print(tag.name)

print("\nQuestao 3")
for repo in g.get_user("torvalds").get_repos():
    print(repo.name)

print("\nQuestao 4")
query = "language:c"
for repo in g.search_repositories(query, sort="stars", order="desc")[:10]:
    print(repo.full_name)

print("\nQuestao 5")
query = "language:c"
for repo in g.search_repositories(query, sort="forks", order="desc")[:10]:
    print(repo.full_name)

print("\nQuestao 6")
query = "topic:microservices"
for repo in g.search_repositories(query, sort="stars", order="desc")[:10]:
    print(repo.full_name)

print("\nQuestao 7")
query = "language:javascript topic:html5"
for repo in g.search_repositories(query, sort="stars", order="desc")[:10]:
    print(repo.full_name)

print("\nQuestao 8")
query = "fakenews"
for repo in g.search_repositories(query, sort="stars", order="desc")[:10]:
    print(repo.full_name)

print("\nQuestao 9")
query = "android in:name"
for repo in g.search_repositories(query)[:10]:
    print(repo.full_name)

print("\nQuestao 10")
query = "android client in:description"
for repo in g.search_repositories(query)[:10]:
    print(repo.full_name)

print("\nQuestao 11")
query = "circleCI in:readme"
for repo in g.search_repositories(query)[:10]:
    print(repo.full_name) 

print("\nQuestao 12")
query = "label:critical language:javascript"
for issue in g.search_issues(query)[:10]:
    print(issue.title) 

print("\nQuestao 13")
query = "label:bug language:Go state:closed"
for issue in g.search_issues(query)[:10]:
    print(issue.title) 

print("\nQuestao 14")
query = "label:needhelp language:javascript state:open"
for issue in g.search_issues(query)[:10]:
    print(issue.title)

print("\nQuestao 15")
query = "label:feature state:open"
for issue in g.search_issues(query, sort="created", order="asc")[:10]:
    print(issue.title)
