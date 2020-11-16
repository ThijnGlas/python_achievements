import math

trees = 333
ApplePerTree = 146

shadedTrees = trees * 1
sunnyTrees  = trees / 3 *2

shadeOutputModifier = 80

sunnyTreeOutput   = 1 * 146
shadedTreeOutput  = 1 * 146 / 100 * 80

sunnyOutput         = sunnyTrees * sunnyTreeOutput
shadedOutput        = shadedTrees * shadedTreeOutput
totalOutput         = sunnyOutput + shadedOutput

owners              = 4

eatCount            = totalOutput % owners
sellableOutput      = totalOutput - eatCount
cut                 = sellableOutput / owners

print(cut)
