
topdf: main ./source/vanderpol_130010051.png ./source/vanderpol_130010051.tex
	pdflatex ./source/vanderpol_130010051.tex --result=./output/vanderpol_130010051.pdf

main:
	mkdir -p output
	cd source && make

test:
	python ./source/test.py

target: prerequisites
	recipe

clean:
	rm -rf ./source/__pycache__
	rm -rf ./output/
