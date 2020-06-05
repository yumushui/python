#!/usr/bin/env python
# -*- conding:utf-8 -*-

''' three python inter tool '''
print("1 make a small download server")
print("in pyton2")
print("python -m SimpleHTTPServer")
print("in python3")
print("python -m http.server")
print("")

print("2 string convert to JSON")
print(
    ''' echo '{"job": "devoloper", "name": "lmx", "sex": "male" }' | python -m json.tool ''')
print(''' echo '{ "address": {"province": "zhejiang", "city": "shanghai"}, "name": "feixiang.zhao", "sex": "male" }' | python -m json.tool ''')

print("3 check the thire package")
print("import {package_name}")
print("import paramiko")
print("python -c 'import paramiko'")


''' the usage of pip '''
print(" 1 install pip")
print("pip install -u pip")
print("")

print("2 the pip sub commands")
print("find package :   pip search flask")
print("install package:  pip install flask==0.8")
print("uninstall package:  pip uninstall Werkzeug")
print("show package : pip show flask")
print("check pip:  pip check flask")
print("show installed list : pip list")
print("load package list : pip freeze > requirements.txt")
print("install from requie file :  pip install requirements.txt")
print("command full:  pip completion --bash >> ~/.profile")
print("source ~/.profile")
print("")

print("3 pip install speed quikly")
print("use the prpi resource in china, such as douban/aliyun")
print("pip install -i https://pypi.douban.com/simpe/flask")
print(''' in linux OS , you can cate a file  to save source
       vim ~/.pip/pip.confg
       
       [global]
       index-url = https://pypi.douban.com/simple/
       ''')
print("")
print(''' You can also download the resource first ,then install package
       # download the package
       pip install --download='pwd' -r requirements.txt

       # local install package
       pip install --no-index -f file://'pwd' -r requirements.txt
       
       # this mothed not only download the need package ,but also download the re exsite package
       pip install --download='pwd' flask
       ls
       ''')
print("")


'''The python code IDE  '''
print("1 ptyhon IDE : vim")
print('''excute the python one command ''')
'''
""""""""""""""""
" Quickly Run
"""""""""""""""
map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
    exec "w"
    if &filetype == 'c'
        exec "!g++ % -o %<"
        exec "!time ./%<"
    elseif &filetype == 'cpp'
        exec "!g++ % -o %<"
        exec "!time ./%<"
    elseif &filetype == 'java'
        exec "!javac %"
        exec "!time java %<"
    elseif &filetype == 'sh'
        :!time bash % 
    elseif &filetype == 'python'
        exec "!time python2.7 %"
    elseif &filetype == 'html'
        exec "!firefox % &"
    elseif &filetype == 'go'
        exec "!go build %<"
        exec "!time go run %"
    elseif &filetype == 'mkd'
        exec "!~/.vim/markdown.pl % > %.html &"
        exec "!firefox %.html &"
    endif
endfunc
'''
print("vim plugin : snipmate")
print("vim plugin : Syntastic")
print("jedi-vim")
print("")
print("python IDE : PyCharm")
print("")

''' Python inter active progame '''
print("1 python shell")
print("python")
print("2 ipython")
print("pip install")
print("ipython")
print("ipython is a better inert active IDE ")
print("ipython get the help info more easy")
print(''' 
       import os
       ?os.path.is*

       import json
       import os
       os.path.isfile?
       json.dump?

       import json
       d = dict(a=1, b=2, c=3)
       json.dump?
       json.dumps(d)
       
       # anoth get help info
       import json
       %pdef json
       %pdef json.dump
       %pfile json.dump
       %pdoc json.dump
       %pinfo json

       # the % head function is magic function
       %lsmagic
       %save?
       1 the control code function: %run, %edit, %save
       2 the control ipython function : %colors, %xmode 
       3 other magic function: %reset, %timeit, %load

       # as DBA ,you should execute the sql :
       show slave status;
       show master status;
       show variables like '%innodb%buffer%';
       show status like '%select%';
       show global innodb_buffer_pool_dump_pct = 30
       GRANT ALL PRIVILEGES on *.* to 'feixiang'@'localhost' WITH GRANT OPTION;

       vim connect.py
       %load connect.py
       
       ipython save the command history
       
       ipthon can execute the OS command:
       ! wc -l /tmp/app.log
       data = !df
       data
       data[1].split()[4]




       ''')

print("the jupyter : ipython Notebook")
print(''' 
      pip install jupyter
       jupyter notebook --no-browser --ip=0.0.0.0
       pip install matplotlib
       
       ''')

''' the python Debugger '''
print("The python Debugger : gdb , ipdb")
print('''
    # pdb
    python -m pdb test_pdb.py

    #/usr/bin/env python
    from __future__ import print_function
    imprt pdb

    def sum_nums(n):
       s=0
       for i in range(n):
            pdb.set_trace()
            s += i
            print (s)

    if __name__ == '__main__':
       sum_nums(5)
      ''')

print(''' 
    # ipdb
    the ipdb to pdb , means the ipython to python
    pip install ipdb



''')

''' the python code style check '''
print("The python code style check tool")
print(" PEP8 , pycodestyle , autopep8 ")
print('''
    PEP 8 style :
    import os 
    import sys

    not as :
    import sys, os

    pip install pep8
    pip install pycodestyle

    usage:
    pycodestyle --first  optparse.py
    pep8 optparse.py

    pycodestyle --show-source  --show-pep8 testsuite/E40.py

    # the autopep8  format the script
    pip install autopep8
    autopep8 --in-place optparse.py

    a test python file:

vim hello.py

import os, sys
def main():
    print [item for item in os.listdir('.') if item.endswith('.py') ];
    print sys.version

if __name__ == '__main__'
    main()

    # check but not merge 
    pycodestyle hello.py
    autopep8 hello.py

    # check and merge the modify
    autopep8 --in-place hello.py


       ''')
