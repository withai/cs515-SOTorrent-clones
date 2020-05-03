import sys, os, argparse
from itertools import islice

def begin_parse(file_arg, create_dirs = False):
	location = os.getcwd()
	if create_dirs:
		dirs = ['/cpp', '/java', '/python']
		for dir in dirs:
			if not os.path.isfile(location + dir):
				try:
					os.mkdir(location + dir)
				except OSError:
					print('The directory %s already exists!' % dir)
				else:
					print('Successfully created the directory %s ' % dir)

	everything = []
	with open(file_arg, 'r') as data_file:
		for one_line in data_file:
			everything.append(one_line)
	return location, everything


def check_lang(the_list, verbose = False):
	for line in the_list:
		cpp_ind = line.find('lang-cpp')
		java_ind = line.find('lang-java')
		python_ind = line.find('lang-python')
		if cpp_ind != -1:
			replace_and_save(line, '.cpp', verbose)
		if java_ind != -1:
			replace_and_save(line, '.java', verbose)
		if python_ind != -1:
			replace_and_save(line, '.py', verbose)


def replace_and_save(line, ext, verbose):
	eight_zeros = '00000000'
	if (line[0] == '"'):
		line = line[1:]
	if (line[len(line) - 2] == '"'):
		line = line[:len(line) - 2]
	line = line.replace('&#xD;&#xA;', '\n')

	while True:
		start_tag_ind = line.find('<!-- ')
		if start_tag_ind == -1:
			break
		end_tag_ind = line.find(' -->')
		if end_tag_ind == -1:
			break
		if start_tag_ind > end_tag_ind:
			break
		remove_tag = line[start_tag_ind:end_tag_ind + 4]
		line = line.replace(remove_tag, '')

	if ext == '.cpp':
		file_name = eight_zeros[0:8-len(str(cpp_count))]
		with open(path + '/cpp/' + file_name + str(cpp_count) + ext, 'w') as new_cpp_snippet:
			new_cpp_snippet.write(line)
		if verbose:
			print(file_name + str(cpp_count) + ext)
		increment_cpp()
	elif ext == '.java':
		file_name = eight_zeros[0:8-len(str(java_count))]
		with open(path + '/java/' + file_name + str(java_count) + ext, 'w') as new_java_snippet:
			new_java_snippet.write(line)
		if verbose:
			print(file_name + str(java_count) + ext)
		increment_java()
	elif ext == '.py':
		file_name = eight_zeros[0:8-len(str(python_count))]
		with open(path + '/python/' + file_name + str(python_count) + ext, 'w') as new_python_snippet:
			new_python_snippet.write(line)
		if verbose:
			print(file_name + str(python_count) + ext)
		increment_python()


def increment_cpp(num = 1):
	global cpp_count
	cpp_count += num


def increment_java(num = 1):
	global java_count
	java_count += num


def increment_python(num = 1):
	global python_count
	python_count += num


def get_file_count(change = True):
	_, _, cur_cpp = next(os.walk(path + '/cpp'))
	_, _, cur_java = next(os.walk(path + '/java'))
	_, _, cur_python = next(os.walk(path + '/python'))
	if change:
		increment_cpp(len(cur_cpp))
		increment_java(len(cur_java))
		increment_python(len(cur_python))
	return len(cur_cpp), len(cur_java), len(cur_python)


if __name__ == '__main__':
	cpp_count = 0
	java_count = 0
	python_count = 0

	parse_flag = False
	if len(sys.argv) < 2:
		print('You must specify the file to parse!')
		sys.exit()
	else:
		for i in range(len(sys.argv)):
			if sys.argv[i] == '-f':
				parse_flag = True
		if not parse_flag:
			print('You must specify the file to parse!')
			sys.exit()

	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--create_dir', required = False, action = 'store_true')
	parser.add_argument('-c', '--file_count', required = False, action = 'store_true')
	parser.add_argument('-f', '--parse_file', required = True)
	parser.add_argument('-v', '--verbose', required = False, action = 'store_true')
	args = parser.parse_args()
	file = args.parse_file

	if args.create_dir == True:
		path, all_lines = begin_parse(file, True)
	else:
		path, all_lines = begin_parse(file)

	get_file_count()
	if args.verbose == True:
		check_lang(all_lines, True)
	else:
		check_lang(all_lines)

	if args.file_count == True:
		c, j, p = get_file_count(False)
		print('C++:    %s files' % c)
		print('Java:   %s files' % j)
		print('Python: %s files' % p)

