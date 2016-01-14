#!/usr/bin/env pypy

from __future__ import absolute_import, print_function, division, unicode_literals

import fileinput
from urlparse import urlparse

KNOWN_HTTP_ONLY_PATHS = (
    ('http://hdl.loc.gov', 'hdl.loc.gov'),
    ('http://chroniclingamerica.loc.gov', 'chroniclingamerica.loc.gov'),
    ('http://findingaids.loc.gov', 'findingaids.loc.gov'),
    ('http://eresources.loc.gov', 'eresources.loc.gov'),
    ('http://id.loc.gov', 'id.loc.gov'),
    ('http://www.loc.gov/law', 'loc.gov-law'),
    ('http://www.loc.gov/teachers', 'loc.gov-teachers'),
    ('http://www.loc.gov/jukebox', 'loc.gov-jukebox'),
    ('http://www.loc.gov/bookfest', 'loc.gov-bookfest'),
    ('http://www.loc.gov/pressroom/', 'loc.gov-pressroom'),
)

OUTPUT_FILES = {}

for line in fileinput.input():
    try:
        line = line.decode('utf-8').strip().lower()
    except UnicodeDecodeError:
        print('Unicode error on %s:%s' % (fileinput.filename(), fileinput.filelineno()), file=sys.stderr)
        continue

    # Skip HTTPS links since we don't need to rewrite them:
    if not line.startswith('http:'):
        continue
    elif line.startswith('http://cdn.loc.gov'):
        continue
    elif line.startswith('http://media.loc.gov'):
        continue
    elif line.startswith('http://tile.loc.gov'):
        continue

    for prefix, filename in KNOWN_HTTP_ONLY_PATHS:
        if line.startswith(prefix):
            output_file = filename
    else:
        parsed = urlparse(line)
        if parsed.netloc == 'www.loc.gov' or parsed.netloc == 'loc.gov':
            output_file = 'loc.gov-%s' % parsed.path.split('/')[1]
        else:
            output_file = parsed.netloc

    if output_file not in OUTPUT_FILES:
        OUTPUT_FILES[output_file] = open('%s.urls' % output_file, 'w')

    print(line.encode('utf-8'), file=OUTPUT_FILES[output_file])
