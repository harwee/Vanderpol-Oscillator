
topdf: main vanderpol_130010051.png vanderpol_130010051.tex
	pdflatex vanderpol_130010051.tex

main: test
	python vanderpol.py

test:
	python test.py

target: prerequisites
	recipe

clean:
	rm -rf __pycache__
	rm -rf *.out
	rm -rf *.mp4 
	rm -rf *.log
	rm -rf *.png
	rm -rf *.aux
	rm -rf *.pdf