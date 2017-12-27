vowels=['a','e','i','o','u','A','E','I','O','U']
class sentence:
	def __init__(self,sent):
		self.sent=sent;

	def revsent(self):
		rev=self.sent.split()[::-1]
		self.revs=' '.join(rev)
		print (self.revs)



	def countv(self):
		cv=0
		for i in range(len(self.sent)):
			if self.sent[i] in vowels:
				cv=cv+1
		return cv
		


s1=sentence("I am here")
s1.countv()


s2=sentence("Hello World")
s2.countv()


s3=sentence("Hello World Bye bye")
s3.countv()


s=[s1,s2,s3]
s.sort(key=lambda x:x.countv(),reverse=True)

print ("Reverse of Strings in Descending order of Number of Vowels:-")
for i in s:
	i.revsent()