# OWA-Dict
Two simple scripts to create OWA usernames from a list of first + last names. It also contains a script to build combinations of a custom dictionary of words, scraped from a website or file metadata, and outputs a text file with all combinations. A common strategy when creating wordlists of an image in forensics.

Formatting of the dictionary is explained in Words.txt
Formatting of names is explained in Names.py


Look at the examples and the output after execution.

No dependencies outside of internal Python libs. This means that no venv is needed (PEP 668). Don't install globally, just clone to a folder, chmod and run in said directory. Was initially made to be used with Ruler, for OWA password spraying.
* https://github.com/sensepost/ruler



## NOTE: The output wordlist will become VERY large if you include a large dictionary. My example is almost 10 MB. Ensure that your VM has sufficient storage if using large dictionaries. Consider using NTFS or ZFS compression on the working folder if this is problematic for your use case.



## HTTrack2Wordlist looks for many obscure HTML tags, elements and constructs by default. It filters out duplicate occurrences. You can expand the list with more HTML Elements, depreciated or not. Refer to https://developer.mozilla.org/en-US/docs/Web/HTML/Element

You do not need to explicitly use HTTrack, you can save source manually. But HTTrack will recursively download subdirectories, assets and scripts locally from an website, and is thus the most convenient way to build a custom wordlist automatically.


Note that currently, JSON, XML, CSS (Files, not inline), CSV ETC are treated as plaintext files and parsed accordingly. Thus, the only thing that will be tokenized are things included in the initial list. You can implement handling of other file types, or specify the list accordingly if you want proper support for other file types.


If you get too much junk from the CSS/XHR/XML/JS/MD/JSON ETC files, simply change the code accordingly or point to a directory with either nothing or exclusively HTML/HTM files.