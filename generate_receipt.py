from reportlab.pdfgen import canvas
from datetime import datetime
import os
import platform

def generate_receipt(customer_name, items, total_amount, receipt_number):
    filename = f"Receipt_{receipt_number}.pdf"
    pdf = canvas.Canvas(filename)


  
    pdf.setTitle("Payment Receipt")
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(200, 800, "Payment Receipt")

    
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 770, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    pdf.drawString(50, 750, f"Receipt No: {receipt_number}")
    pdf.drawString(50, 730, f"Customer Name: {customer_name}")

    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 700, "Item")
    pdf.drawString(250, 700, "Qty")
    pdf.drawString(350, 700, "Price")

   
    y = 680
    pdf.setFont("Helvetica", 12)
    for item in items:
        pdf.drawString(50, y, item['name'])
        pdf.drawString(250, y, str(item['qty']))
        pdf.drawString(350, y, f"₹ {item['price']:.2f}")
        y -= 20

   
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y - 20, f"Total Amount: ₹ {total_amount:.2f}")

    
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(50, y - 50, "Thank you for your purchase!")

    
    pdf.save()
    print(f"\n Receipt saved as {filename}")

   
    if platform.system() == "Windows":
        os.startfile(filename)
    elif platform.system() == "Darwin":
        os.system(f"open {filename}")
    elif platform.system() == "Linux":
        os.system(f"xdg-open {filename}")

def print_receipt_to_terminal(customer_name, items, total_amount, receipt_number):
    print("\n" + "=" * 40)
    print(" " * 10 + "Payment Receipt")
    print("=" * 40)
    print(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print(f"Receipt No: {receipt_number}")
    print(f"Customer Name: {customer_name}")
    print("-" * 40)
    print(f"{'Item':20}{'Qty':>5}{'Price':>10}")
    print("-" * 40)
    for item in items:
        print(f"{item['name'][:20]:20}{item['qty']:>5}{item['price']:>10.2f}")
    print("-" * 40)
    print(f"{'Total Amount:':>30} ₹ {total_amount:.2f}")
    print("=" * 40)
    print("Thank you for your purchase!\n")


if __name__ == "__main__":
    num_customers = int(input("How many customers do you want to generate receipts for? "))

    for c in range(num_customers):
        print(f"\n--- Customer {c+1} ---")
        customer = input("Enter customer name: ")
        num_items = int(input("How many items does the customer want to buy? "))
        items = []

        for i in range(num_items):
            print(f"\nEnter details for item {i+1}")
            name = input("Item name: ")
            qty = int(input("Quantity: "))
            price = float(input("Price per item: "))
            items.append({'name': name, 'qty': qty, 'price': price})

        total = sum(item['qty'] * item['price'] for item in items)
        receipt_id = int(datetime.now().strftime('%Y%m%d%H%M%S')) + c  # Ensure unique receipt number

        generate_receipt(customer, items, total, receipt_id)
        print_receipt_to_terminal(customer, items, total, receipt_id)
