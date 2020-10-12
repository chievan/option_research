from pricing import black_scholes

if __name__ == "__main__":
    s, k, r, t, v, cp = 2027.0, 2000, 0.03, 58/365, 0.25, -1
    price, delta, gamma, theta, vega = black_scholes.calculate_greeks(
        s, k, r, t, v, cp)
    print(price, delta, gamma, theta, vega)
