from git import Repo
import time
import os, os.path
from sets import Set

CURRENT_YEAR = 2019
ANALYZED_REPO = '/Users/jonatascavalcante/Projects/EventBus'

# Functions definitions
def count_qtd_files(commit):
	repo.git.checkout(commit)
	qtd_files = sum([len(files) for root_folder, directory, files in os.walk(ANALYZED_REPO)])
	return qtd_files


def count_qtd_java_files(commit):
	repo.git.checkout(commit)
	java_files = 0

	for root_folder, directory, files in os.walk(ANALYZED_REPO):
		for file in files:
			if file.endswith('.java'):
				java_files += 1
	
	return java_files


def count_qtd_java_lines(commit):
	repo.git.checkout(commit)
	java_lines = 0
	
	for root_folder, directory, files in os.walk(ANALYZED_REPO):
		for file in files:
			if file.endswith('.java'):
				file_name = root_folder + '/' + file
				java_lines += file_len(file_name)
				
	return java_lines


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_all_commits_by_year_interval(all_commits, begin, end):
	result_commits = []
	
	for commit in all_commits:
		commit_year = time.gmtime(commit.committed_date).tm_year

                if(commit_year <= end and commit_year >= begin):
                        result_commits.append(commit)
	
	return result_commits


def qtd_files_by_year(commits_of_the_year):
	files_of_year = Set([])
	
	for commit in commits_of_the_year:
		repo.git.checkout(commit)
		for root_folder, directory, files in os.walk(ANALYZED_REPO):
			for file in files:
				file_name = root_folder + '/' + file
				files_of_year.add(file_name)

	return len(files_of_year)


def qtd_java_files_by_year(commits_of_the_year):
	java_files_of_year = Set([])
	
	for commit in commits_of_the_year:
		repo.git.checkout(commit)
		for root_folder, directory, files in os.walk(ANALYZED_REPO):
			for file in files:
				if file.endswith('.java'):
					file_name = root_folder + '/' + file
					java_files_of_year.add(file_name)

	return len(java_files_of_year)


def qtd_java_lines_by_year(commits_of_the_year):
	qtd_java_lines = 0
	
	for commit in commits_of_the_year:
		repo.git.checkout(commit)
		for root_folder, directory, files in os.walk(ANALYZED_REPO):
			for file in files:
				if file.endswith('.java'):
					file_name = root_folder + '/' + file
					qtd_java_lines += file_len(file_name)

	return qtd_java_lines


def count_qtd_files_by_year(all_commits):
	first_commit = all_commits[- 1]
	first_commit_year = time.gmtime(first_commit.committed_date).tm_year
	year = first_commit_year
	
	while year <= CURRENT_YEAR:
		qtd_files = 0
		commits_of_the_year = get_all_commits_by_year_interval(all_commits, year, year)		
		print str(year) + ": " + str(qtd_files_by_year(commits_of_the_year)) + " file(s)"
		year += 1


def count_qtd_java_files_by_year(all_commits):
	first_commit = all_commits[- 1]
	first_commit_year = time.gmtime(first_commit.committed_date).tm_year
	year = first_commit_year
	
	while year <= CURRENT_YEAR:
		qtd_java_files = 0
		commits_of_the_year = get_all_commits_by_year_interval(all_commits, year, year)
		print str(year) + ": " + str(qtd_java_files_by_year(commits_of_the_year)) + " java file(s)"
		year += 1


def count_qtd_java_lines_by_year(all_commits):
	first_commit = all_commits[- 1]
	first_commit_year = time.gmtime(first_commit.committed_date).tm_year
	year = first_commit_year
	
	while year <= CURRENT_YEAR:
		qtd_java_lines = 0
		commits_of_the_year = get_all_commits_by_year_interval(all_commits, year, year)
		print str(year) + ": " + str(qtd_java_lines_by_year(commits_of_the_year)) + " java code line(s)"
		year += 1

# End of functions definitions

# Start of the main program flow
repo = Repo(ANALYZED_REPO)
assert not repo.bare
all_commits = list(repo.iter_commits('master'))

repo.git.checkout(all_commits[0])

# Question 1
print "Question 1:"
print "Files in the last commit: " + str(count_qtd_files(all_commits[0]))
print "Files in the first commit: " + str(count_qtd_files(all_commits[-1]))

# Question 2
print "\nQuestion 2:"
print "Java files in the last commit: " + str(count_qtd_java_files(all_commits[0]))
print "Java files in the first commit: " + str(count_qtd_java_files(all_commits[-1]))

# Question 3
print "\nQuestion 3:"
for commit in all_commits:
	print commit.hexsha + ": " + str(count_qtd_files(commit)) + " file(s)"

# Question 4
print "\nQuestion 4:"
for commit in all_commits:
	print commit.hexsha + ": " + str(count_qtd_java_files(commit)) + " java file(s)"

# Question 5
print "\nQuestion 5:"
for commit in all_commits:
	print commit.hexsha + ": " + str(count_qtd_java_lines(commit)) + " java code line(s)"

# Question 6
print "\nQuestion 6:"
count_qtd_files_by_year(all_commits)

# Question 7
print "\nQuestion 7:"
count_qtd_java_files_by_year(all_commits)

# Question 8
print "\nQuestion 8:"
count_qtd_java_lines_by_year(all_commits)
