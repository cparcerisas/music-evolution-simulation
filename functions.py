import random
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('svg', 'pdf')
from scipy.stats import beta
from scipy.special import logsumexp
from math import log, log1p, exp



def wta(items):
    maxweight = max(items)
    candidates = []
    for i in range(len(items)):
        if items[i] == maxweight:
            candidates.append(i)
    return random.choice(candidates)


def ca_monte(speaker_system, hearer_system, trials):
    total = 0.
    accumulator = []
    for n in range(trials):
        total += communicate(speaker_system, hearer_system, 
                            random.randrange(len(speaker_system)))
        accumulator.append(total / (n + 1))
    return accumulator


def mutate(system):
    for row_i in range(len(system)):
        for column_i in range(len(system[0])):
            if random.random() < mutation_rate:
                system[row_i][column_i] = random.randint(0, mutation_max)


def pick_parent(population, sum_f):
    accumulator = 0
    r = random.uniform(0, sum_f)
    for agent in population:
        accumulator += fitness(agent)
        if r < accumulator:
            return agent


def log_subtract(x,y):
    """ Substract logarithmic numbers """
    return x + log1p(-exp(y - x))


def normalize_probs(probs):
    """ Normalize probabilities """
    total = sum(probs) #calculates the summed log probabilities
    normedprobs = []
    for p in probs:
        normedprobs.append(p / total) #normalise - subtracting in the log domain
                                      #equivalent to dividing in the normal domain
    return normedprobs


def normalize_logprobs(logprobs):
    """ Normalize Logarithmic probabilities """
    logtotal = logsumexp(logprobs) #calculates the summed log probabilities
    normedlogs = []
    for logp in logprobs:
        normedlogs.append(logp - logtotal) #normalise - subtracting in the log domain
                                           #equivalent to dividing in the normal domain
    return normedlogs
 

def log_roulette_wheel(normedlogs):
    """ Given a normalized logarithmic distribution, get a random value """
    r = log(random.random()) #generate a random number between 0 and 1, then convert to log
    accumulator = normedlogs[0]
    for i in range(len(normedlogs)):
        if r < accumulator:
            return i
        accumulator = logsumexp([accumulator, normedlogs[i + 1]])


def calculate_prior(alpha):
    """ Calculate prior distribution given an alpha """
    logprior = []
    for pW1 in possible_pW1:
        logprior.append(beta.pdf(pW1, alpha, alpha)) 
    return normalize_probs(logprior)


def calculate_logprior(alpha):
    """ Calculate logarithmic prior distribution given an alpha """
    logprior = []
    for pW1 in possible_pW1:
        logprior.append(beta.logpdf(pW1, alpha, alpha)) 
    return normalize_logprobs(logprior) 


def likelihood(data, logpW1):
    """ Calculate the likelihood of a data given a probability distr """
    logpW0 = log_subtract(log(1), logpW1) #probability of w0 is 1-prob of w1
    logprobs = [logpW0, logpW1]
    loglikelihoods = []
    for d in data:
        loglikelihood_this_item = logprobs[d] #d will be either 0 or 1, 
                                              #so can use as index
        loglikelihoods.append(loglikelihood_this_item)
    return sum(loglikelihoods) #summing log probabilities = 
                               #multiply non-log probabilities
    

def posterior(data, prior):
    """ Given data and a prior, calculate the posterior """
    posterior_logprobs = []
    for i in range(len(possible_logpW1)):
        logpW1 = possible_logpW1[i] 
        logp_h = prior[i] #prior probability of this pW1
        logp_d = likelihood(data, logpW1) #likelihood of data given this pW1
        posterior_logprobs.append(logp_h + logp_d) #adding logs = 
                                                   #multiplying non-logs
    return normalize_logprobs(posterior_logprobs) 


def iterate(alpha, n_productions, starting_count_w1, generations):
    prior = calculate_logprior(alpha)
    pW1_accumulator = []
    data_accumulator = []
    data = [1] * starting_count_w1 + [0] * (n_productions - starting_count_w1)
    for generation in range(generations):
        logpW1 = learn(data, prior)
        data = produce(logpW1, n_productions)
        pW1_accumulator.append(exp(logpW1))
        data_accumulator.append(sum(data))
    return pW1_accumulator, data_accumulator


def prior(language):
    for i in range(len(priors)):
        if languages[i] == language:
            return priors[i]


def update_posterior(posterior, meaning, signal):
    in_language = log(1 - noise)
    out_of_language = log(noise / (len(signals) - 1))
    new_posterior = []
    for i in range(len(posterior)):
        if (meaning, signal) in languages[i]:
            new_posterior.append(posterior[i] + in_language)
        else:
            new_posterior.append(posterior[i] + out_of_language)
    return normalize_logprobs(new_posterior)


def sample(posterior):
    return languages[log_roulette_wheel(posterior)]
