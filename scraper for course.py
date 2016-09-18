#crawler for CMU 15-388/688, Fall 2016
# Liu L.
# Sep 15, 2016

#================================================================

import re, requests, urllib, os, tarfile
from bs4 import BeautifulSoup

course_url = 'http://www.datasciencecourse.org'
content = requests.get(course_url).content
soup = BeautifulSoup(content, 'html.parser')
tag_a = soup.findAll('a', class_="")
downloads = [tag['href'] for tag in tag_a if re.search(r'(.pdf|.tar)$', tag['href'])]

full_links = []
for d in downloads:
    if not d.startswith('http'):
        full_links.append('/'.join([course_url, d]))
    else:
        full_links.append(d)

target_dir = '/Users/Liu/Dropbox/courses/CMU 15-388:688 Practical Data Science'
exsited_downloads = os.listdir(target_dir)
os.chdir(target_dir)

for l in full_links:
    if l.endswith('.pdf'):
        file_name = re.search(r'/([^/]*.pdf)$', l).group(1)
        if file_name not in exsited_downloads:
            urllib.urlretrieve(l, file_name)
    elif l.endswith('.tar'):
        if l.endswith('handout.tar'):
            num = re.search(r'(\d)/handout.tar$', l).group(1)
            file_name = ''.join(['handout', num])
            tar_fname = file_name + '.tar'
            if (file_name not in exsited_downloads) & (tar_fname not in exsited_downloads):
                urllib.urlretrieve(l, tar_fname)
                os.mkdir(file_name)
                tar = tarfile.open(tar_fname, "r:")
                tar.extractall(file_name)
                tar.close()
                os.remove(tar_fname)
        else:
            file_name = re.search(r'/([^/]*).tar', l).group(1)
            tar_fname = file_name + '.tar'
            if (file_name not in exsited_downloads) & (tar_fname not in exsited_downloads):
                urllib.urlretrieve(l, tar_fname)
                os.mkdir(file_name)
                tar = tarfile.open(tar_fname, "r:")
                tar.extractall(file_name)
                tar.close()
                os.remove(tar_fname)