from pathlib import Path

er_konkurransemappe = lambda x: x.is_dir() and x.name.startswith("20") and len(x.name) == 4
er_pythonfil = lambda x: x.name.endswith(".py")

konkurransemapper = [p for p in Path(".").iterdir() if er_konkurransemappe(p)]

løsninger = {k.name: {} for k in konkurransemapper}

for mappe in konkurransemapper:
    pythonfiler = [fil for fil in mappe.iterdir() if er_pythonfil(fil)]
    for pyfil in pythonfiler:
        
        with open(pyfil, "r", encoding="utf-8") as f:
            løsninger[mappe.name][pyfil.name.lstrip("0").removesuffix(".py")] = ('løst' in f.readline())


with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Advent of Code\n\n")
    
    for mappe in sorted(konkurransemapper, key=lambda x: -int(x.name)):
        f.write("### " + mappe.name)
        for i in range(1,26):
            if (i-1)% 5 == 0:
                f.write("<br>\n")
            for deloppgave in "ab":
                oppgave = f"{i}{deloppgave}"

                status = ("⬛️" if oppgave not in løsninger[mappe.name] else ("🟩" if løsninger[mappe.name][oppgave] else "🟨"))
                f.write(status)
            f.write(" ")
        f.write("\n")

