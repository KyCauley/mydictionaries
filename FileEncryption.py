Encrypt = {}
Encrypt['A'] = '%'
Encrypt['a'] = '9'
Encrypt['B'] = '@'
Encrypt['b'] = '#'
Encrypt['C'] = '1'
Encrypt['c'] = '!'
Encrypt['D'] = '2'
Encrypt['d'] = '3'
Encrypt['E'] = '4'
Encrypt['e'] = '$'
Encrypt['F'] = '5'
Encrypt['f'] = '6'
Encrypt['G'] = '^'
Encrypt['g'] = '7'
Encrypt['H'] = '&'
Encrypt['h'] = '8'
Encrypt['I'] = '*'
Encrypt['i'] = '('
Encrypt['J'] = ')'
Encrypt['j'] = '-'
Encrypt['K'] = '_'
Encrypt['k'] = '='
Encrypt['L'] = '+'
Encrypt['l'] = '`'
Encrypt['M'] = '~'
Encrypt['m'] = '/'
Encrypt['N'] = '?'
Encrypt['n'] = '.'
Encrypt['O'] = '>'
Encrypt['o'] = ','
Encrypt['P'] = '<'
Encrypt['p'] = ';'
Encrypt['Q'] = ':'
Encrypt['q'] = '"'
Encrypt['R'] = '|'
Encrypt['r'] = ']'
Encrypt['S'] = '}'
Encrypt['s'] = '['
Encrypt['T'] = '{'
Encrypt['t'] = 'k'
Encrypt['U'] = 'y'
Encrypt['u'] = 'l'
Encrypt['V'] = 'e'
Encrypt['v'] = 'c'
Encrypt['W'] = 'a'
Encrypt['w'] = 'u'
Encrypt['X'] = 'l'
Encrypt['x'] = 'd'
Encrypt['Y'] = 'o'
Encrypt['y'] = 'g'
Encrypt['Z'] = 's'
Encrypt['z'] = 'P'

infile = open('info_security.txt','r')
outfile = open('encrypted.txt','w')

for letters in infile:
    for x in letters:
        encryption = Encrypt.get(x, x)
        outfile.write(encryption)
