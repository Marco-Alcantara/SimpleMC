"""
This module processes the samples from a nested sampler and prints, saves chains in a text file
and creates a param file.
"""
# from simplemc.tools.Simple_Plots import Simple_plots
from simplemc import logger
from simplemc.cosmo.Derivedparam import AllDerived
import sys
import os.path as path
import numpy as np
import re
import scipy as sp


class PostProcessing:
    """
    In this class we...
    """

    def __init__(self, list_result, paramList, filename, \
                 skip=0.1, engine='dynesty', addDerived=True, loglike=None):
        self.analyzername = list_result[0]
        self.result = list_result[1]
        self.paramList = paramList
        self.filename = filename
        self.args = []
        self.list_result = list_result
        self.skip = skip
        self.engine = engine
        self.derived = addDerived
        self.loglike = loglike
        if self.derived:
            self.AD = AllDerived()

        for i in range(2, len(self.list_result)):
            self.args.append(self.list_result[i])

    def saveNestedChain(self):
        """
        This generates an output Simple(cosmo)MC style for dynesty Samplers.

        """
        if path.isfile(self.filename + '_1.txt'):
            logger.critical("Output file exists! Please choose another"
                            " name or move the existing file.")
            sys.exit(1)
        else:
            f = open(self.filename + '_1.txt', 'w+')
        if self.engine == 'dynesty':
            weights = np.exp(self.result['logwt'] - self.result['logz'][-1])

            postsamples = self.result.samples

            logger.info('\n Number of posterior samples is {}'.format(postsamples.shape[0]))

            for i, sample in enumerate(postsamples):
                strweights = str(weights[i])
                strlogl = str(self.result['logl'][i])
                strsamples = str(sample).lstrip('[').rstrip(']')
                row = strweights + ' ' + strlogl + ' ' + strsamples  # + strOLambda
                nrow = " ".join(row.split())
                if self.derived:
                    for pd in self.AD.listDerived(self.loglike):
                        nrow += " " + str(pd.value)
                f.write("{}\n".format(nrow))

        elif self.engine == 'nestle':
            for i in range(len(self.result.samples)):
                strweights = str(self.result.weights[i]).lstrip('[').rstrip(']')
                strlogl = str(-1 * self.result.logl[i]).lstrip('[').rstrip(']')
                strsamples = str(self.result.samples[i]).lstrip('[').rstrip(']')
                row = strweights + ' ' + strlogl + ' ' + strsamples
                nrow = " ".join(row.split())
                if self.derived:
                    for pd in self.AD.listDerived(self.loglike):
                        nrow = "{} {}".format(nrow, pd.value)
                f.write(nrow + '\n')
        f.close()

    # AJUSTAR!
    def saveEmceeSamples(self):
        dims = len(self.paramList)
        # postsamples = self.result.chain[:, self.skip:, :].reshape((-1, dims))
        tau = self.result.get_autocorr_time()
        logger.info("Autocorrelation time: {}".format(tau))
        tau = np.mean(tau)
        burnin = int(0.5 * np.max(tau))
        thin = int(0.5 * np.min(tau))
        f = open(self.filename + '.txt', 'w+')
        logprobs = self.result.get_log_prob(discard=burnin, flat=True, thin=thin)
        flat_log_prior_samps = self.result.get_blobs(flat=True)
        postsamples = self.result.get_chain(discard=burnin, flat=True, thin=thin)

        for i, row in enumerate(postsamples):
            strsamples = str(row).lstrip('[').rstrip(']')
            # strsamples = "{} {} {}\n".format(1, -2 * (logprobs[i] - flat_log_prior_samps[i]), strsamples)
            strsamples = "{} {} {}\n".format(1, -2 * (logprobs[i]), strsamples)
            strsamples = re.sub(' +', ' ', strsamples)
            strsamples = re.sub('\n ', ' ', strsamples)
            if self.derived:
                for pd in self.AD.listDerived(self.loglike):
                    strsamples = "{} {}".format(strsamples, pd.value)
            f.write(strsamples)
        f.close()

    def paramFiles(self):
        """
        This method writes the .paramnames file with theirs LaTeX names.

        Parameters:

        T:          T is an instance of ParseModel(model)
        L:          L is an instance of ParseDataset(datasets)

        """
        cpars = self.loglike.freeParameters()
        parfile = self.filename + ".paramnames"

        if (path.isfile(parfile)):
            logger.info("Existing parameters file!")

        fpar = open(parfile, 'w')
        for p in cpars:
            fpar.write(p.name + "\t\t\t" + p.Ltxname + "\n")
        if self.derived:
            for pd in self.AD.list:
                fpar.write(pd.name + "\t\t\t" + pd.Ltxname + "\n")

    def writeSummary(self, time, *args):
        if self.analyzername == 'genetic':
            sys.exit(1)
        file = open(self.filename + "_Summary" + ".txt", 'w')
        file.write('SUMMARY\n-------\n')

        for item in self.args:
            if type(item) is list:
                for element in item:
                    if element is not None:
                        file.write(str(element) + '\n')
            else:
                if item is not None:
                    file.write(str(item) + '\n')

        for item in args:
            if type(item) is list:
                for element in item:
                    if element is not None:
                        file.write(str(element) + '\n')
            else:
                if item is not None:
                    file.write(str(item) + '\n')

        if self.engine =='dynesty' and self.analyzername == 'nested':
            file.write("nlive: {:d}\nniter: {:d}\nncall: {:d}\n"
                       "eff(%): {:6.3f}\nlogz: "
                       "{:6.3f} +/- {:6.3f}".format(self.result.nlive, self.result.niter,
                                               sum(self.result.ncall), self.result.eff,
                                               self.result.logz[-1], self.result.logzerr[-1]))

        logger.info("\nElapsed time: {:.3f} minutes = {:.3f} seconds".format(time / 60, time))
        file.write('\nElapsed time: {:.3f} minutes = {:.3f} seconds \n'.format(time / 60, time))
        file.close()

    def getdistAnalyzer(self, cov=False):
        from getdist import mcsamples

        mcsamplefile = mcsamples.loadMCSamples(self.filename, settings={'ignore_rows': self.skip})

        if cov:
            cov = mcsamplefile.cov(pars=self.paramList)
            np.savetxt(self.filename + '_' + 'cov.txt', cov)
            logger.info("Covariance matrix:\n")
            logger.info(cov)
            logger.info("\n")

        means = mcsamplefile.getMeans()

        stddev = mcsamplefile.std(self.paramList)

        summaryResults = []

        for i, param in enumerate(self.paramList):
            logger.info(self.paramList[i] + " : " + str(round(means[i], 4)) + \
                        "+/-" + str(round(stddev[i], 4)))
            summaryResults.append(self.paramList[i] + " : " + str(round(means[i], 4)) + \
                                  "+/-" + str(round(stddev[i], 4)))
        return summaryResults
