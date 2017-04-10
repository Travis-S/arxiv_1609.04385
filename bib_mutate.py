import bibtexparser

def mutate_bibtex_entry(entry):

    #Does mutation of the journal name if journal *is* arxiv
    try:
        if str(entry['journal']).lower() == 'arxiv':
            entry['journal'] = '{0}:{1}'.format(entry['journal'],\
                                                 entry['arxivid'])
    except Exception, err:
        pass
    
    pop_keys = ['file', 'keywords', 'abstract', 'isbn', 'issn',\
               'archiveprefix', 'arxivid', 'eprint']

    for key in pop_keys:
        entry.pop(key, None)
    return entry

def main():

    #Open up the bibliography file produced by Mendeley
    with open('modelselectionpaper.bib') as bibtex_file:
        bibtex_str = bibtex_file.read()

    #Load the bib into a database
    bib_database = bibtexparser.loads(bibtex_str)

    #Mutate the entries in the database
    new_entries = map(lambda e: mutate_bibtex_entry(e), bib_database.entries)

    writer = bibtexparser.bwriter.BibTexWriter()
    with open('wilkspaper.bib', 'w') as bibfile:
        bibfile.write(writer.write(bib_database))

if __name__ == '__main__':
    main()