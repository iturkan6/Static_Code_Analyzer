<h1>Stage 5/5: Analyze arguments and variables</h1>
<h5>Theory</h5>
<p>In this stage, it is preferable to make use of the&nbsp;ast&nbsp;module (<a href="https://docs.python.org/3/library/ast.html" rel="noopener noreferrer nofollow" target="_blank">Abstract Syntactic Tree<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a>). If you feel that you need to know more about it, here are two tutorials that can help you work with it:</p>
<ul>
    <li><a href="https://www.mattlayman.com/blog/2018/decipher-python-ast/" rel="noopener noreferrer nofollow" target="_blank">A short tutorial: How to use AST to understand code<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a></li>
    <li><a href="https://greentreesnakes.readthedocs.io/en/latest/" rel="noopener noreferrer nofollow" target="_blank">A long tutorial that complements the standard documentation<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a></li>
</ul>
<p>ast&nbsp;module also contains many classes that represent different elements of Python&apos;s syntax. For example, the class&nbsp;FunctionDef&nbsp;is a node of the tree representing a definition of some function in the code, the class&nbsp;arguments&nbsp;represents function&apos;s arguments, the class&nbsp;Assign&nbsp;represents an expression where a value gets assigned to some variable. You can use all these (and other) classes to find places of the code (names of the variables and so on) that you want to check for correctness:</p>
<pre>for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        function_name = node.name
        # check whether the function&apos;s name is written in camel_case
        pass</pre>
<p>Don&apos;t be shy to check some other classes and functions of this module to feel confident while using it.</p>
<h5>Description</h5>
<p>In this final stage, you need to improve your program to check that all the names of function arguments as well as local variables meet the requirements of PEP8. The program must not force the names of variables outside of functions (for example, in modules or classes). The most convenient way to do this is to use the Abstract Syntactic Tree (AST) from the&nbsp;ast&nbsp;module.</p>
<p>Also, your program must check that the given code does not use mutable values (lists, dictionaries, and sets) as default arguments to avoid errors in the program.</p>
<h5>Objectives</h5>
<p>You need to add three new checks to your analyzer:</p>
<ul>
    <li>
        <p>[S010]&nbsp;Argument name arg_name should be written in snake_case;</p>
    </li>
    <li>
        <p>[S011]&nbsp;Variable var_name should be written in snake_case;</p>
    </li>
    <li>
        <p>[S012]&nbsp;The default argument value is mutable.</p>
    </li>
</ul>
<p>Please note that:</p>
<ol>
    <li>
        <p>Names of functions, as well as names of variables in the body of a function should be written in snake_case. However, the error message for an invalid function name should be output only when the function is defined. The error message for an invalid variable name should be output only when this variable is assigned a value, not when this variable is used further in the code.</p>
    </li>
    <li>
        <p>To simplify the task, you only need to check whether the mutable value is directly assigned to an argument:</p>
        <pre>def fun1(test=[]):  # default argument value is mutable
    pass


def fun2(test=get_value()):  # you can skip this case to simplify the problem
    pass</pre>
    </li>
    <li>
        <p>If a function contains several mutable arguments, the message should be output only once for this function.</p>
    </li>
    <li>
        <p>Variable and argument names are assumed to be valid if they are written in snake_case. Initial underscores (_) are also acceptable.</p>
    </li>
</ol>
<p>As before:</p>
<ul>
    <li>
        <p>You can use other messages, but the check codes must be exactly as given above.</p>
    </li>
    <li>
        <p>All the previously implemented checks should continue to work correctly, and the program should be able to read from one or more files.</p>
    </li>
</ul>
<h5>Examples</h5>
<p>Here is an input example:</p>
<pre>CONSTANT = 10
names = [&apos;John&apos;, &apos;Lora&apos;, &apos;Paul&apos;]


def fun1(S=5, test=[]):  # default argument value is mutable
    VARIABLE = 10
    string = &apos;string&apos;
    print(VARIABLE)</pre>
<p>The expected output for this code is:</p>
<pre>/path/to/file/script.py: Line 5: S010 Argument name &apos;S&apos; should be snake_case
/path/to/file/script.py: Line 5: S012 Default argument value is mutable
/path/to/file/script.py: Line 6: S011 Variable &apos;VARIABLE&apos; in function should be snake_case</pre>
<p>Note that the message for the line&nbsp;print(VARIABLE)&nbsp;is not printed since it was already output for line 6, where the variable&nbsp;VARIABLE&nbsp;is assigned a value.</p>
<h5>Extra</h5>
<p>You can also use AST to rewrite some of the checks implemented before. It would be especially convenient for checking the names of functions and classes.</p>
<p>If you would like to continue improving this project, you can also:</p>
<ul>
    <li>
        <p>implement all of the standard PEP8 checks;</p>
    </li>
    <li>
        <p>display column numbers;</p>
    </li>
    <li>
        <p>disable some of the checks via command-line arguments.</p>
    </li>
</ul>