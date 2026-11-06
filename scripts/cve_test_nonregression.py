#!/usr/bin/env python3
"""Test de non-regression CVE-2024-22195 : l'injection ne doit plus passer.
Usage : python test_nonregression.py [base_url]   (defaut http://localhost:8082)
Sortie 0 = sain ; 1 = injection encore possible OU page cassee (regression)."""
import sys, urllib.parse, urllib.request, urllib.error

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8082"
PAYLOAD = "x onmouseover=alert(document.domain)"
url = BASE + "/?" + urllib.parse.urlencode({"q": "Brie", "tri": PAYLOAD})
try:
    resp = urllib.request.urlopen(url, timeout=5); html = resp.read().decode("utf-8", "replace"); code = resp.getcode()
except urllib.error.HTTPError as e:
    html = e.read().decode("utf-8", "replace"); code = e.code
if "onmouseover" in html:
    print("ECHEC : l'injection repasse (onmouseover present) — REGRESSION. [HTTP %s]" % code); sys.exit(1)
if "Brie de Meaux" not in html:
    print("ECHEC : la page ne rend plus le catalogue [HTTP %s]." % code); sys.exit(1)
print("OK : injection bloquee et page fonctionnelle [HTTP %s]." % code); sys.exit(0)
