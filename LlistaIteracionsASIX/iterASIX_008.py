# 8. Neteja de fitxers temporals: Donada una llista de noms de fitxers, recórrer-la i "esborrar"
# (imprimir per pantalla) només aquells que acabin en .tmp o .log.
FITXERS = [
    '/var/log/dpkg.log.10.gz',
    '/var/log/dbconfig-common',
    '/var/log/dbconfig-common/dbc.log.1',
    '/var/log/dbconfig-common/dbc.log',
    '/var/log/alternatives.log',
    '/var/log/dpkg.log.3.gz',
    '/var/log/auth.log',
    '/var/log/dpkg.log',
    '/var/log/syslog.1',
    '/var/log/alternatives.log.6.gz',
    '/var/log/apport.log',
    '/var/log/btmp.1',
    '/var/log/btmp',
    '/var/log/alternatives.log.2.gz',
    '/var/log/auth.log.2.gz',
    '/var/log/dmesg.3.tmp',
    '/var/log/dpkg.log.2.gz',
    '/tmp/.XIM-unix.log',
    '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-systemd-resolved.service-Ser41h',
    '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-systemd-resolved.service-Ser41h/tmp',
    '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-upower.service-9OWUxh.tmp',
    '/tmp/.X11-unix.tmp',
    '/tmp/.ICE-unix.log',
    '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-ntp.service-erKexg',
    '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-ntp.service-erKexg.tmp',
    '/tmp/snap-private.tmp',
    '/tmp/snap-private-tmp/snap.lxd',
    '/tmp/snap-private-tmp/snap.tmp',
    '/tmp/.font-unix',
    '/tmp/.Test-unix'
]

for f in FITXERS:
    nom_fitxer = f.split("/")[-1]
    parts = nom_fitxer.split(".")
    if "tmp" in parts or "log" in parts:
        print(f)
