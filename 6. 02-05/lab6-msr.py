from git import Repo
import platform
import networkx as nx
import matplotlib.pyplot as plt

if platform.system() == "Windows":
	ANALYZED_REPO = 'C:\\Users\\samue\\EventBus'
else:
	ANALYZED_REPO = '/Users/jonatascavalcante/Projects/EventBus'
	
class Author:
	def __init__(self,name):
		self.name=name
		self.contrib = 0

class File:
	def __init__(self,name):
		self.name=name
		self.authors = []

def get_all_project_files(commits):
	files = {}
	

	for commit in commits:
		for file in commit.diff().iter_change_type('A'):
			files[file.a_path]={'authors': [commit.author.name]}
		
		for file in commit.diff().iter_change_type('M'):
			files[file.a_path]['authors'].append(commit.author.name)
		
	return files

repo = Repo(ANALYZED_REPO)
all_commits = list(repo.iter_commits(reverse=True))

all_project_files = get_all_project_files(all_commits)


print(all_project_files)






