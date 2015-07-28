import sys

import mechanize

if len(sys.argv) == 1:
    uri = "https://750words.com/auth"
else:
    uri = sys.argv[1]

    request = mechanize.Request(mechanize.urljoin(uri, ''))
    response = mechanize.urlopen(request)
    forms = mechanize.ParseResponse(response, backwards_compat=False)
    response.close()
            ## f = open("example.html")
            ## forms = mechanize.ParseFile(f, "http://example.com/example.html",
            ##                              backwards_compat=False)
            ## f.close()
    form = forms[0]
    print form  # very useful!
