from git import Repo
import time 

CURRENT_YEAR = 2019
ANALYZED_REPO = '/Users/jonatascavalcante/Projects/EventBus'

# Functions definitions
def count_qtd_files(commit):
	stats = commit.stats
	return stats.total['files']


def count_qtd_java_files(commit):
	stats = commit.stats
	java_files = 0
	for file in stats.files:
		if file.endswith('.java'):
			java_files += 1
	return java_files


def count_qtd_java_lines(commit):
	stats = commit.stats
	java_lines = 0
	for file, file_stats in stats.files.iteritems():
		if file.endswith('.java'):
			java_lines += file_stats['lines']
	return java_lines


def get_all_commits_by_year_interval(all_commits, begin, end):
	result_commits = []
	for commit in all_commits:
		commit_year = time.gmtime(commit.committed_date).tm_year

                if(commit_year <= end and commit_year >= begin):
                        result_commits.append(commit)
	return result_commits


def count_qtd_files_by_year(all_commits):
	first_commit = all_commits[len(all_commits) - 1]
	first_commit_year = time.gmtime(first_commit.committed_date).tm_year
	year = first_commit_year
	
	while year <= CURRENT_YEAR:
		qtd_files = 0
		commits_of_the_year = get_all_commits_by_year_interval(all_commits, year, year)
		for commit in commits_of_the_year:
			qtd_files += count_qtd_files(commit)
		print str(year) + ": " + str(qtd_files) + " file(s)"
		year += 1


def count_qtd_java_files_by_year(all_commits):
	first_commit = all_commits[len(all_commits) - 1]
	first_commit_year = time.gmtime(first_commit.committed_date).tm_year
	year = first_commit_year
	
	while year <= CURRENT_YEAR:
		qtd_java_files = 0
		commits_of_the_year = get_all_commits_by_year_interval(all_commits, year, year)
		for commit in commits_of_the_year:
			qtd_java_files += count_qtd_java_files(commit)
		print str(year) + ": " + str(qtd_java_files) + " java file(s)"
		year += 1


def count_qtd_java_lines_by_year(all_commits):
	first_commit = all_commits[len(all_commits) - 1]
	first_commit_year = time.gmtime(first_commit.committed_date).tm_year
	year = first_commit_year
	
	while year <= CURRENT_YEAR:
		qtd_java_lines = 0
		commits_of_the_year = get_all_commits_by_year_interval(all_commits, year, year)
		for commit in commits_of_the_year:
			qtd_java_lines += count_qtd_java_lines(commit)
		print str(year) + ": " + str(qtd_java_lines) + " java code line(s)"
		year += 1

# End of functions definitions

# Start of the main program flow
repo = Repo(ANALYZED_REPO)
assert not repo.bare
all_commits = list(repo.iter_commits('master'))
first_commit_index = len(all_commits) - 1

# Question 1
print "Question 1:"
print "Files in the last commit: " + str(count_qtd_files(all_commits[0]))
print "Files in the first commit: " + str(count_qtd_files(all_commits[first_commit_index]))

# Question 2
print "\nQuestion 2:"
print "Java files in the last commit: " + str(count_qtd_java_files(all_commits[0]))
print "Java files in the first commit: " + str(count_qtd_java_files(all_commits[first_commit_index]))

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

#Question 6
print "\nQuestion 6:"
count_qtd_files_by_year(all_commits)

#Question 7
print "\nQuestion 7:"
count_qtd_java_files_by_year(all_commits)

#Question 8
print "\nQuestion 8:"
count_qtd_java_lines_by_year(all_commits)
