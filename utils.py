# This function cleans a price string and converts it to a float
# Example: "$45,000.23" → 45000.23 (float)
def clean_price(price_str):
    try:
        # Remove the dollar sign and commas, then convert to a number
        return float(price_str.replace("$", "").replace(",", "").strip())
    except ValueError:
        # If conversion fails (invalid or empty data), return None
        return None
