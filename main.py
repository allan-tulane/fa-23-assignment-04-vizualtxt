import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
    
    if (S, T) in MED:
      return MED[(S, T)]
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    elif (S[0] == T[0]):
      MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
      return MED[(S, T)]
    else:
      MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))
      return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
      return MED[(S,T)]
    elif (S == ""):
      MED[(S, T)] = (len(T), ("-"*len(T), T))
    elif T == "":
      MED[(S, T)] = (len(S), ("-"*len(S), S))
    else:
      if S[0] == T[0]:
        MEDhold = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = (MEDhold[0], (S[0] + MEDhold[1][0], T[0] + MEDhold[1][1]))
      else: 
        insert = fast_align_MED(S, T[1:], MED)
        delete = fast_align_MED(S[1:], T, MED)
        #substitute = fast_align_MED(S[:-1], T, MED)
        if insert[0] <= delete[0] and insert[0] <= substitute[0]:
          MED[(S, T)] = (1 + insert[0], ('-' + insert[1][0], T[0] + insert[1][1]))
        elif delete[0] <= insert[0] and delete[0] <= substitute[0]:
          MED[(S, T)] = (1 + delete[0], (S[0] + delete[1][0], '-' + delete[1][1]))
        #else: 
        #  MED[(S, T)] = (substitute[0] + 1, (S[0] + substitute[1][0], T[0] + substitute[1][1]))
    return MED[(S, T)]
        

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)

# there is some error in the alignment function, and it nearly matches the test cases.. unsure what to change but it's 99% there
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        print(fast_align_MED(S, T))
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
print(fast_align_MED("kookaburra", "kookybird"))