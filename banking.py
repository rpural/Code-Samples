''' From Python Programmers (Beginners)
    and Mike Kerry

Here is a challenge. Write a script using OOP 
to represent a bank with multiple user 
accounts. 

There are 2 classes. One class named Account 
which holds Account Number, Holder Name, and 
Balance. It has methods for deposit and 
withdraw and get balance.

A second class named Bank holds a dictionary
of accounts (key is account number, data is 
Account object). This class has classmethods 
for creating an instance of Account, and for 
listing all accounts with their details.
'''

class Account:
	interest = 0.01
	def __init__(self, acctno, name, balance=0):
		self.acctno = acctno
		self.name = name
		self.balance = float(balance)
		
	def __str__(self):
		return f"{self.acctno}  {self.name}  {self.balance}"
		
	def deposit(self, amt):
		try:
			self.balance += float(amt)
			return self.balance
		except ValueError:
			return None
			
	def withdraw(self, amt):
		try:
			amt = float(amt)
			if amt <= self.balance:
				self.balance -= amt
				return self.balance
			else: return self.balance - amt
		except ValueError:
			return None
			
	def eom(self):
		self.balance += (self.balance * self.interest)
		
	def details(self):
		return (self.acctno, self.name, self.balance)
		
		
class MoneyMarket (Account):
	interest = 0.03
	
	def __init__(self, acctno, name, amt):
		super().__init__(acctno, name, amt)
		
	def __str__(self):
		return f"*  {self.acctno}  {self.name}  {self.balance}"
		
		
class Bank:
	def __init__(self, name):
		self.name = name
		self.accounts = dict()
		
	def account(self, acctno):
		return self.accounts.get(acctno, None)
		
	def addAccount(self, acctno, name, amt):
		if not self.account(acctno):
			newacct = Account(acctno, name, amt)
			self.accounts[acctno] = newacct
			return acctno
		else:
			return None
			
	def addMoneyMarket(self, acctno, name, amt):
		if not self.account(acctno):
			newacct = MoneyMarket(acctno, name, amt)
			self.accounts[acctno] = newacct
			return acctno
		else:
			return None
			
	def eom(self):
		for acct in self.accounts:
			self.accounts[acct].eom()
			
	def __str__(self):
		return self.name
		
	@property
	def assets(self):
		asset = 0.00
		for acct in self.accounts:
			asset += self.accounts[acct].balance
		return asset
		
	@property
	def acctlist(self):
		accts = list()
		for acct in self.accounts.values():
			accts.append(acct)
		return accts
		
		
if __name__ == "__main__":
	acme = Bank("Acme Banking")
	acme.addAccount(123, "Bob", 100)
	acme.addAccount(159, "Sue", 500)
	acme.addMoneyMarket(345, "Sam", 2000)
	print(f"assets for {acme.name} = {acme.assets}.")
	for acct in acme.acctlist:
		print(f"  {acct}")
		
	acme.account(123).withdraw(15.00)
	acme.account(345).deposit(1000)
	print(f"{acme.account(123)}")
	print(f"{acme.account(345)}")
	print(f"assets for {acme.name} = {acme.assets}.\n-----\nafter EOM processing:\n")
	acme.eom()
	print(f"assets for {acme.name} = {acme.assets}.\n")
	for acct in acme.acctlist:
		print(f"  {acct}")
