Todo list CLI using python - Created by Aryan Garg, 12/17/2020

# Extra Features
1) There's an extra feature in the program which can be invoked by 
passing in the arguement: reportVerbose.

reportVerbose -
It lists all the documents along with the standard pending and 
completed counter.

2) -h flag also works the same way as passing help as an arguement.

3) The initial Makefile is there to efficiently set-up the testing 
environment and see all the test cases pass :)

# General Note
The functions were written keeping in mind that other functions 
derive efficient use out of them instead of increasing redundancies.

Hope you achieve increased productivity with this tool :)

# Issues that might occur
1) Is your python interpreter in the same path as in the source file?
Try locating it by following these steps:
 a) $which python3
 b) Copy this path and replace it in the source code's shebang

2) Issues related to execution permissions can be resolved by simply:
Running:
chmod +x todo.py

# Any feedback is highly appreciated!
