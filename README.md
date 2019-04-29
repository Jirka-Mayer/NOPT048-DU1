Domácí úkol 1
=============

Zadání: [https://iuuk.mff.cuni.cz/~husek/vyuka/optmet1819/ukol-01.pdf](https://iuuk.mff.cuni.cz/~husek/vyuka/optmet1819/ukol-01.pdf)


Spuštění
--------

Generátory lineárních programů jsou napsané v pythonu 3 v každé složce pod jménem `generator.py`. Spuštění řešiče na výsledku generátoru vypadá takto:

    glpsol -m <(cat example-input.txt | python3 generator.py)

V každé složce je i ukázkový vstup `example-input.txt` a ručně psaný model na kterém jsem LP vymýšlel `model.mod`.


Topologické uspořádání (úloha 1)
--------------------------------

Každý vrchol `v_i` dostane celočíselnou nezápornou proměnnou `x[i]` (indexy v LP začínají od 1, ale v zadání od 0). Ta určuje pořadí vrcholu ve výsledném uspořádání. Snažíme se minimalizovat největší hodnotu, takže budeme slačovat horní mez `m`:

    minimize m
    m >= x[i]       pro každé i

Navíc pro každou hranu `v_i --> v_j` musí platit `x[i] < x[j]`, což lze zajistit podmínkou `x[i] <= x[j] - 1`.

Úloha nebude mít řešení, pokud je v grafu cyklus. Navíc, aby se program nezacyklil, je potřeba omezit pořadí přiřazené vrcholům nějakou dobrou konstantou (např. počet vrcholů), aby byl prohledávaný prostor konečný (a menší).


Krátké cykly (úloha 2)
----------------------

> Indexy vrcholů v glpsolu jsou opět od 1, ale v pythonu a výstupu od 0

Nejprve potřebuji nějak označit hrany, které se mají odebrat, takže pro každou hranu `(i, j)` vytvořím booleovskou proměnnou `x["i_j"]`. Jelikož chci mít co nejmenší cenu odebraných hran, tak budu minimalizovat součin těchto proměnných s jejich váhami. Odebrání nějaké hrany cyklu vynutíme analogií disjunkce `x[_] + x[_] + x[_] >= 1` pro všechny hrany na cyklu. Cykly (3,4-cykly) najdeme algoritmicky prohledáváním do šířky v pythonu.

Úloha bude mít nějaké řešení pokaždé, protože vždy máme možnost prostě odebrat všechny hrany. Takové řešení je určitě přípustné, protože se splní všechny disjunkce a prázdné disjunkce nemáme.
