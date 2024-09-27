lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl, llllllllllllIII, lllllllllllIlll, lllllllllllIllI, lllllllllllIlIl, lllllllllllIlII = any, getattr, print, str, int, open, __name__, bool, bytes, list, len, input

from hashlib import sha512 as llllllllllIIll, blake2s as lllIIlIlIllIll, sha256 as IlIIIIllllIIII, sha384 as lIlIlIllIlIlII, blake2b as llIIIIIllllIIl, sha224 as lIIllIIIlllIII, md5 as IllIIIllIlIlII, sha1 as IIIllIIIllIIII
from blake3 import blake3 as IIIIIIlIlIIllI
from argparse import ArgumentParser as IIIIlIlIIIIllI
from os.path import exists as lIIllIIIlIIlll

def lIllllIIllIlIlIlIl(lIIIIlIllIIllIllII):
    llIlIlIlIlIIlIIllI = {32: 'MD5', 40: 'SHA1', 56: 'SHA224', 64: 'SHA256', 96: 'SHA384', 128: 'SHA512', 64: 'BLAKE2b', 66: 'BLAKE2s', 64: 'BLAKE3'}
    return llllllllllllllI(llIlIlIlIlIIlIIllI, llllllllllllllI(lllllllllllIlll, 'fromhex')('676574').decode())(lllllllllllIlIl(lIIIIlIllIIllIllII), 'Unknown hash type')

def IllIIlIlIIIlIllllI(lIllIIllIllIlIllII, IIIIlllIIIlIIIllIl):
    if IIIIlllIIIlIIIllIl == 'MD5':
        return IllIIIllIlIlII(llllllllllllllI(lIllIIllIllIlIllII, llllllllllllllI(lllllllllllIlll, 'fromhex')('656e636f6465').decode())()).hexdigest()
    elif IIIIlllIIIlIIIllIl == 'SHA1':
        return IIIllIIIllIIII(llllllllllllllI(lIllIIllIllIlIllII, llllllllllllllI(lllllllllllIlll, 'fromhex')('656e636f6465').decode())()).hexdigest()
    elif IIIIlllIIIlIIIllIl == 'SHA224':
        return lIIllIIIlllIII(llllllllllllllI(lIllIIllIllIlIllII, llllllllllllllI(lllllllllllIlll, 'fromhex')('656e636f6465').decode())()).hexdigest()
    elif IIIIlllIIIlIIIllIl == 'SHA256':
        return IlIIIIllllIIII(llllllllllllllI(lIllIIllIllIlIllII, llllllllllllllI(lllllllllllIlll, 'fromhex')('656e636f6465').decode())()).hexdigest()
    elif IIIIlllIIIlIIIllIl == 'SHA384':
        return lIlIlIllIlIlII(llllllllllllllI(lIllIIllIllIlIllII, llllllllllllllI(lllllllllllIlll, 'fromhex')('656e636f6465').decode())()).hexdigest()
    elif IIIIlllIIIlIIIllIl == 'SHA512':
        return llllllllllIIll(llllllllllllllI(lIllIIllIllIlIllII, llllllllllllllI(lllllllllllIlll, 'fromhex')('656e636f6465').decode())()).hexdigest()
    elif IIIIlllIIIlIIIllIl == 'BLAKE2b':
        return llIIIIIllllIIl(llllllllllllllI(lIllIIllIllIlIllII, llllllllllllllI(lllllllllllIlll, 'fromhex')('656e636f6465').decode())()).hexdigest()
    elif IIIIlllIIIlIIIllIl == 'BLAKE2s':
        return lllIIlIlIllIll(llllllllllllllI(lIllIIllIllIlIllII, llllllllllllllI(lllllllllllIlll, 'fromhex')('656e636f6465').decode())()).hexdigest()
    elif IIIIlllIIIlIIIllIl == 'BLAKE3':
        return IIIIIIlIlIIllI(llllllllllllllI(lIllIIllIllIlIllII, llllllllllllllI(lllllllllllIlll, 'fromhex')('656e636f6465').decode())()).hexdigest()

def lIlllIlIlIlIllllII(lIIIIlIllIIllIllII, lIIllIlIllIllIIllI, IIIIlllIIIlIIIllIl, lllIlIIIIllIlIllIl):
    with llllllllllllIlI(lIIllIlIllIllIIllI, 'r', encoding='utf-8', errors='ignore') as IlllIllIIIlIllllll:
        lIIIIlIlIIIIlIIIII = llllllllllllllI(IlllIllIIIlIllllll.read(), llllllllllllllI(lllllllllllIlll, 'fromhex')('73706c69746c696e6573').decode())()

    def llllIlIlIlIlIlIIll(lIllIIllIllIlIllII):
        if IllIIlIlIIIlIllllI(lIllIIllIllIlIllII, IIIIlllIIIlIIIllIl) == lIIIIlIllIIllIllII:
            lllllllllllllIl(f'Hash cracked! The word is: {lIllIIllIllIlIllII}')
            return llllllllllllIII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
        return llllllllllllIII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
    with concurrent.futures.ThreadPoolExecutor(max_workers=lllIlIIIIllIlIllIl) as IIIIIlIIIlllIIIIII:
        lIIlIllIIllllIIIlI = lllllllllllIllI(IIIIIlIIIlllIIIIII.map(llllIlIlIlIlIlIIll, lIIIIlIlIIIIlIIIII))
        if lllllllllllllll(lIIlIllIIllllIIIlI):
            return llllllllllllIII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
        else:
            lllllllllllllIl('Hash tidak ditemukan dalam wordlist.')
            return llllllllllllIII(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)

def IlIIIlIlIlllIlllll():
    llIlIlIllllIIIlIlI = IIIIlIlIIIIllI(description='Hash cracking tool made by adjisan.')
    llIlIlIllllIIIlIlI.add_argument('-c', '--crack', type=lllllllllllllII, help='Hash value to crack')
    llIlIlIllllIIIlIlI.add_argument('-w', '--wordlist', type=lllllllllllllII, help='Wordlist file to use')
    llIlIlIllllIIIlIlI.add_argument('-d', '--detect', action='store_true', help='Detect the hash type')
    llIlIlIllllIIIlIlI.add_argument('--t', type=llllllllllllIll, default=1, help='Number of threads to use')
    IIIlllllIllIIlllll = llIlIlIllllIIIlIlI.parse_args()
    if IIIlllllIllIIlllll.crack:
        lIIIIlIllIIllIllII = IIIlllllIllIIlllll.crack
        if IIIlllllIllIIlllll.detect:
            IIIIlllIIIlIIIllIl = lIllllIIllIlIlIlIl(lIIIIlIllIIllIllII)
            lllllllllllllIl(f'Detected hash type: {IIIIlllIIIlIIIllIl}')
        else:
            IIIIlllIIIlIIIllIl = llllllllllllllI(lllllllllllIlII('Masukkan jenis hash (MD5/SHA1/SHA224/SHA256/SHA384/SHA512/BLAKE2b/BLAKE2s/BLAKE3): '), llllllllllllllI(lllllllllllIlll, 'fromhex')('7570706572').decode())()
        if IIIlllllIllIIlllll.lIIllIlIllIllIIllI and lIIllIIIlIIlll(IIIlllllIllIIlllll.lIIllIlIllIllIIllI):
            lllllllllllllIl(f'Cracking hash {lIIIIlIllIIllIllII} menggunakan {IIIlllllIllIIlllll.lIIllIlIllIllIIllI} dengan {IIIlllllIllIIlllll.t} thread...')
            lIlllIlIlIlIllllII(lIIIIlIllIIllIllII, IIIlllllIllIIlllll.lIIllIlIllIllIIllI, IIIIlllIIIlIIIllIl, IIIlllllIllIIlllll.t)
        else:
            lllllllllllllIl('Wordlist tidak ditemukan atau tidak diberikan.')
    else:
        llIlIlIllllIIIlIlI.print_help()
if llllllllllllIIl == '__main__':
    IlIIIlIlIlllIlllll()
