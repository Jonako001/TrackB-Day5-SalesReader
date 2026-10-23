import csv

FILE = "sales.csv"

def read_sales():
    total = 0
    top_name = ""
    top_amount = 0
    sales_list = []

    try:
        with open(FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Clean data (remove spaces)
                name = row['name'].strip()
                county = row['county'].strip()
                amount = float(row['amount'].strip())

                sales_list.append(row)
                total += amount

                if amount > top_amount:
                    top_amount = amount
                    top_name = name

    except FileNotFoundError:
        print(f"❌ Error: {FILE} not found. Make sure it's in the same folder.")
        return
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    print("\n🇰🇪 Sales Data Reader - Day 5 Project")
    print("-" * 40)
    print(f"Total Sales Records: {len(sales_list)}")
    print(f"Total Sales Amount: KSH {total:,.2f}")
    print(f"Top Salesperson: {top_name} - KSH {top_amount:,.2f}")
    print("-" * 40)

if __name__ == "__main__":
    read_sales()