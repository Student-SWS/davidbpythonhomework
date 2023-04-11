######## test2a.py:  read file3a.txt ########

""" test2a.py:  open and read a file """

fh = open('dir3a/file3a.txt')                       # add relative filepath here to open file3a.txt

print(fh.read())                                    # this is file3a.txt



######## test1.py:  read file4.txt ########

""" test1.py:  open and read a file """

fh = open('dir2a/dir3a/dir4/file4.txt')             # add relative filepath here to open file4.txt

print(fh.read())                                    # this is file4.txt



######## test4.py:  read file3a.txt ########

""" test4.py:  open and read a file """

fh = open('../file3a.txt')                          # add relative filepath here to open file3a.txt

print(fh.read())                                    # this is file3a.txt



######## test3a.py:  read file1.txt ########

""" test3a.py:  open and read a file """

fh = open('../../file1.txt')                        # add relative filepath here to open file1.txt

print(fh.read())                                    # this is file1.txt



######## test2b.py:  read file2a.txt ########

""" test2b.py:  open and read a file """

fh = open('../dir2a/file2a.txt')                    # add relative filepath here to open file2a.txt
                                                    # hint:  you must go "down, then up" within the single filepath

print(fh.read())                                    # this is file2a.txt