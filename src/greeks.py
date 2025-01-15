import numpy as np
from scipy.stats import norm

def calculate_greeks(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta_call = norm.cdf(d1)
    delta_put = delta_call - 1
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta_call = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2))
    theta_put = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    rho_call = K * T * np.exp(-r * T) * norm.cdf(d2)
    rho_put = -K * T * np.exp(-r * T) * norm.cdf(-d2)

    return {
        "Delta (Call)": delta_call,
        "Delta (Put)": delta_put,
        "Gamma": gamma,
        "Theta (Call)": theta_call,
        "Theta (Put)": theta_put,
        "Vega": vega,
        "Rho (Call)": rho_call,
        "Rho (Put)": rho_put,
    }

if __name__ == "__main__":
    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2

    greeks = calculate_greeks(S, K, T, r, sigma)
    for key, value in greeks.items():
        print(f"{key}: {value:.4f}")
