#!/bin/bash
rm -rf *.aux
#rm -rf *.bbl
rm -rf *.blg
rm -rf *.log

TAG=`date +'%y%m%d'`
echo "preparing latex"
#python gdoc2latex.py "https://docs.google.com/document/d/1dzCMpYgPO8FswOI56ynHMB19043unNG43ngKhJokmZE/edit?usp=sharing"  > separability.tex
#python gdoc2latex.py "https://docs.google.com/document/d/1GkEQ2LS4-E6yCdB0tgV-fzUjdUBzeOZ1ffe7aiYWzUU/edit?usp=sharing"  > body.tex
echo "latexing"
pdflatex plos_latex_template.tex
echo "creating bibtex"
#python gdoc2latex.py "https://docs.google.com/document/d/1KLq-8gsntsIpZA5LIHDXUB2sR849G8oqWaGuVYF78u4/edit?usp=sharing" > ref.bib
bibtex plos_latex_template
bibtex app
echo "creating PDF"
pdflatex plos_latex_template.tex
bibtex plos_latex_template.aux
bibtex app.aux
pdflatex plos_latex_template.tex
pdflatex plos_latex_template.tex

rm -rf *.aux
#rm -rf *.bbl
rm -rf *.blg
rm -rf *.log
rm -rf *.out
echo "DONE"

