from git import Repo
import platform
import networkx as nx
import matplotlib.pyplot as plt

if platform.system() == "Windows":
	ANALYZED_REPO = 'C:\\Users\\samue\\EventBus'
else:
	ANALYZED_REPO = '/Users/jonatascavalcante/Projects/EventBus'
	
def get_all_project_files(commits):
	all_project_files = set()

	for commit in commits:
		commit_files = commit.stats.files.keys()
		for file in commit_files:
			all_project_files.add(file)
	return all_project_files

def connect_files_commited_together(all_commits, G):
   
	for commit in all_commits:
		commit_files = list(commit.stats.files.keys())
		for i in range(len(commit_files)):
			if commit_files[i].endswith(".java"):
				for j in range(i+1, len(commit_files)):
					if commit_files[j].endswith(".java"):
						if G.has_edge(commit_files[i],commit_files[j]):
							G[commit_files[i]][commit_files[j]]['weight'] += 1
						else:
							G.add_edge(commit_files[i],commit_files[j], weight=1)
						if G.has_edge(commit_files[j],commit_files[i]):
							G[commit_files[j]][commit_files[i]]['weight'] += 1
						else:
							G.add_edge(commit_files[j],commit_files[i], weight=1)		
repo = Repo(ANALYZED_REPO)
all_commits = list(repo.iter_commits('master'))

all_project_files = get_all_project_files(all_commits)

G = nx.Graph()
wG = nx.Graph()

for project_file in all_project_files:
	G.add_node(project_file)

connect_files_commited_together(all_commits, G)

for node in G:
	wG.add_node(node)
	for edge in G[node]:
		if G[node][edge]['weight'] > 10:
			wG.add_edge(node, edge, weight=G[node][edge]['weight'])

nx.draw_random(wG, with_labels=False, edge_color="black", node_size = 5, width = 1, node_color="blue")
plt.show()
