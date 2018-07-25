Instructions:


STEP 1
Create text.tex for the content page in latex format, but remove the following:
- preamble, \begin{document} and \end{document}
- images: these should be moved into their own separate files, WITH preamble, begin/end document, etc (it should be able to typeset)

STEP 2
We now transform the latex format into html format
Run sed:
```
sed -r -f latex2html text.tex > text-temp.html
```
And then awk:
```
awk -f latex2html2 text-temp.html > text.html
```

STEP 3
We now transform the images into svg format.
htlatex image.tex
It creates (among other things) an svg image that can be uploaded to canvas, and inserted into the html page by hand

STEP 4
Paste result into canvas content page. Check that it looks good (optional: add new commands to sed/awk files). Several things need to be done by hand, for example:
- tables
- pasting proof text into the proof button


(Optional step: see if there are any commands that weren't replaced but should be (because they will occur more often), and add it to the script.)
