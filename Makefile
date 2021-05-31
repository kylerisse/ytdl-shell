test:
	docker build -t ytdl-batch-test .
	docker run -ti ytdl-batch-test bash

install:
	# attempt to install ytdl-shell in /usr/local/bin
	# you must have pip intalled
	which pip
	pip install -r src/requirements.txt
	sudo cp src/ytdl-shell.py /usr/local/bin/ytdl-shell && sudo chmod +x /usr/local/bin/ytdl-shell
