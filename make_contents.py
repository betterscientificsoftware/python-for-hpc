#!/usr/bin/env python

# Run ./make_contents.py
# _data/navigation.yml sidebar will be updated from _pages/content.md
# If test_run is set to True, then will create prposed file in out_tmp.md
import shutil
import re

infile = "_pages/content.md"
#infile = "tmp.md"

test_run = False
permalink = "/python-for-hpc/"
section_name = "##"
section_link = "###"
#child_link = "####"
template = "_data/navigation.tmpl"
bkup = "nav.tmp"

if test_run:
    outfile = "out_tmp.md" # Manually copy to _data/navigation.yml
else:
    outfile = "_data/navigation.yml"
    shutil.copyfile(outfile, bkup)

shutil.copyfile(template, outfile)


def add_entry(line, prefix="", link=False):
    elements = line.split()
    elements.pop(0)
    title = (" ").join(elements)
    out = prefix + "    - title: \"" + title + "\"\n"
    if link:
        linkname = ("-").join(elements).lower().strip(':')
        linkname = re.sub('[/():]', '', linkname) # Add any symbols to remove from line                
        out = out + prefix + "      url: " + permalink + "#" + linkname + "\n"
    return out


prefix=""
new_section = True
with open (outfile, 'a') as g:
    with open(infile) as f:
        #content = f.readlines()
        for line in f:
            if line.startswith(section_name):
                if line.startswith(section_link):
                    if (new_section):
                        g.write("      children:\n")
                        prefix = "  "
                        new_section = False
                    g.write(add_entry(line,prefix,link=True))
                else:
                    new_section = True
                    g.write(add_entry(line))
