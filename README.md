Links from Wikipedia to Library of Congress websites
====================================================

Scripts & data files for working with the Wikipedia external links dumps

Usage
-----

    ./download-dumps
    pypy dump-wikipedia-links
    for i in *.links; do LC_ALL=C sort -ifu -o $i $i; done

    cat *.links | LC_ALL=C sort -ifu | wc -l
      588236


During the HTTPS migration, these lists are very useful for finding mixed-active content warnings using a tool like [phantomjs-mixed-content](http://github.com/acdha/phantomjs-mixed-content)
