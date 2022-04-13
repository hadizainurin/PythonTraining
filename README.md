# PythonTraining 

**Phyton** is a high-level interpreted programming language that is famous for its nearly readable code. From TIOBE Index for March 2022, Python was rated The most popular programming language in the world follow by C and Java. The reason for this is because Phyton is easy to learn and there is numerous tutorial available online that teach Phyton. It is also practical for serious project. <br>
Watch the [tutorial video](docs/TUTORIAL.md) for a quick rundown on using it.

**Created by**: Guido Van Rossum (1991)

## Example

' def spam():
    eggs = 10
    return'

## Application

1. Server-side Application
    1. Web Apps (django)
    2. Mobile Application (kivy)
2. Big Data Analysis
3. Machine Learning

## Why learn Phyton?

1. Phyton emphasises on **Readability**. In its Zen of Phyton, by Tim Peters which you can import by importing 'import this'. <br> The three core priciples are that :-
    1. Beautiful is better than ugly
    2. Explicit is better than implicit
    3. Simple is better than complex

2. Avoids **MAGIC** that causes **AMIBIGUITY**. For example, in Jupyter notebook, you can run individual cell or block of code which allows you to see hows your code is running

## Advantage

Take a look at this piece of code 'hello = 'hi mom''
Phyton is strongly type which means value won't change in unexpected way but dynamic so type annotation are not required (Variable annotation such as int, char, float, etc.) <br>
This syntax is highly efficient allowing you to declare multiple variables on a single line such as 'hello, hola = 'hi mom', 'hola mama''

**Phyton** allowed you to structure your data by tuple, list and dictionary
'my_tuple = ('a', 'b')

'my_list = [1,2,3]'

'my_dictg = {
    'key' : 'value'
}'

**Note:** List is mutable while Tuple is immutable. This means you can change the value in list but not tuple.

## Convention

1. Phyton uses indentation to terminate or determine the scope of line of code. (this is known as snake case)

2. A function is defined with the 'def' keyword then indext the next line 
example: 
'def have_fun():
    for i in range(5):
        print(i)
'
This differt from other langauges that used '{}' or ';' found in many other languages

3. It is recommended to not semicolons you code, althought your code will just work fine.

## Paradigm

Everything in Phyton is an object, you can see this by using 'print(type())' command which shows the builtin object that Phyton is using. <br>
However, Phyton is not limited to Object-Oriented paradigm (OOP) as its can also applied **functional programming** and **procedural programming** <br>
patterns with things like anonymous functions using lambda

## Third-party Library/Application

1. PyQt
2. Django
3. NumPy
4. Pandas
5. Tensorflow
6. OpenCV
7. Pyinstaller
8. auto-py-to-exe
9. Kivy

## Reference

[Phyton Documentation](https://docs.python.org/3/)

## Step-by-Step process to push to this repository

1. 'git add .' (Add all files but you can also add specify file)
2. 'git status' (optional)
3. 'git commit -m "Comment changes"
4. git remote -v (optional) 
5. git push -u origin master (origin is your remote link and branch is normally at master) (optionally you can create a new branch using 'git checkout -b new_branch')

NOTED: If you trying to snych directory, used git pull -u origin master
