
#install anaconda-navigator in to linux https://www.anaconda.com/download and https://geekflare.com/install-anaconda-on-linux/
#open canaconda-navigator by type into terminal
anaconda-navigator
# launch jupyter notebook


# Run file: python3 fileName
git add .
git commit -m "message"
git push

# for untrack files
git rm -r --cached .
git add --all
git commit -am 'fix'
git push

Data types: 
number: whole number, floating number
string --- ordered sequence of characters (immutability)
tuples: ('a', 'b', 'c') --- ordered sequence of objects (immutability)
dictionary: {'key': 'value1'} --- key-value pairing that is unordered
list: [1, 2, 3, 4] --- ordered sequence of objects (mutable)
sets: unique value but unoredered in a list. mySet = set(), mySet.add(1)

get file path: pwd
mode: 'r', 'w', 'a', 'r+', 'w+'

Resource link
Python course: https://cglearning.udemy.com/course/complete-python-bootcamp/learn/lecture/9388536#overview
https://pyformat.info/
https://codingbat.com/python

unit test - Pylint Unittest
pylint myexample.py -r y

# set up web scraping libraries
pip install requests
pip install lxml
pip install bs4

# work with image
pip install pillow