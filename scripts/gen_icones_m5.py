"""Module 5, « Quels problèmes l'IA pose-t-elle ? » : une icône par famille de problèmes, pour le tableau des neuf
familles. Pastilles carrées au fond parchemin (lisibles en thème sombre), tracé au trait."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module5" / "icones"
FOND, BORD, TEAL, BRUN, ROUGE, BLEU, VIOLET, VERT = "#efe7d3", "#d9cbac", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#7b5ea7", "#5a8a3a"
T = 'fill="none" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"'

ICONES = {
    # une tête de profil, un point d'interrogation à l'intérieur
    "philosophique": (VIOLET, f'<path d="M30 39 V33 Q37 32 37 26 L39.5 23 L37 21.5 Q37 10 25 10 Q13 10 13 21 Q13 28 18 31 V39" {T}/>'
                              f'<path d="M21.5 18.5 Q21.5 15 25 15 Q28.5 15 28.5 18.5 Q28.5 21 25 22.5 V24.5" {T}/>'
                              '<circle cx="25" cy="28.2" r="1.6" fill="{c}"/>'),
    # un erlenmeyer
    "scientifique": (BLEU, f'<path d="M20 9 H28 M21 9 V20 L12 36 Q11 39 14 39 H34 Q37 39 36 36 L27 20 V9" {T}/>'
                           f'<path d="M15.5 30 H32.5" {T}/><circle cx="21" cy="34" r="1.4" fill="{{c}}"/><circle cx="27" cy="33" r="1.1" fill="{{c}}"/>'),
    # une balance
    "morale": (BRUN, f'<path d="M24 9 V38 M16 38 H32 M11 15 H37 M24 12 V15" {T}/>'
                     f'<path d="M11 15 L6 26 H16 Z M37 15 L32 26 H42 Z" {T}/>'),
    # des barres et une flèche qui monte
    "economique": (TEAL, f'<path d="M9 39 H39 M13 39 V31 M21 39 V26 M29 39 V29 M37 39 V20" {T}/>'
                         f'<path d="M11 24 L19 17 L26 21 L37 10 M31 10 H37 V16" {T}/>'),
    # un marteau de juge et son socle
    "juridique": (BRUN, f'<path d="M14 21 L23 12 M20 27 L29 18 M16.5 15.5 L24.5 23.5 L22 26 L14 18 Z" {T}/>'
                        f'<path d="M22 21 L36 35" {T}/><path d="M9 39 H25 M11 39 V35 H23 V39" {T}/>'),
    # trois personnes
    "sociale": (BLEU, f'<circle cx="24" cy="15" r="4.5" {T}/><path d="M16 35 Q16 23 24 23 Q32 23 32 35" {T}/>'
                      f'<circle cx="12" cy="19" r="3.5" {T}/><path d="M6 35 Q6 26 12 26 Q15 26 16.5 28" {T}/>'
                      f'<circle cx="36" cy="19" r="3.5" {T}/><path d="M42 35 Q42 26 36 26 Q33 26 31.5 28" {T}/>'),
    # une feuille
    "environnementale": (VERT, f'<path d="M12 37 Q10 13 37 10 Q39 35 14 36 Z" {T}/><path d="M12 37 Q21 25 30 17" {T}/>'),
    # une personne et un cœur
    "humaine": (ROUGE, f'<circle cx="19" cy="14" r="5" {T}/><path d="M9 38 Q9 24 19 24 Q24 24 26.5 27" {T}/>'
                       f'<path d="M34 38 Q26 32 26 27.5 Q26 24 29.5 24 Q32 24 34 27 Q36 24 38.5 24 Q42 24 42 27.5 Q42 32 34 38 Z" {T}/>'),
    # un triangle d'avertissement
    "risques": (ROUGE, f'<path d="M24 8 L42 39 H6 Z" {T}/><path d="M24 19 V29" {T}/><circle cx="24" cy="34" r="1.7" fill="{{c}}"/>'),
}

OUT.mkdir(parents=True, exist_ok=True)
for nom, (coul, corps) in ICONES.items():
    corps = corps.replace("{{c}}", coul).replace("{c}", coul).replace("<path ", f'<path stroke="{coul}" ').replace("<circle cx", f'<circle stroke="{coul}" cx')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="36" height="36" role="img">'
           f'<rect x="1" y="1" width="46" height="46" rx="10" fill="{FOND}" stroke="{BORD}" stroke-width="1.5"/>{corps}</svg>\n')
    (OUT / f"{nom}.svg").write_text(svg)
print(len(ICONES), "icônes écrites dans", OUT)
