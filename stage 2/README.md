<h1>Stage 2/5: New checks</h1>
<h5>Description</h5>
<p>Let&apos;s add a few more checks to the program. All of them are consistent with the PEP8 style guide.</p>
<h5>Objectives</h5>
<p>In this stage, you need to add checks for the following five errors to your program:</p>
<ul>
    <li>
        <p>[S002]&nbsp;Indentation is not a multiple of four;</p>
    </li>
    <li>
        <p>[S003]&nbsp;Unnecessary semicolon after a statement (note that semicolons are acceptable in comments);</p>
    </li>
    <li>
        <p>[S004]&nbsp;Less than two spaces before inline comments;</p>
    </li>
    <li>
        <p>[S005]&nbsp;TODO found (in comments only and case-insensitive);</p>
    </li>
    <li>
        <p>[S006]&nbsp;More than two blank lines preceding a code line (applies to the first non-empty line).</p>
    </li>
</ul>
<p>Please note that:</p>
<ol>
    <li>
        <p>If a line contains the same stylistic issue several times, your program should print the information only once. However, if a single line has several issues with different types of error codes, they should be printed as a sorted list.</p>
    </li>
    <li>
        <p>To simplify the task, we consider it acceptable if your program finds some false-positive stylistic issues in strings, especially in multi-lines (&apos;&apos;&apos;...&apos;&apos;&apos;&nbsp;and&nbsp;&quot;&quot;&quot;...&quot;&quot;&quot;).</p>
    </li>
    <li>
        <p>We recommend that you break your code into a set of functions to avoid confusion.</p>
    </li>
</ol>
<p>Once again:</p>
<ul>
    <li>
        <p>The path to the file with Python code is obtained from standard input.</p>
    </li>
    <li>
        <p>The general output format is:</p>
    </li>
</ul>
<pre>Line X: Code Message</pre>
<ul>
    <li>The lines with found issues must be output in ascending order.</li>
</ul>
<h5>Examples</h5>
<p>Here is an example of badly styled Python code (please never write code like this!):</p>
<pre>print(&apos;What\&apos;s your name?&apos;) # reading an input
name = input();
print(f&apos;Hello, {name}&apos;);  # here is an obvious comment: this prints a greeting with a name


very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)



def some_fun():
    print(&apos;NO TODO HERE;;&apos;)
    pass; # Todo something</pre>
<p>It contains nine code style issues:</p>
<pre>Line 1: S004 At least two spaces required before inline comments
Line 2: S003 Unnecessary semicolon
Line 3: S001 Too long
Line 3: S003 Unnecessary semicolon
Line 6: S001 Too long
Line 11: S006 More than two blank lines used before this line
Line 13: S003 Unnecessary semicolon
Line 13: S004 At least two spaces required before inline comments
Line 13: S005 TODO found</pre>
<p><br></p>
<p><br></p>