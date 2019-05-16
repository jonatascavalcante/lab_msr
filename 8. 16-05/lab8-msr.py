from github import Github

g = Github("a7ea3343e2e00529d1a27e4a00a93ca61d509fd3")

"""
for repo in g.get_user().get_repos():
    print(repo.name)
"""
print("1 - ")
print(g.get_repo("torvalds/linux").get_languages())


print("2 - ")
for tag in g.get_repo("torvalds/linux").get_tags()[:10]:
    print(tag.name)

print("3 - ")
for repo in g.get_user("torvalds").get_repos():
    print(repo.name)

print("4 - ")
query = "language:c"
for repo in g.search_repositories(query, sort="stars", order="desc"):
    print(repo.full_name)
