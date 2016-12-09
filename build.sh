#!/bin/bash
rm -rf *.aux
rm -rf *.bbl
rm -rf *.blg
rm -rf *.pdf
rm -rf *.log
#rm body.tex
echo "preparing latex"
#python gdoc2latex.py "https://docs.google.com/document/d/1250KVkX4lfCBlHjB35O-q0AnfDKTLMKgJei_goj5fNU/edit"  > body.tex 
echo "latexing"
pdflatex separability.tex
echo "creating bibtex"
python gdoc2latex.py "https://docs.google.com/document/d/1LpVyucw8MNplvaLsRehRBzmKMgfCC2TI8pNOv9E9YWk/edit" > ref.bib
bibtex separability
echo "creating PDF"
pdflatex separability.tex
pdflatex separability.tex

rm -rf *.aux
rm -rf *.bbl
rm -rf *.blg
rm -rf *.log
rm -rf *.out
#rm body.tex
rm ref.bib
echo "DONE"
