topdf: main ../output/vanderpol_130010051.png ../source/vanderpol_130010051.tex
	pdflatex vanderpol_130010051.tex
	mv ./vanderpol_130010051.pdf ../output/vanderpol_130010051.pdf
	mv ./vanderpol_130010051.aux ../output/vanderpol_130010051.aux
	mv ./vanderpol_130010051.log ../output/vanderpol_130010051.log
	mv ./vanderpol_130010051.out ../output/vanderpol_130010051.out

main: 
	python vanderpol.py

test:
	python test.py