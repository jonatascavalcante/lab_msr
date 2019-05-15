from git import Repo
import platform
import operator
import collections

TRUCK_FACTOR_PERCENT = 0.5

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

def calculate_authorship(all_project_files, files_with_auths, authors):
	for project_file_key, project_file in all_project_files.iteritems():
		totalModifications = 0
		authorships = {}
		relevant_authorships = {}
		biggestAuthorship = 0

		files_with_auths[project_file.name] = []

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
		print project_file.creator

		# Itera sobre as autorias exibindo apenas as que estao entre 0 e 1
		for authorName, authorContrib in sorted_authorships.iteritems():
			if authorContrib > 0:
				print authorName + ": " + str(authorContrib)
				files_with_auths[project_file.name].append(authorName)
				if authorName in authors:
					authors[authorName] += authorContrib
				else:
					authors[authorName] = authorContrib
		print "\n"

def calculate_truck_factor(files_with_auths, authors):
	totalFiles = len(files_with_auths)
	affectedFiles = 0
	truckFactor = 0

	# Itera pelos autores dos arquivos ordenados por contribuicao
	for authorName, authContrib in authors.iteritems():
		# Itera nos arquivos do projeto, removendo o autor corrente
		for file, authors in files_with_auths.iteritems():
			if authorName in authors:
				authors.remove(authorName)
				if len(authors) == 0:
					affectedFiles += 1
		truckFactor += 1
		if affectedFiles >= TRUCK_FACTOR_PERCENT * totalFiles:
			break

	print "Truck Factor: " + str(truckFactor)			


# Fim das definicoes e inicio do fluxo do programa

repo = Repo(ANALYZED_REPO)
all_commits = list(repo.iter_commits(reverse=True))

all_project_files = get_all_project_files(all_commits)
files_with_auths = {}
authors = {}

calculate_authorship(all_project_files, files_with_auths, authors)

sorted_authors = collections.OrderedDict( sorted(authors.items(), 
					key=operator.itemgetter(1), reverse=True) );

calculate_truck_factor(files_with_auths, sorted_authors)
