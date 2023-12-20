<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/veticus/lwu">lwu</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/veticus">Veticus</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

# About lwu
Lazy Word Unscrambler.
Takes a set of letters to make words from them.
The desired length of words can be specified.
Which letter/letters is/are at which position/positions can be specified.

On launch the program will look for a wordlist and a "nogood" list in the `~/.lwu` directory.
If none are found, they will be generated.

By default a set of `en_US` lists are generated.
Additionally a config file will be placed in the directory, and used to initialise variables that define the programs behavior.



# Feature wish list
- [ ] Interactive mode
- [ ] "regular" CLI mode
- [ ] "piped" mode
- [ ] API mode
- [ ] Package mode
- [ ] Maybe pickle lists?
- [ ] Or maybe have them as pandas? Maybe sqlite3? Compare performance and memory usage.


# Query syntax
Multiple “letter/position” combinations (like e4) can be added.

`arsenic 4 e4`
(with the letters arsenic get all words with length 4 and an e at position 4)

`arsenic 4`
(with letters arsenic get all words with length 4)

`arsenic e4`
(with letters arsenic get all words with e in the 4th position)

`arsenic`
(get all words with the letters arsenic)

`e4`
(with the previous letters get the words with e on position 4)
(only for interactive mode, and if a set of letters has previously been set)

`4`
(with previous letters get all words with length four)
(only for interactive mode, and if a set of letters has previously been set)

# Interactive mode commands
`:quit`
(quit program)

`:add arsenic`
(adds the word arsenic to wordlist)

`:remove arsenic`
(removes word from wordlist)

`:nogood arsenic`
(as above, and adds word to “nogood” list, preventing it from being re-added by merging new dicts in. Also removes word from wordlist.)

`:good arsenic`
(removes the word arsenic from the nogood list)

`:lang en_gb`
(uses the en_gb wordlist and nogood lists)

`:lang en`
(enumerates all languages that start with en and have a wordlist and nogood list) (ask user user to enter name of language to use)

`:lang`
(lists all languages that have a wordlist and nogood list) (ask user to enter name of language to use)

`:help`
(shows a help text)


# CLI args and flags
| Arg/flag                             | Description                                                                                                                               |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| letters                              | the letters to unscramble                                                                                                                 |
| length                               | the length of the word to be found. All lengths will be shown, if blank                                                                   |
| letter/position[s]                   | zero or more pairs of letters and at which position in the word they're expected.<br/>E.g.: e4 - for a word with an e on the fourth place |
|                                      | multiple pairs can be supplied seperated by space. E.g.: "e4 j11"                                                                         |
| `-—add-dict PATH`                    | given a path to a file with one word per line, merge those words into wordlist (except words in nogood list)                              |
| `—c`<br/>`--cleanup`                 | deletes all files made by this program                                                                                                    |
| `—-import-nogood PATH`               | imports nogood list from the specified path                                                                                               |
| `—-export-nogood PATH`               | exports nogood list to the current directory                                                                                              |
| `—-import-wordlist PATH`             | imports wordlist from the specified path                                                                                                  |
| `—-export-wordlist PATH`             | exports wordlist to the current directory                                                                                                 |
| `-l`<br/>`--lang`                    | print available languages                                                                                                                 |
| `--lang en`                          | print available languages starting with en                                                                                                |
| `--lang en_gb`                       | sets “en_us” as default language in settings file                                                                                         |
| `—version`<br/>`-v`                  | prints version                                                                                                                            |
| `-h`<br/>`-—help`<br/>`-?`<br/>`-—?` | print help                                                                                                                                |
| `—j`<br/>`--json-output`             | gives output as json                                                                                                                      |
| `—a`<br/>`--fastapi`                 | loads the fastapi module, attempting to expose the functionalities as a REST api on port 8000.                                            |
| `--port n`                           | when using “—a” overrides the port to use for fastapi                                                                                     |
| `--bind-address nnn.nnn.nnn.nnn`     | when using “—a” sets the ip address to let fastapi bind to (will usually work automatically)                                              |
| `--config PATH`                      | to define the path to a non-default config file                                                                                           |

# Synopsis
```
lwu [-c|l|v|j|a|h|?][--config </path/to/config/file>][letters][length][letters/positions]
lwu --add-dict </path/to/file>
lwu --import-nogood </path/to/exported/nogood/file>
lwu --import-wordlist </path/to/exported/wordlist/file>
lwu --export-wordlist <filename>
lwu --export-nogood <filename>
lwu --lang <lanague code>
lwu --lang <first two letters of language code>
lwu --port <port number>
lwu --bindaddr <IPv4 address>
```

# Expected behaviors and stuff to implement
- On first launch add blank nogood and collection files to OS temp dir or users home dir.
- Append language code to file names, like “collection-en_gb” and “nogood-en_gb”.
- Populate collection from OS wordlist if available, or some kinda api maybe?
- Have list of possible languages via the standard “en_gb” like notation.
- Give output as space seperated words if fixed length.
- Give output as space seperated words with seperators for lengths, if multiple lengths.
- If possible to detect: if output is being piped always print everything as space seperated words.
- If above is possible, maybe print things pretty with “rich” library. Then add “—nopretty” flag/arg to give simple outout as above.
- Get languages somehow from the locales in /usr/share/i18n/SUPPORTED
- Maybe add supported languages, as dictionaries are located?
- Make manual on how to extend the software, for example with new dictionaries.