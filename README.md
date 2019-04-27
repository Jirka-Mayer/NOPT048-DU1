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


Krátké cykly (úloha 2)
----------------------

TODO


Žádné cykly (pozorování)
------------------------


Řešení vzniklo omylem při pokusu o řešení problému krátkých cyklů, bez BFS v generátoru LP.

*Zadání:* Máme graf s ohodnocenými hranami. Chceme najít co nejlevnější podmnožinu hran, po jejímž odebrání dostaneme DAG.

*Převedení na LP:* vezmu topolog uspořádání a umožním porušení podmínek
