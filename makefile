.PHONY:  all install clean build upload serve permissions
.SILENT:

XOPP = $(shell find _includes/ -type f -name '*.xopp')
SVG  = $(patsubst %.xopp, %.svg, $(XOPP))

all: build upload

install: ; bundle install

xopp: $(SVG);
build: permissions $(SVG); ! ps -aux | grep "ruby.*jekyll" | grep -v grep -q && bundle exec jekyll build --trace || (echo "ERROR: Jekyll seems to be running already." && exit 1)
serve: permissions $(SVG); ! ps -aux | grep "ruby.*jekyll" | grep -v grep -q && bundle exec jekyll serve --trace --drafts --config _config.yml,_config-local.yml || (echo "ERROR: Jekyll seems to be running already." && exit 1)

upload:
	cd _site && git a . && git c -m "automated commit" && git push -f

clean:
	bundle exec jekyll clean --trace

permissions:
	chmod +x _plugins/*.py

%.svg: %.xopp
	_plugins/xopp_to_svg.py -f $^
