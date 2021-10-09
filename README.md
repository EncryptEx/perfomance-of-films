<p align="center">
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.archiveteam.org%2Fimages%2Fe%2Fe6%2FImdb_logo.png&f=1&nofb=1" alt="IMBd" height="60"/>
</p>
<h1 align="center">Film's Perfomance</h1>
<p align="center">A program that computes the average of the films per country.</p>
<p align="center">
<img src="https://img.shields.io/github/languages/code-size/EncryptEx/perfomance-of-films?label=Code%20Size"/>
<img src="https://img.shields.io/badge/DB%20Size-1%2C3%20GB-blue"/>
<img src="https://img.shields.io/github/last-commit/EncryptEx/perfomance-of-films"/>
<img src="https://img.shields.io/github/v/release/EncryptEx/perfomance-of-films?label=Version%20"/>
<a href="https://discord.gg/q6Wh3jN"><img src="https://img.shields.io/discord/714403840207749174?label=Discord"/></a>

## Pre-requisites

[Python 3.x Installed](https://www.python.org/downloads/)  

## Tutorial

1. First, download the ``title.akas.tsv.gz`` file and the ``title.ratings.tsv.gz`` file too. ( I'll upload the files renamed and pre-downloaded, also, the DB file too. See section called [Fonts](https://github.com/EncryptEx/perfomance-of-films#fonts))  
  
2. After decompressing them, place the data.tsv files at the same directory where the python program it is.

```sh
curl -O https://datasets.imdbws.com/title.akas.tsv.gz && gzip -d title.akas.tsv.gz && mv title.akas.tsv title.tsv
```

```sh
curl -O https://datasets.imdbws.com/title.ratings.tsv.gz && gzip -d title.ratings.tsv.gz && mv title.ratings.tsv ratings.tsv
```

**Important**: Rename the data.tsv files to distinguish which one is the title.tsv and ratings.tsv.  

3. Then, run the program.

```sh
python3 movies.py
```

Suggestion: Use ``screen`` command to run the program in the background. [More info here](https://www.shellhacks.com/linux-screen-command-run-in-background/)

```sh
sudo apt-get install screen
```

```sh
screen -S <session_name>
```

And then run the program.

**If you don't know how the program works, don't skip any step. AND BE PATIENT**
For any help, contact me [GitHub](https://github.com/EncryptEx) | [Contact Page](https://encryptex.me/contact).

## Pre Work and Database Pre-created/downloaded files

[movies.sqlite](https://mega.nz/file/j98CVIqS#nSc_otTRFejnfVKxj1jM_LgLV8AE_rAYxj0z-b04EM8)
[title.tsv](https://mega.nz/file/D89CWYzZ#bHBRJcE1xEOL-gQ9aP8FdpDhjc-JeIyKBuKWIqQ4gM8)  
[ratings.tsv](https://mega.nz/file/CtkWUaCC#rVY8EZOhwS1V9UF-p2IHQg_6X0kRo0yUTZ012-_w3HM)  

## My Story 'n Problems while coding  

I had to discard the films that:
> Were Duplicated
> Didn't have a country (\N)  
> Films that didn't have a rating (\NA)
> Films with "fake" country names: (with slashes or dashes.)  
> Fix code to avoid parsing fake countries (last line) solved with (867afed386064ff74eb80f25f46021a3a454239e)

So, after discarding them, I changed from 10 M (dirty data) rows to 1 M clean (full data) rows.  

Finally, the program computes the average per country and displays it out, it also records it into a file called: ``results.txt``

**Attention**: Every time that you run the program, you'll rewrite the past results at the results.txt  

## Fonts

[IMBd Documentation](https://www.imdb.com/interfaces/)  
[title.akas.tsv.gz](https://datasets.imdbws.com/title.akas.tsv.gz)  
[title.ratings.tsv.gz](https://datasets.imdbws.com/title.ratings.tsv.gz)  

<p align="center"><img src="http://randojs.com/images/barsSmall.gif" alt="Animated footer bars" width="100%"/></p>
