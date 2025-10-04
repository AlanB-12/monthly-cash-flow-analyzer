print()

logo = '''
███╗   ███╗ ██████╗ ███╗   ██╗████████╗██╗  ██╗██╗  ██╗   ██╗     ██████╗ █████╗ ███████╗██╗  ██╗      
████╗ ████║██╔═══██╗████╗  ██║╚══██╔══╝██║  ██║██║  ╚██╗ ██╔╝    ██╔════╝██╔══██╗██╔════╝██║  ██║      
██╔████╔██║██║   ██║██╔██╗ ██║   ██║   ███████║██║   ╚████╔╝     ██║     ███████║███████╗███████║      
██║╚██╔╝██║██║   ██║██║╚██╗██║   ██║   ██╔══██║██║    ╚██╔╝      ██║     ██╔══██║╚════██║██╔══██║      
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║   ██║   ██║  ██║███████╗██║       ╚██████╗██║  ██║███████║██║  ██║      
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      
███████╗██╗      ██████╗ ██╗    ██╗     █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
██╔════╝██║     ██╔═══██╗██║    ██║    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
█████╗  ██║     ██║   ██║██║ █╗ ██║    ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
██╔══╝  ██║     ██║   ██║██║███╗██║    ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
██║     ███████╗╚██████╔╝╚███╔███╔╝    ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
'''

print(logo)

income = float(input("\nEnter your monthly income : $"))

print("\n--- MONTHLY EXPENSES ---\n")

rent = float(input("Enter your rent amount : $"))
groceries = float(input("Enter your groceries amount : $"))
electricity = float(input("Enter your electricity bill amount : $"))
maintenance = float(input("Enter your maintenance amount : $")) 
gas = float(input("Enter your gas bill amount: $"))

expenses = rent + groceries + electricity + maintenance + gas

print(f"\nMonthly Income = ${income}")
print(f"Total Monthly Expenses = ${expenses}")

cash_flow = income - expenses
print(f"\nNet Cash Flow = ${cash_flow}")

if cash_flow>0:
    print("\nWell done! Positive Cash Flow.\n")
else:
    print("\nWarning! Negative Cash Flow. Review your expenses.\ns")