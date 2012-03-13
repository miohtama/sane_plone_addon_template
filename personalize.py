#!/usr/bin/env python
"""

    Creates a personally named version of youraddon.

    1. Copy to a new folder (assume we are in buildout/src)

    1. Do in-place template string replacement of template strings

    2. Walk through all files/folders and rename them

    sed/awk would be nice but let's stick in Python because all other code is Python,
    and we might need to take care of poor Windoze users :(

"""

import sys
import shutil
import os
import fnmatch

TEMPLATE_NAME="youraddon"

IGNORE_MASKS=["*.pyc", "*.pyo", "*.git*", "*.egg*", "*.EGG*"]

def process(fname, newname):
    """ """

    # See if we don't want to touch this file
    for mask in IGNORE_MASKS:
        if fnmatch.fnmatch(fname, mask):
            return

    # Do in-place replacement of template strings,
    # all one of them.
    # Because we are workin on a copy, don't be
    # that pick about atomicity
    if not os.path.isdir(fname):

        # Read the source file
        f = open(fname, "rt")
        data = f.read()
        f.close()

        # Replace template variables
        data = data.replace(TEMPLATE_NAME, newname)

        # Clean up all lines between EXAMPLES START and EXAMPLES END section
        new_lines = []
        filtering = False
        for line in data.split("\n"):
            if "EXAMPLES START" in line:
                filtering = True
            
            if not filtering:
                new_lines.append(line)

            if "EXAMPLES END" in line:
                filtering = False

        # Write the output
        data = "\n".join(new_lines)

        f = open(fname, "wt")       
        f.write(data)
        f.close()

    path, file = os.path.split(fname)

    if file == TEMPLATE_NAME:
        # Rename youraddon folders to something else
        newname = os.path.join(path, newname)
        shutil.move(fname, newname)

def post_cleanup(target, newname):
    """
    Remove unneeded files.
    """

    # Clean up templates folder from all templates
    templates = os.path.join(target, newname, "templates")
    for name in os.listdir(templates):
        fname = os.path.join(templates, name)
        os.remove(fname)
    
    # Remove git data if it's around
    git = os.path.join(target, ".git")
    if os.path.exists(git):
        shutil.rmtree(git)

    # Remove egg info if it's around
    eggy = os.path.join(target, "youraddon.egg-info")
    if os.path.exists(eggy):
        shutil.rmtree(eggy)


    # Remove README
    readme = os.path.join(target, "README.rst")
    if os.path.exists(readme):
        os.remove(readme)

def fancy_replace(newname):
    """ """

    source = os.getcwd()

    target = os.path.join(os.getcwd(), "..", newname)
    if os.path.exists(target):
        print "Already exists:" + target
        print "Plese remove first"
        sys.exit(1)

    # Create a copy of the skeleton
    shutil.copytree(source, target)

    # Replace strings and filenames
    for root, dirs, files in os.walk(target, topdown=False):
        for name in files:
            fname = os.path.join(root, name)
            process(fname, newname)
    
        for name in dirs:
            fname = os.path.join(root, name)
            process(fname, newname)

    post_cleanup(target, newname)

    print "Created ../" + newname

def main():
    """ """

    if len(sys.argv) < 2:
        print "Usage: ./personalize.py yourfancyname"
        print "The name must contain only lowercase a-z"
        sys.exit(1)

    fancy_replace(sys.argv[1])


if __name__ == "__main__":
    main()
