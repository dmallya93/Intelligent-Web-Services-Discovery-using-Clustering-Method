import difflib

sm = difflib.SequenceMatcher(None)

sm.set_seq2('activity beach')
#SequenceMatcher computes and caches detailed information
#about the second sequence, so if you want to compare one
#sequence against many sequences, use set_seq2() to set
#the commonly used sequence once and call set_seq1()
#repeatedly, once for each of the other sequences.
# (the doc)

for x in ('activity beach',
          'Social working service',
          'Social ocean',
          'Atlantic ocean',
          'Atlantic and arctic oceans'):
    sm.set_seq1(x)
    print x,sm.ratio()
