import re
from typing import *



def parse(S: str):
    # % - \n
    S = re.sub(r'\\%', '', S)
    S = re.sub(r'%.*?\n', '', S)

    # ~ -> _\
    S = re.sub(r'~', ' ', S)

    S = re.sub(r'\$.*?\$', 'P', S)

    # \ref{?} -> 1
    S = re.sub(r'\\ref\{.*?\}', '1', S)

    # \cite{} -> [1]
    # S = re.sub(r'\\cite\{.*?\}', '[1]', S)
    S = re.sub(r' \\cite\{.*?\}', '', S)
    S = re.sub(r'\\cite\{.*?\}', '', S)

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
    S = r'''
Cyber threats emanate not only from tenacious attackers outside the data center but also other insidious entities sharing infrastructure within the same data center. 
Due to lack of encryption on internal communication, early-stage data centers exposed extra attacking surfaces to adversaries, leading to several publicized security disasters \cite{solarwinds,target}. 
%Early-stage data centers expose extra attacking surfaces to adversaries with their encryption surrender policy of internal communication. 
Consequently, the zero trust security model came into being.
% was born to fix this issue. 
In the zero trust model, no entities should trust each other by default; hence authentication and encryption are always desired. 
% Providing network transmission data encryption within data centers has become the current consensus of the best practices for cloud computing
% The current best practices dedicate all connections to be encrypted by TLS for security~\cite{aws-security}.
This model has gained popularity in most cloud computing paradigms, such as IaaS and newly-emerging microservices, which dedicates TLS encryption to all connections to be the best practice
'''
    print(parse(S))