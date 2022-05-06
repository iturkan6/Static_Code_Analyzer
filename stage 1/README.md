<h1>Stage 1/5: Search for long lines</h1>
<h5>Description</h5>
<p>To make sure your Python code is beautiful and consistently formatted, you should follow the PEP8 specification and best practices recommended by the Python community. This is not always easy, especially for beginners. Luckily, there are special tools called&nbsp;<strong>static code analyzers</strong> (pylint, flake8, and others) that automatically check that your code meets all the standards and recommendations. These tools don&apos;t execute your code but just analyze it and output all the issues they find.</p>
<p>In this project, you will create a small static analyzer tool that finds some common stylistic mistakes in Python code. This way, you will familiarize yourself with the concept of static code analysis and improve your Python skills along the way.</p>
<p>PEP8 requires that we should &quot;limit all lines to a maximum of 79 characters&quot;, which is designed to make your code more readable. So let&apos;s first make a program that checks that code lines are not too long.</p>
<h5>Objectives</h5>
<p>In this stage, your program should read Python code from a specified file and perform a single check: the length of code lines should not exceed 79 characters.</p>
<p>Note that:</p>
<ol>
    <li>The path to the file is obtained from standard input.</li>
    <li>The general output format is:
        <pre>Line X: Code Message</pre>
        <p>In the format:</p>
        <ul>
            <li>
                <p>X&nbsp;is the number of the line where the issue was found. The count starts from one.</p>
            </li>
            <li>
                <p>Code&nbsp;is the code of the discovered stylistic issue (like&nbsp;S001).</p>
            </li>
            <li>
                <p>Message<strong>&nbsp;</strong>is a human-readable description of the issue (optional).</p>
            </li>For example:
        </ul>
        <p></p>
        <pre>Line 3: S001 Too long</pre>
        <p>This format will be used throughout the project with some minor changes.</p>
    </li>
    <li>The order of the lines should always be first to last.</li>
    <li>Your program can output another message instead of&nbsp;Too long. The rest of the output must exactly match the provided example. In the code&nbsp;S001,&nbsp;S&nbsp;means a stylistic issue, and&nbsp;001&nbsp;is the internal number of the issue.</li>
</ol>
<h5>Examples</h5>
<p>Here is an example of the file&apos;s contents:</p>
<pre>print(&apos;What\&apos;s your name?&apos;)
name = input()
print(f&apos;Hello, {name}&apos;)  # here is an obvious comment: this prints a greeting with a name

very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)</pre>
<p>This code contains two long lines (&gt;79 characters): lines 3 and 5.</p>
<p>Here is the expected output for the given example:</p>
<pre>Line 3: S001 Too long
Line 5: S001 Too long</pre>
<p><br></p>