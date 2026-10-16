#!/bin/sh
# Garde un `hugo server` en vie sur le port 1313, détaché de tout terminal.
# Repris d'INF1410 (2026-08-31), pour le même mal : le surveillant de fichiers
# de Hugo cesse parfois de réagir en session longue, et le serveur finit par
# mourir sans laisser de trace. La boucle le relance et garde le journal.
#
# Accessible aussi depuis le réseau local (iPad) : http://MBA-cjauvin.local:1313/inf1901-teluq/
# Lancer une fois, détaché :  nohup .hugo-serve/supervise.sh > .hugo-serve/serveur.log 2>&1 &
# Arrêter :                   pkill -f hugo-serve/supervise.sh ; pkill -f 'hugo server.*1313'
cd "$(dirname "$0")/.." || exit 1
while true; do
  echo "=== démarrage $(date '+%F %T') ==="
  hugo server --bind 0.0.0.0 --baseURL http://MBA-cjauvin.local:1313/inf1901-teluq/ --appendPort=false --disableFastRender --noHTTPCache --port 1313
  echo "=== arrêt (code $?) $(date '+%F %T') ==="
  sleep 2
done
