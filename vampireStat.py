import numpy as np
import scipy.stats as ss
import pylab as P

import random


# Python < 2.7: from optparse import OptionParser,OptionGroup
from argparse import ArgumentParser
# Python < 2.7: parser = OptionParser(description='Bulabulabula')
parser = ArgumentParser(description='This script answers to the basic question: has the email from the character X been hacked, either by the bad guys or by another character?')

commonOpts = parser.add_argument_group("Common options", "Options common to recursive copy and deletion")
commonOpts.add_argument("-e", "--emailsSent", dest="emails_sent", help="Emails the player has already sent since last LARP session", default='0', type=int)
commonOpts.add_argument("-d", "--defenderDots", dest="defender_dots", help="Dots that the defender character has in the Computers skill", default='0', type=int)
commonOpts.add_argument("-c", "--carefulDefender", dest="careful_defender", help="Whether the defender has been careful in sending emails", action='store_true')
commonOpts.add_argument("-a", "--attackerDots", dest="attacker_dots", help="Dots that the attacker character has in the Computers skill", default='0', type=int)
commonOpts.add_argument("-v", "--verbose",  dest="debug",    help='Activate debug mode (verbose printing)',       action="store_true")

expertOpts = parser.add_argument_group("Expert options", "Options for experts (manipulate basic probabilities")
expertOpts.add_argument("-b", "--baseProbability", dest="base_probability", help="Base probability for an email or thread to be hacked", default='0.4', type=float)
expertOpts.add_argument("-f", "--frequencyMalus", dest="frequency_malus", help="probability malus per-already-sent-email", default='0.03', type=float)

parser.print_help()

args=parser.parse_args()

attacker_coeff = 0.05
defender_coeff = 0.03
if args.careful_defender:
    defender_coeff = 0.05


# TODO: Must also compute a small probability for the defender to realize he has been attacked (modified by the computer skills dots as well)
base_probability = args.base_probability - args.defender_dots*defender_coeff + args.attacker_dots*attacker_coeff + args.emails_sent*args.frequency_malus


gausvar = []
uniformvar = []
for i in range(0,10000):
    gausvar.append(random.gauss(base_probability,0.2))
    k=0
    if random.uniform(0.,1.) > base_probability:
        k=1
    uniformvar.append(k)
P.hist(gausvar, 100)
P.hist(uniformvar, 100)
                


#a = ss.norm.rvs(4, 2, 40)
#P.hist(a, normed=True)
#
#xs = np.linspace(0, 10, 30)
#P.plot(xs, ss.norm.pdf(xs, 4, 2), label='pdf')
#P.plot(xs, ss.norm.cdf(xs, 4, 2), label='cdf')

P.show()
