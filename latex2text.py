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
    S = r'''Not much research literature focuses on emergency call systems. 
RFC 5096~\cite{RFC5069} summarized the security threats that emergency call systems might encounter in a conceptual manner. Those threats include leakage and falsification of location and personal information, as well as abuse of anonymity and priority privileges. 
% However, no actual attack or defense approaches are discussed in it.
The chance of the DDoS attack on 911 services by leveraging the anonymity privilege has been mentioned in \cite{guri_911DDoS, onofrei2010_DDoS_911}. 
% Guri \textit{et al.} estimated that, with 6,000 bots, 911 services in a state can be blocked for a whole day \cite{guri_911DDoS}.
Based on the estimation of~\cite{guri_911DDoS}, with 6,000 bots, 911 emergency services in a U.S. state can be blocked for a whole day.
Rebahi \textit{et al.}~\cite{fokus_attack} proposed an attack in current 3GPP's scheme, that an adversary can impersonate PSAPs. '''
    print(parse(S))