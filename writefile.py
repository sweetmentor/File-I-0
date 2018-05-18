# f = open('newfile.txt', 'w')
# f.write("Hello World\n")
# f.close()
#-------------------------

words = ["The", "quick", "brown" "fox"]

words_as_str = "The\nquick\nbrown\nfox"


f = open('newfile.txt', 'w')
f.write(words_as_str)
f.close()
