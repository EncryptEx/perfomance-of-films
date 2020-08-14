<p align="center"><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.archiveteam.org%2Fimages%2Fe%2Fe6%2FImdb_logo.png&f=1&nofb=1" alt="IMBd" height="60"/></p>
<h1 align="center">Film's Perfomance</h1>
<p align="center">A program that computes the average of the films per country.</p>
<p align="center">
	<img src="https://img.shields.io/github/languages/code-size/EncryptEx/perfomance-of-films?label=Code%20Size"/>
	<img src="https://img.shields.io/badge/DB%20Size-1%2C3%20GB-blue"/>
	<img src="https://img.shields.io/github/last-commit/EncryptEx/perfomance-of-films"/>
	<img src="https://img.shields.io/github/v/release/EncryptEx/perfomance-of-films?label=Version%20"/>
	<a href="https://discord.gg/q6Wh3jN"><img src="https://img.shields.io/discord/714403840207749174?label=Discord"/></a>

## Pre requisites  
[Python 3.x Installed](https://www.python.org/downloads/)  

## Tutorial  
1. Fist I download the ``title.akas.tsv.gz`` and then the ``title.ratings.tsv.gz`` ( I'll upload the files renamed and predownloaded, also, the DB file too.)  
  
2. After decompressing them, place the data.tsv files at the same directory where the python program it is.  

**Important**: Rename the data.tsv files to distinguish which one is the title.tsv and ratings.tsv.  

3. Then, run the program.  

**If you don't know how the program works, don't skip any step. AND BE PATIENT**  
## Pre Work and Database Pre-created/downloaded files
[movies.sqlite](https://mega.nz/file/j98CVIqS#nSc_otTRFejnfVKxj1jM_LgLV8AE_rAYxj0z-b04EM8)    
[title.tsv](https://mega.nz/file/D89CWYzZ#bHBRJcE1xEOL-gQ9aP8FdpDhjc-JeIyKBuKWIqQ4gM8)  
[ratings.tsv](https://mega.nz/file/CtkWUaCC#rVY8EZOhwS1V9UF-p2IHQg_6X0kRo0yUTZ012-_w3HM)  

  
## My Story 'n Problems while coding:  
I had to discard the films that:
> Duplicated Films  
> Didn't have a country  
> Films that didn't have a rating  
> Films with "fake" country names: (with slashes or dashes.)  
 
So, after discarding i changed from 10 M (dirty data) rows to 1 M clean (full data) rows.  

Finally, the program computes the avergae per country and it displays out, also, it records it into a file called: ``results.txt``   

**Attention**: Every time that you run the program, you'll rewrite the past results at the results.txt  

## Fonts:
[IMBd Documentation](https://www.imdb.com/interfaces/)  
[title.akas.tsv.gz](https://datasets.imdbws.com/title.akas.tsv.gz)  
[title.ratings.tsv.gz](https://datasets.imdbws.com/title.ratings.tsv.gz)  


<p align="center"><img src="http://randojs.com/images/barsSmall.gif" alt="Animated footer bars" width="100%"/></p>