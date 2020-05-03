import sys, os
from itertools import islice

def begin_parse():
	location = os.getcwd()
	dirs = ['/cpp', '/java', '/python']
	for dir in dirs:
		if not os.path.isfile(location + dir):
			try:
				os.mkdir(location + dir)
			except OSError:
				print("The directory %s already exists!" % dir)
			else:
				print("Successfully created the directory %s " % dir)

	everything = []
	with open(sys.argv[1], 'r') as data_file:
		for one_line in data_file:
			everything.append(one_line)
	return location, everything


def check_lang(the_list):
	for line in the_list:
		cpp_ind = line.find('lang-cpp')
		java_ind = line.find('lang-java')
		python_ind = line.find('lang-python')
		if cpp_ind != -1:
			replace_and_save(line, ".cpp")
		if java_ind != -1:
			replace_and_save(line, ".java")
		if python_ind != -1:
			replace_and_save(line, ".py")


def replace_and_save(line, ext):
	eight_zeros = '00000000'
	if (line[0] == '"'):
		line = line[1:]
	if (line[len(line) - 2] == '"'):
		line = line[:len(line) - 2]
	line = line.replace('&#xD;&#xA;', '\n')
	start_tag_ind = 0
	end_tag_ind = -1

	while start_tag_ind != -1:
		start_tag_ind = line.find('<!--')
		end_tag_ind = line.find('-->')
		remove_tag = line[start_tag_ind:end_tag_ind + 3]
		line = line.replace(remove_tag, '')

	if ext == ".cpp":
		file_name = eight_zeros[0:8-len(str(cpp_count))]
		with open(path + "/cpp/" + file_name + str(cpp_count) + ext, 'w') as new_cpp_snippet:
			new_cpp_snippet.write(line)
		increment_cpp()
	elif ext == ".java":
		file_name = eight_zeros[0:8-len(str(java_count))]
		with open(path + "/java/" + file_name + str(java_count) + ext, 'w') as new_java_snippet:
			new_java_snippet.write(line)
		increment_java()
	elif ext == ".py":
		file_name = eight_zeros[0:8-len(str(python_count))]
		with open(path + "/python/" + file_name + str(python_count) + ext, 'w') as new_python_snippet:
			new_python_snippet.write(line)
		increment_python()


def increment_cpp():
	global cpp_count
	cpp_count += 1


def increment_java():
	global java_count
	java_count += 1


def increment_python():
	global python_count
	python_count += 1


if __name__ == '__main__':
	cpp_count = 0
	java_count = 0
	python_count = 0
	path, all_lines = begin_parse()
	check_lang(all_lines)

