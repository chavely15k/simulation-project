import numpy as np

def generate_poisson(lam=5):
    return np.random.poisson(lam)

def generate_geometric(p=0.5):
    return np.random.geometric(p)

def generate_uniform(low=1, high=10):
    return np.random.randint(low, high)

def generate_binomial(n=10, p=0.5):
    return np.random.binomial(n, p)

def generate_exponential(scale=10):
    return round(np.random.exponential(scale))

def generate_normal(loc=0, scale=1):
    return round(np.random.normal(loc, scale))

def generate_beta(a=2, b=5):
    return round(np.random.beta(a, b))

def generate_gamma(shape=2, scale=1):
    return round(np.random.gamma(shape, scale))

distributions = [generate_poisson, generate_geometric, \
    generate_uniform, generate_binomial, generate_exponential, \
    generate_normal, generate_beta, generate_gamma]