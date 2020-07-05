import re
from typing import *



def parse(S: str):
    # % - \n
    S = re.sub(r'%.*?\n', '', S)

    # ~ -> _\
    S = re.sub(r'~', ' ', S)

    S = re.sub(r'\$.*?\$', 'P', S)

    # \ref{?} -> 1
    S = re.sub(r'\\ref\{.*?\}', '1', S)

    # \cite{} -> [1]
    S = re.sub(r'\\cite\{.*?\}', '[1]', S)

    # (?) -> -
    S = re.sub(r'\(.*?\)', '', S)
    # \?{ -> -
    S = re.sub(r'\\.*?\{', '', S)
    # } -> -
    S = re.sub(r'\}', '', S)

    # \eg -> e.g.  \ie -> i.e.
    S = re.sub(r'\\eg', 'e.g.', S)
    S = re.sub(r'\\ie', 'i.e.', S)

    # $?$ -> P


    return S

if __name__ == '__main__':
    S = r'''\textcircled{2} \textit{Symbolic Analysis}.
The whole state space may be prohibitively large, especially for those systems involving cryptographic algorithms.
The symbolic analysis employs predefined reduction rules to save efforts in verification. 
% Authentication and key agreement (AKA) is a cryptographic protocol used in 3GPP networks. 
% To check its security, 
A lot of works \cite{3gpp33902, arapinis2012new, basin2018formal5G, cremers2019component} applied modern symbolic provers, like ProVerif~\cite{blanchet2016modeling} and Tamarin~\cite{basin2017symbolically}, on AKA protocols used in 3G, 4G, and 5G. 
Nevertheless, cryptographic related procedures constitute only a small portion of cellular network protocols, and those methods cannot be generalized to other procedures.}

\new{\textcircled{3} \textit{Software Analysis}.
Software analysis aims to directly verify the implementations, as that can save time and efforts of building a model manually. 
% If the software implementation of cellular protocols is available, it would seem attractive to directly perform the formal software analysis, as that can save time and efforts to build a model manually.
}
For instance, Pi \textit{et al.} \cite{tencent2018exploring} extracted binary codes from a Qualcomm baseband and recompiled them to perform static analysis and debugging. Yu \textit{et al.} \cite{yu2019cellscope} ran software model checking on open-source cellular protocol emulators. 
However, one implementation is only a single instance of the protocols, so it can not reflect other implementations. 
\new{
In comparison, our approach is based upon protocols. It targets problems on a higher level and can be adapted to many instances.'''
    print(parse(S))