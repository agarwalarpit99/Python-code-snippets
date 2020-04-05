class Account:
	def __init__(self,account_no,account_name,account_balance):

		self.account_no=account_no
		self.account_name=account_name
		self.account_balance=account_balance
	def depositAmnt(self,value):
		self.account_balance+=value

	def withdrawAmnt(self,value):
		self.account_balance-=value
		if self.account_balance<1000:
			self.account_balance+=value
			return 1
		else:
			return 0
if __name__=='__main__':
	account_no=int(input())
	account_name=input()
	account_balance=int(input())
	dep=int(input())
	wit=int(input())
	a=Account(account_no,account_name,account_balance)
	a.depositAmnt(dep)
	final=a.withdrawAmnt(wit)
	print(a.account_balance)
	if final==1:
		print('INSUFFICIENT BALANCE FOR WIDTHDRAWL')
