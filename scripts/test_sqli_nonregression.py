#!/usr/bin/env python3
"""Non-regression injection SQL : l'injection ne doit plus tout renvoyer.
Sortie 0 = sain ; 1 = regression."""
import sys, urllib.parse, urllib.request, json
BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080"
inj = json.loads(urllib.request.urlopen(BASE + "/products/search?" + urllib.parse.urlencode({"q":"' OR '1'='1"}), timeout=5).read())
if len(inj["results"]) > 1:
    print("ECHEC : l'injection renvoie %d produits — REGRESSION." % len(inj["results"])); sys.exit(1)
print("OK : injection neutralisee (%d resultat)." % len(inj["results"])); sys.exit(0)
