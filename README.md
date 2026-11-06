# Les vulnérabilités et techniques d'attaques — TP

Travaux pratiques du module Diginamic **« Les vulnérabilités et techniques
d'attaques »** (RNCP40573, sécurité applicative J2/J3), réalisés par
**Badr-Eddine Tirari**.

> Dépôt **privé** : il contient mes réponses aux TP et le dossier du TP
> intégrateur noté. Cours de référence (public) :
> https://github.com/DiginamicAcademy/cours-securite-vulnerabilites-attaques

## Contenu

### `TP-rendus/` — dossiers Word
| Fichier | TP |
| --- | --- |
| `Tirari_Badr_TP01_classer-owasp.docx` | 01 — Classer dans le Top 10 OWASP |
| `Tirari_Badr_TP02_trouver-injection.docx` | 02 — Repérer une injection |
| `Tirari_Badr_TP03_revue-de-code.docx` | 03 — Revue de code (constats, gravité) |
| `Tirari_Badr_TP04_menace-pipeline-data.docx` | 04 — Menaces d'un pipeline de données |
| `Tirari_Badr_TP05_avis-exposition.docx` | 05 — Lire un advisory, avis d'exposition |
| `Tirari_Badr_TP07_reconstituer-attaque.docx` | 07 — Reconstituer une attaque (kill chain) |
| `Tirari_Badr_TP09_course-patch-exploit.docx` | 09 — La course patch / exploit |
| `Tirari_Badr_TP10_exploiter-corriger.docx` | 10 — Exploiter / corriger une CVE |
| `Tirari_Badr_TP12_menace-prevention.docx` | 12 — Analyse menace / prévention / détection |
| `Tirari_Badr_TP13_kill-chain-data.docx` | 13 — Kill chain d'une fuite de données |
| `Tirari_Badr_Fiche_ch06-08-11.docx` | Fiche de synthèse (chap. sans TP) |
| `Tirari_Badr_TP-INTEGRATEUR_dossier-DIGICHEESE.docx` | **TP intégrateur noté** |

### `scripts/` — exploits et tests de non-régression (lab local DIGICHEESE)
| Script | Rôle |
| --- | --- |
| `exploit_sqli.py` | Injection SQL sur `/products/search` (service `vulnerable`, port 8080) |
| `test_sqli_nonregression.py` | Vérifie que l'injection SQL ne renvoie plus toute la table |
| `cve_exploit.py` | Injection `xmlattr` (CVE-2024-22195) sur le service `cve` (port 8082) |
| `cve_test_nonregression.py` | Vérifie que l'injection `xmlattr` ne passe plus |

Usage : `python <script>.py [base_url]`.

## Correctifs appliqués (cause racine)
- **Injection SQL** (`vulnerable/app.py`, `search_products`) : requête paramétrée.
- **CVE-2024-22195** (`cve/`) : Jinja2 3.1.2 → 3.1.4 **et** validation des clés par liste blanche.

> ⚠️ **Cadre légal.** Tout a été réalisé sur le lab Docker local, sur des données
> fictives. Accéder ou se maintenir sans droit dans un système d'autrui est un
> délit (art. 323-1 et suivants du Code pénal).
