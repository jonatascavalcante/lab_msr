from git import Repo
import platform
import operator
import collections

if platform.system() == "Windows":
	ANALYZED_REPO = 'C:\\Users\\samue\\EventBus'
else:
	ANALYZED_REPO = '/Users/jonatascavalcante/Projects/EventBus'

# Definicao de classes
class File:
	def __init__(self, name, creator):
		self.name = name
		self.creator = creator
		self.authors = {}

	def add_author(self, author):
		if author in self.authors:
			self.authors[author] += 1
		else:
			self.authors[author] = 1

# Definicao das funcoes
def get_all_project_files(commits):
	files = {}

	for commit in commits:
		for file in commit.diff():
			if ".java" in file.a_path:
				if file.a_path in files:
					current_file = files[file.a_path]
					current_file.add_author(commit.author.name)
				else:
					current_file = File(file.a_path, commit.author.name)
					files[file.a_path] = current_file
		
	return files

def calculate_authorship(all_project_files):
	for project_file_key, project_file in all_project_files.iteritems():
		totalModifications = 0
		authorships = {}
		biggestAuthorship = 0

		# Calcula o total de modificacoes realizados no arquivo
		for authorName, authorContrib in project_file.authors.iteritems():
			totalModifications += authorContrib

		# Calcula a autoria de cada desenvolvedor que alterou o arquivo
		for authorName, authorContrib in project_file.authors.iteritems():
			authorship = 0.5 * authorContrib - 0.1 * (totalModifications - authorContrib)
			if authorName == project_file.creator:
				authorship += 1
			if authorship > biggestAuthorship:
				biggestAuthorship = authorship
			authorships[authorName] = authorship

		# Normaliza o valor da autoria dividindo pelo maior valor de modificacaoes
		for authorName, authorContrib in authorships.iteritems():
			authorships[authorName] = authorContrib/biggestAuthorship

		# Ordena o dicionario com as autorias em ordem decrescente
		sorted_authorships = collections.OrderedDict( sorted(authorships.items(), 
					key=operator.itemgetter(1), reverse=True) );
		
		print project_file.name

		# Itera sobre as autorias exibindo apenas as que estao entre 0 e 1
		for authorName, authorContrib in sorted_authorships.iteritems():
			if authorContrib > 0:
				print authorName + ": " + str(authorContrib)
		print "\n"				
# Fim das definicoes e inicio do fluxo do programa

repo = Repo(ANALYZED_REPO)
all_commits = list(repo.iter_commits(reverse=True))

all_project_files = get_all_project_files(all_commits)
calculate_authorship(all_project_files)
