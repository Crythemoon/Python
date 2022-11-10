def calc_tax(amount, tax_rate):
    tax = amount * tax_rate
    return tax

def main():
    tax = calc_tax(85.0, .05)
    print("Tax:", tax)

if __name__ == "__main__":
    main()

