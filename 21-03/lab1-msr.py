from git import Repo
import time 
import operator 

# Functions definitions

def count_all_commits(all_commits):
	print "Total of commits: " + str(len(all_commits)) + "\n"

def count_commits_by_year(all_commits):
	commits_2019 = 0
	commits_2018 = 0
	commits_2017 = 0

	for commit in all_commits:
		commit_year = time.gmtime(commit.committed_date).tm_year
		
		if(commit_year == 2019):
			commits_2019 += 1
		if(commit_year == 2018):
			commits_2018 += 1
		if(commit_year == 2017):
			commits_2017 += 1

	print "Total of commits in 2019: " + str(commits_2019)
	print "Total of commits in 2018: " + str(commits_2018)
	print "Total of commits in 2017: " + str(commits_2017) + "\n"

def count_commits_by_message(all_commits):
	commits_with_features = 0
	commits_with_fixes = 0
	
	for commit in all_commits:
		if commit.message.find("feature") >= 0:
			commits_with_features += 1
		if commit.message.find("fix") >= 0:
			commits_with_fixes+=1

	print "Total of commits with features: " + str(commits_with_features)
	print "Total of commits with fixes: " + str(commits_with_fixes) + "\n"

def list_five_most_modified_files(all_commits):
	modified_files = {}

	for commit in all_commits:
		for diff in commit.diff().iter_change_type('M'):
			if ".java" in diff.a_path:
				if diff.a_path not in modified_files: 
					modified_files[diff.a_path] = 1  
				else:
					modified_files[diff.a_path] += 1

	sorted_modified_files = sorted(modified_files.items(), key=operator.itemgetter(1), reverse = True)

	for modified_file in sorted_modified_files[:5]:
		print modified_file
	print "\n"

def get_all_commits_by_year_interval(all_commits,begin,end):
	result_commits = []
	for commit in all_commits:
		commit_year = time.gmtime(commit.committed_date).tm_year

                if(commit_year <= end and commit_year >=begin):
                        result_commits.append(commit)

	return result_commits


#def list_most_active_devs(all_commits):
#	headcommit.author.name

# End of functions definitions

# Start of the main program flow
repo = Repo('/Users/jonatascavalcante/Projects/EventBus')
assert not repo.bare
all_commits = list(repo.iter_commits('master'))

# Question 1
print "Question 1"
count_all_commits(all_commits)

# Question 2
print "Question 2"
count_commits_by_year(all_commits)

# # Question 3
print "Question 3"
count_commits_by_message(all_commits)

# # Question 4
print "Question 4"
list_five_most_modified_files(all_commits)

# # Question 5
print "Question 5"
list_five_most_modified_files(get_all_commits_by_year_interval(all_commits=all_commits, begin=2018, end=2019))

# # Question 6
print "Question 6:"
list_five_most_modified_files(get_all_commits_by_year_interval(all_commits=all_commits, begin=2017, end=2017))

# # Question 7





