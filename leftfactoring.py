

EPSILON = "e"
from  trie import  Trie

def leftFactoring(file, outputfile = None):
    productionList = decodeProductionList(file)

    newProductionList = __leftFactoring(productionList)

    encodeProductionList(newProductionList, outputfile)

def __leftFactoring(productionList):
    ans = []
    availableNonterminal = getAvailableNonterminals(productionList)
    for production in productionList:
        subans =leftFactoringEachProduction(production, availableNonterminal)
        ans.extend(subans)

    return ans

def getAvailableNonterminals(productionList):
    availableNonterminasl = set([])

    for i in range(0, 26):
        A = ord('A')
        c = chr(i + A)
        availableNonterminasl.add(c)

    for production in productionList:
        if production.nonterminal in availableNonterminasl:
            availableNonterminasl.remove(production.nonterminal)

    return availableNonterminasl

def leftFactoringEachProduction(production, availableNonterminal):
    ans = []
    longestLength, commonPrefixRights = longestCommonPrefixProductions(production.rightList)

    ## no two or more productions with common prefix
    if longestLength <= 0:
        ans.append(production)

        return ans

    production1, production2 = genNewProduction(production, commonPrefixRights, longestLength, availableNonterminal)

    ans.append(production2)

    subasn = leftFactoringEachProduction(production1, availableNonterminal)

    ans.extend(subasn)

    return ans

def genNewProduction(production, commonPrefixRights, lengthOfCommonPrefix, availableNonterminal):
        newnonterminal = availableNonterminal.pop()

        newProdcution = Production().left(newnonterminal)

        newProdcution.right([right[lengthOfCommonPrefix:] if right[lengthOfCommonPrefix:] != "" else EPSILON for right in commonPrefixRights])

        nonCommonPrefixRights = production.getNonCommonPrefixRights(commonPrefixRights)

        newProdcution2 = Production().left(production.nonterminal).right(nonCommonPrefixRights)\
            .right(commonPrefixRights[0][:lengthOfCommonPrefix] + newProdcution.nonterminal)

        return newProdcution2, newProdcution

def longestCommonPrefixProductions(rightList):
    trie = Trie()
    for right in rightList:
        trie.build(right)

    longest, commonrights = trie.wordsWihtLargestCommonPrefix()
    return (longest, commonrights)


def encodeProductionList(productionList, outputfile= None):
    if outputfile == None:
        outputfile = "./production.out"

    with open(outputfile, "w+") as fd:
        for  production in productionList:
            line =  encodeProduction(production)
            fd.write(line)
            fd.write("\n")


    return

def encodeProduction(production):
    left = production.nonterminal
    right = "|".join(production.rightList)

    return  left +  "->" + right


def decodeProductionList(file):

    ans = []

    with open(file) as fd:
        lines = fd.readlines()

        for line in lines:
            if line != "":
                production = decodeProduction(line)
                ans.append(production)

    return  ans

def decodeProduction(line):
    production_rule = line.split("->")
    left, right_rule = production_rule[0], production_rule[1]

    production = Production().left(left)

    rights = right_rule.split("|")

    production.right([right.strip() for right in rights])

    return production

class Production():
    def __init__(self):
        self.nonterminal = None

        self.rightList = []

    def left(self, nonterminal):
        self.nonterminal = nonterminal
        return self

    def right(self, rightDerivations):
        if isinstance(rightDerivations, list):
            self.rightList.extend(rightDerivations)
        else:
            self.rightList.append(rightDerivations)

        return self

    def getNonCommonPrefixRights(self, commonPrefixRights):
        return [right for right in self.rightList if right not in commonPrefixRights]

