import subprocess

ingredients = [
    ('Red','Yellow','Green'),
    ('Red','Yellow','Blue'),
    ('Red','Yellow','White'),
    ('Red','Green','Blue'),
    ('Red','Green','White'),
    ('Red','Blue','White'),
    ('Yellow','Green','Blue'),
    ('Yellow','Green','White'),
    ('Yellow','Blue','White'),
    ('Green','Blue','White'),
]

# Target Card Back
subprocess.run(['lualatex', '--jobname=target_card_back', '--output-directory=Images/TTSCards', './target_card_back.tex'])
subprocess.run(['convert', 'Images/TTSCards/target_card_back.pdf', 'Images/TTSCards/target_card_back.png'])

# Target Cards
for x,y,z in ingredients:
    argstring = r'\newcommand\first{%s}\newcommand\second{%s}\newcommand\third{%s}'% (x,y,z)
    command_string = '"' + argstring + r'\input{./target_card.tex}' + r'"'
    subprocess.run(['lualatex', '--jobname=target_card_%s%s%s' % (x,y,z), '--output-directory=Images/TTSCards', command_string])
    subprocess.run(['convert', 'Images/TTSCards/target_card_%s%s%s.pdf' % (x,y,z), 'Images/TTSCards/target_card_%s%s%s.png' % (x,y,z)])

# Finale Card 4
w,x,y,z = 'Red', 'Yellow', 'Green', 'Blue' 
argstring = r'\newcommand\first{%s}\newcommand\second{%s}\newcommand\third{%s}\newcommand\fourth{%s}'% (w,x,y,z)
command_string = '"' + argstring + r'\input{./finale_card_4.tex}' + r'"'
subprocess.run(['lualatex', '--jobname=finale_card_4', '--output-directory=Images/TTSCards', command_string])
subprocess.run(['convert', 'Images/TTSCards/finale_card_4.pdf', 'Images/TTSCards/finale_card_4.png'])

# Finale Card 5
v,w,x,y,z = 'Red', 'Yellow', 'Green', 'Blue', 'White' 
argstring = r'\newcommand\first{%s}\newcommand\second{%s}\newcommand\third{%s}\newcommand\fourth{%s}\newcommand\fifth{%s}'% (v,w,x,y,z)
command_string = '"' + argstring + r'\input{./finale_card_5.tex}' + r'"'
subprocess.run(['lualatex', '--jobname=finale_card_5', '--output-directory=Images/TTSCards', command_string])
subprocess.run(['convert', 'Images/TTSCards/finale_card_5.pdf', 'Images/TTSCards/finale_card_5.png'])

# Fireworks Cards Backs
ingredients = [
    ('red', 'yellow'),
    ('red', 'green'),
    ('red', 'blue'),
    ('red', 'white'),
    ('yellow', 'green'),
    ('yellow', 'blue'),
    ('yellow', 'white'),
    ('green', 'blue'),
    ('green', 'white'),
    ('blue', 'white'),
]

for x,y in ingredients:
    argstring = r'\newcommand\first{%s}\newcommand\second{%s}' % (x,y,)
    command_string = '"' + argstring + r'\input{./fireworks_card_back.tex}' + r'"'
    subprocess.run(['lualatex', '--jobname=fireworks_card_back_%s%s' % (x,y), '--output-directory=Images/TTSCards', command_string])
    subprocess.run(['convert', 'Images/TTSCards/fireworks_card_back_%s%s.pdf' % (x,y), 'Images/TTSCards/fireworks_card_back_%s%s.png' % (x,y)])

for x,y in ingredients:
    argstring = r'\newcommand\first{%s}\newcommand\second{%s}' % (x,y,)
    command_string = '"' + argstring + r'\input{./fireworks_card_front.tex}' + r'"'
    subprocess.run(['lualatex', '--jobname=fireworks_card_front_%s%s' % (x,y), '--output-directory=Images/TTSCards', command_string])
    subprocess.run(['convert', 'Images/TTSCards/fireworks_card_front_%s%s.pdf' % (x,y), 'Images/TTSCards/fireworks_card_front_%s%s.png' % (x,y)])

for y,x in ingredients:
    argstring = r'\newcommand\first{%s}\newcommand\second{%s}' % (x,y,)
    command_string = '"' + argstring + r'\input{./fireworks_card_front.tex}' + r'"'
    subprocess.run(['lualatex', '--jobname=fireworks_card_front_%s%s' % (x,y), '--output-directory=Images/TTSCards', command_string])
    subprocess.run(['convert', 'Images/TTSCards/fireworks_card_front_%s%s.pdf' % (x,y), 'Images/TTSCards/fireworks_card_front_%s%s.png' % (x,y)])

subprocess.run('rm ./Images/TTSCards/*.log', shell=True)
subprocess.run('rm ./Images/TTSCards/*.aux', shell=True)
subprocess.run('rm ./Images/TTSCards/*.pdf', shell=True)