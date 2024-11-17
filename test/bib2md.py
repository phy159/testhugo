import bibtexparser

library = bibtexparser.parse_file("publications.bib")
n_entries = len(library.entries)
i=0
entry = library.entries[0].fields
len(entry)
library.entries[0].fields