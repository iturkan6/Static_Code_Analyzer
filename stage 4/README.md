<h1>Stage 4/5: Check names according to PEP8</h1>
<h5>Description</h5>
<p>As many coders say, naming is one of the hardest things in programming. Good naming makes your code more readable and uniform. Names should also follow style guides. In Python, the basic requirement is using snake_case for function names and CamelCase for class names. Also, there should be only one space between the construction name and the object name. Checking these rules is the next feature that we need to implement.</p>
<p>Check out the Python&nbsp;<a href="https://docs.python.org/3/howto/regex.html" rel="noopener noreferrer nofollow" target="_blank">tutorial about regular expressions<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a>: they will help you implement the checks.</p>
<h5>Objectives</h5>
<p>In this stage, we need to add three new checks to the program:</p>
<ul>
    <li>
        <p>[S007]&nbsp;Too many spaces after construction_name (def or class);</p>
    </li>
    <li>
        <p>[S008]&nbsp;Class name class_name should be written in CamelCase;</p>
    </li>
    <li>
        <p>[S009]&nbsp;Function name function_name should be written in snake_case.</p>
    </li>
</ul>
<p>Note that:</p>
<ol>
    <li>
        <p>Functions names may start or end with underscores (__fun,&nbsp;__init__).</p>
    </li>
    <li>
        <p>To simplify the task, we will assume that classes are always written as in the following examples:</p>
        <pre># a simple class
class MyClass:
    pass

# a class based on inheritance
class MyClass(AnotherClass):
    pass</pre>
        <p>In reality, it&apos;s possible to declare a class this way:</p>
        <pre>class \
        S:
    pass</pre>
        <p>However, since it is not a common way to declare classes, you can ignore it.</p>
    </li>
    <li>
        <p>Another assumption is that functions are always declared like this:</p>
        <pre>def do_magic():
    pass</pre>
    </li>
</ol>
<p>As before:</p>
<ul>
    <li>
        <p>The program obtains the path to the file or directory via command-line arguments:</p>
    </li>
</ul>
<pre>&gt; python code_analyzer.py directory-or-file</pre>
<ul>
    <li>
        <p>All the previously implemented checks should continue to work properly.</p>
    </li>
</ul>
<h5>Examples</h5>
<p>Here is an input example:</p>
<pre>class  Person:
    pass

class user:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def _print1():
        print(&apos;q&apos;)

    @staticmethod
    def Print2():
        print(&apos;q&apos;)</pre>
<p>The expected output for this code is:</p>
<pre>/path/to/file/script.py: Line 1: S007 Too many spaces after &apos;class&apos;
/path/to/file/script.py: Line 4: S008 Class name &apos;user&apos; should use CamelCase
/path/to/file/script.py: Line 15: S009 Function name &apos;Print2&apos; should use snake_case</pre>
<p><br></p>