#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install mrjob')


# In[ ]:


from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordCount(MRJob):
    #mapper
    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1
    #combiner       
    def combiner(self, word, counts):
        yield word, sum(counts)
    #reducer 
    def reducer(self, word, counts):
        yield word, sum(counts)


if __name__ == '__main__':
    MRWordCount.run()

