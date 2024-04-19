# OWA-Dict
Two simple scripts to create OWA usernames from a list of first + last names. It also contains a script to build combinations of a custom dictionary of words, scraped from a website or file metadata, and outputs a text file with all combinations. A common strategy when creating wordlists of an image in forensics.

Formatting of the dictionary is explained in Words.txt
Formatting of names is explained in Names.py


Look at the examples and the output after execution.

No dependencies outside of internal Python libs. This means that no venv is needed (PEP 668). Don't install globally, just clone to a folder, chmod and run in said directory. Was initially made to be used with Ruler, for OWA password spraying.
* https://github.com/sensepost/ruler



## NOTE: The output wordlist will become VERY large if you include a large dictionary. My example is almost 10 MB. Ensure that your VM has sufficient storage if using large dictionaries. Consider using NTFS or ZFS compression on the working folder if this is problematic for your use case.
