#!/usr/bin/env python3
"""Offline calculator. All financial assumptions must be supplied by the user or sourced."""
import argparse
import json

def calculate(price, variable_cost, payment_percent, payment_fixed, cac, refund_rate=0):
    if min(price, variable_cost, payment_percent, payment_fixed, cac, refund_rate) < 0:
        raise ValueError("Inputs must be nonnegative")
    if payment_percent > 100 or refund_rate > 1:
        raise ValueError("payment_percent <= 100; refund_rate <= 1")
    revenue = price * (1 - refund_rate)
    fees = price * payment_percent / 100 + payment_fixed
    profit = revenue - variable_cost - fees - cac
    return {"expected_revenue": round(revenue, 2), "fees": round(fees, 2),
            "profit_per_order": round(profit, 2),
            "break_even_cac": round(revenue - variable_cost - fees, 2)}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--price", type=float, required=True)
    p.add_argument("--variable-cost", type=float, required=True)
    p.add_argument("--payment-percent", type=float, default=0)
    p.add_argument("--payment-fixed", type=float, default=0)
    p.add_argument("--cac", type=float, default=0)
    p.add_argument("--refund-rate", type=float, default=0)
    a = p.parse_args()
    print(json.dumps(calculate(a.price, a.variable_cost, a.payment_percent,
                               a.payment_fixed, a.cac, a.refund_rate), indent=2))
