

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
