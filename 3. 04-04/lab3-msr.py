from git import Repo
import os, os.path

ANALYZED_REPO = '/Users/jonatascavalcante/Projects/EventBus'

# Functions definitions
def cta_mca(fname):
	cta = 0
	mca = 0

	with open(fname) as file:
		for line in file:
			line_complexity = 0
			line = line.replace("  ","\t")
			words = line.split('\t')
			for word in words:
				if(word == ''):
					line_complexity += 1
				else:
					break
			cta += line_complexity
			if(line_complexity > mca):
				mca = line_complexity

	cta_mca = {
		"cta": cta,
		"mca": mca
	}
	
	return cta_mca


def cra(fname):
	file_stats = cta_mca(fname)
	n_lines = file_len(fname)
	cta = file_stats["cta"]

	cra = cta / n_lines
	return cra


def cp(commit):
	repo.git.checkout(commit)

	qtd_files = sum([len(files) for root_folder, directory, files in os.walk(ANALYZED_REPO)])
	total_cra = 0

	for root_folder, directory, files in os.walk(ANALYZED_REPO):
		for file in files:
			file_name = root_folder + '/' + file
			total_cra += cra(file_name)

	return total_cra / qtd_files


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def biggest_cta_cra_mca(commit):
	repo.git.checkout(commit)

	big_cta_value = 0
	big_cta_fname = ''
	big_cra_value = 0
	big_cra_fname = ''
	big_mca_value = 0
	big_mca_fname = ''

	for root_folder, directory, files in os.walk(ANALYZED_REPO):
		for file in files:
			file_name = root_folder + '/' + file
			file_cta_mca = cta_mca(file_name)

			file_cta = file_cta_mca["cta"]
			file_mca = file_cta_mca["mca"]
			file_cra = cra(file_name)

			if(file_cta > big_cta_value):
				big_cta_value = file_cta
				big_cta_fname = file_name
			if(file_mca > big_mca_value):
				big_mca_value = file_mca
				big_mca_fname = file_name
			if(file_cra > big_cra_value):
				big_cra_value = file_cra
				big_cra_fname = file_name

	biggest_cta_cra_mca = {
		"big_cta": big_cta_fname,
		"big_cra": big_cra_fname,
		"big_mca": big_mca_fname
	}

	return biggest_cta_cra_mca


# End of functions definitions

# Start of the main program flow
repo = Repo(ANALYZED_REPO)
assert not repo.bare
all_commits = list(repo.iter_commits('master'))

repo.git.checkout(all_commits[0])

# Question 1
print "Question 1:"
biggest_cta_cra_mca = biggest_cta_cra_mca(all_commits[0])
print "Biggest CTA: " + str(biggest_cta_cra_mca["big_cta"])
print "Biggest CRA: " + str(biggest_cta_cra_mca["big_cra"])
print "Biggest MCA: " + str(biggest_cta_cra_mca["big_mca"])

# # Question 2
# print "\nQuestion 2:"

# Question 3
print "\nQuestion 3:"
print "CP of the last commit: " + str(cp(all_commits[0]))

# # Question 4
# print "\nQuestion 4:"
# print "CP of the last commit of one year ago: " + str(cp(all_commits[0]))

# Question 5
print "\nQuestion 5:"
for commit in all_commits:
	print commit.hexsha + ": CP = " + str(cp(commit))
