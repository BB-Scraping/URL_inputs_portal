def write_url(new_url):
	f = open('urls.txt', 'r')
	url_set = f.read().splitlines()
	if new_url in url_set:
		return False
	else:
		f = open('urls.txt', 'a')
		f.write(new_url)
		f.write('\n')
		f.close()
		return True

if __name__ == '__main__':
	new_url = str(input())
	write_url(new_url)
