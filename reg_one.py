import pprint as pp
import re
sample_text = """
[27] Ming Tan et al. “Out-of-Domain Detection for Low-Resource Text Classification Tasks”. In:
Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP- IJCNLP). 2019, pp. 3557–3563.
[28] Ashish Vaswani et al. “Attention is all you need”. In: Proceedings of the 31st International Conference on Neural Information Processing Systems. 2017, pp. 6000–6010.
[29] Saizheng Zhang et al. “Personalizing Dialogue Agents: I have a dog, do you have pets too?” In: Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2018, pp. 2204–2213.
[30] Yizhe Zhang et al. “DIALOGPT: Large-Scale Generative Pre-training for Conversational Response Generation”. In: Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: System Demonstrations. 2020, pp. 270–278.
"""

# https://www.linkedin.com/learning/learning-regular-expressions-2/what-are-regular-expressions?autoplay=true&u=94919786

# regular expressions are patterns of symbols that match text
# some sample engines
# - oddly enough they are just listing languages here.
# online javascript regex approach
# - regex101.com
# - regexpal.com
# - https://regexr.com/


# I guess the ordering would be 0 - 1 , 1 - 2, 2 - 3, 3 - 4.
# though this would assume that it is happening at the start of the string which may not neccessarily be the case. Though for the purpose of this round of learning lets just pull out the four complete references

# dictionary to hold references
ref_dict = {}
# establishing the  instaces of the refs
# here there are four , but further there may be others
testReg = re.compile(r'\[\d*\]')
results = testReg.findall(sample_text)  # returns a list of bracketed references
# extract index locations for each to know where to segement the lines
index_results = [sample_text.index(x) for x in results]
# appending the end point will help extract all references to the end
# though this should be moved, and indexes extracted first to avoid annoying index references
index_results.append(len(sample_text))

print(index_results)

# regex for just pulling out numbers
numRegex = re.compile(r'\d\d')
# take the reference number and use it as a key
# write a loop that takes slices from the string and stores each reference
for iter in range(len(index_results) - 1):
    print(iter)
    start = index_results[iter]
    end = index_results[iter + 1]
    print(start, end)
    # extract key for reference
    num = numRegex.search(results[iter])  # numRegex just looks at the num in the brackets
    key = num.group(0)
    # extract reference as value
    value = sample_text[start:end]
    # assign to reference dictionary
    ref_dict[key] = value


print(pp.pprint(ref_dict))
# g == findall
# i == case insensitve re.I
# m == re.MULTILINE (re.M)
# to combine expressions use the r pipe |
# grep === g/re/p -> globally search for regular expression and print out!

# literal characters
# car == car.

sample = re.compile(r'in:', re.I)
print(sample.findall(sample_text))


'''
# TODO :
1. update print statements to logging statements
2. Update regex to create to further divide text into author/ title/ conference/ pub year / pages
3. Create a class to hold all information
3a. Neaten code by adhering to PEP8 as well as dividing into separate calling and methods class
4. Update with assert statements to make sure that everything is going in as it should
5. expand code to take pages in over saved text 
'''
