from git import Repo
import os, os.path
from sets import Set

ANALYZED_REPO = '/Users/jonatascavalcante/Projects/EventBus'

# Graph structures declaration

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr):
        if nbr in self.connectedTo:
            self.connectedTo[nbr] += 1
        else:
            self.connectedTo[nbr] = 1

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __iter__(self):
        return iter(self.vertList.values())

# Functions definitions

def all_project_files(commits):
    all_project_files = Set([])
    
    for commit in commits:
        repo.git.checkout(commit)
        for root_folder, directory, files in os.walk(ANALYZED_REPO):
            for file in files:
                if file.endswith('.java'):
                    file_name = root_folder + '/' + file
                    all_project_files.add(file_name)

    return all_project_files


def connect_files_commited_together(commit, repo_graph):
    stats = commit.stats

    for file, file_stats in stats.files.iteritems():
        for other_file, other_file_stats in stats.files.iteritems():
            if other_file != file:
                file_vertex = repo_graph.getVertex(ANALYZED_REPO + "/" + file)
                other_file_vertex = repo_graph.getVertex(ANALYZED_REPO + "/" + other_file)
                if(file_vertex and other_file_vertex):
                    file_vertex.addNeighbor(ANALYZED_REPO + "/" + other_file)
                    other_file_vertex.addNeighbor(ANALYZED_REPO + "/" + file)
        break
# End of functions definitions

# Start of the main program flow

repo = Repo(ANALYZED_REPO)
assert not repo.bare
all_commits = list(repo.iter_commits('master'))

repo.git.checkout(all_commits[0])
repo_graph = Graph()
all_project_files = all_project_files(all_commits)

most_connected_file_connections = 0
most_connected_file_name = ''
biggest_edge_weight = 0
biggest_edge_weight_file_a = ''
biggest_edge_weight_file_b = ''
most_important_file_con = 0
most_important_file_name = ''

for project_file in all_project_files:
    repo_graph.addVertex(project_file)

for commit in all_commits:
    connect_files_commited_together(commit, repo_graph)

for vertex in repo_graph:
    if(len(vertex.connectedTo) > most_connected_file_connections):
        most_connected_file_connections = len(vertex.connectedTo)
        most_connected_file_name = vertex.id
    for connection in vertex.connectedTo:
        if(vertex.getWeight(connection) > biggest_edge_weight):
            biggest_edge_weight = vertex.getWeight(connection)
            biggest_edge_weight_file_a = vertex.id
            biggest_edge_weight_file_b = connection
            important_file_con = vertex.getWeight(connection) * len(vertex.connectedTo)
            if(important_file_con > most_important_file_con):
                most_important_file_con = important_file_con
                most_important_file_name = vertex.id

print "Question 1:"
print biggest_edge_weight_file_a + " and\n" + biggest_edge_weight_file_b + "\nwith " + str(biggest_edge_weight) + " modifications together."

print "\nQuestion 2:"
print most_connected_file_name + " with " + str(most_connected_file_connections) + " connections."

print "\nQuestion 3:"
print most_important_file_name + " with weight of " + str(most_important_file_con)
