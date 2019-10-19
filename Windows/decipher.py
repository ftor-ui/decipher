from sys import argv, exit
import os
import hashlib

def DecipherOneWord(hashes):
	for hash1 in hashes:
		hash1 = hash1.replace("\n","")
		if argv[1] == "md5":	
			if hash1 == hashlib.md5(argv[3].encode('utf-8')).hexdigest():
				yield hash1 + ": " + argv[3]
				exit(0)
		if argv[1] == "sha512":
			if hash1 == hashlib.sha512(argv[3].encode('utf-8')).hexdigest():
				yield hash1 + ": " + argv[3]
				exit(0)
		if argv[1] == "sha224":	
			if hash1 == hashlib.sha224(argv[3].encode('utf-8')).hexdigest():
				yield hash1 + ": " + argv[3]
				exit(0)
		if argv[1] == "sha256":	
			if hash1 == hashlib.sha256(argv[3].encode('utf-8')).hexdigest():
				yield hash1 + ": " + argv[3]
				exit(0)
		if argv[1] == "sha384":	
			if hash1 == hashlib.sha384(argv[3].encode('utf-8')).hexdigest():
				yield hash1 + ": " + argv[3]
				exit(0)

def DecipherOneHash(wordlist):
	for word in wordlist:
		word = word.replace("\n","")
		if argv[1] == "md5":	
			if argv[2] == hashlib.md5(word.encode('utf-8')).hexdigest():
				yield argv[2] + ": " + word
				exit(0)
		if argv[1] == "sha512":
			if argv[2] == hashlib.sha512(word.encode('utf-8')).hexdigest():
				yield argv[2] + ": " + word
				exit(0)
		if argv[1] == "sha224":	
			if argv[2] == hashlib.sha224(word.encode('utf-8')).hexdigest():
				yield argv[2] + ": " + word
				exit(0)
		if argv[1] == "sha256":	
			if argv[2] == hashlib.sha256(word.encode('utf-8')).hexdigest():
				yield argv[2] + ": " + word
				exit(0)
		if argv[1] == "sha384":	
			if argv[2] == hashlib.sha384(word.encode('utf-8')).hexdigest():
				yield argv[2] + ": " + word
				exit(0)

def DecipherList(hashlist,wordlist):
	for hash1 in hashlist:
		hash1 = hash1.replace("\n","")
		for word in wordlist:
			word = word.replace("\n","")
			if argv[1] == "md5":	
				if hash1 == hashlib.md5(word.encode('utf-8')).hexdigest():
					yield hash1 + ": " + word
					break
			if argv[1] == "sha512":	
				if hash1 == hashlib.sha512(word.encode('utf-8')).hexdigest():
					yield argv[2] + ": " + word
					break
			if argv[1] == "sha224":	
				if hash1 == hashlib.sha224(word.encode('utf-8')).hexdigest():
					yield argv[2] + ": " + word
					break
			if argv[1] == "sha256":	
				if hash1 == hashlib.sha256(word.encode('utf-8')).hexdigest():
					yield argv[2] + ": " + word
					break
			if argv[1] == "sha384":	
				if hash1 == hashlib.sha384(word.encode('utf-8')).hexdigest():
					yield argv[2] + ": " + word
					break
		wordlist.seek(0)

if len(argv)<4:
	print("Example: decipher [md5/sha512/sha256/sha224/sha384] [hash/list_hash] [word/wordlist]")
	exit(0)
elif os.path.exists(argv[2]) and os.path.exists(argv[3]):
	with open(argv[2],"r",encoding="utf-8") as hashes:
		with open(argv[3],"r",encoding="utf-8") as dictionary:
			for start in DecipherList(hashes,dictionary):
				print(start)
elif os.path.exists(argv[3]):
	with open(argv[3],"r",encoding="utf-8") as dictionary:
			for start in DecipherOneHash(dictionary):
				print(start)
elif os.path.exists(argv[2]):
	with open(argv[2],"r",encoding="utf-8") as hashes:
			for start in DecipherOneWord(hashes):
				print(start)
else:
	if argv[1] == "md5":	
		if argv[2] == hashlib.md5(argv[3].encode('utf-8')).hexdigest():
			print(argv[2] + ": " + argv[3])
			exit(0)
	if argv[1] == "sha512":
		if argv[2] == hashlib.sha512(argv[3].encode('utf-8')).hexdigest():
			print(argv[2] + ": " + argv[3])
			exit(0)
	if argv[1] == "sha224":	
		if argv[2] == hashlib.sha224(argv[3].encode('utf-8')).hexdigest():
			print(argv[2] + ": " + argv[3])
			exit(0)
	if argv[1] == "sha256":	
		if argv[2] == hashlib.sha256(argv[3].encode('utf-8')).hexdigest():
			print(argv[2] + ": " + argv[3])
			exit(0)
	if argv[1] == "sha384":	
		if argv[2] == hashlib.sha384(argv[3].encode('utf-8')).hexdigest():
			print(argv[2] + ": " + argv[3])
			exit(0)
print("--------\nfinished\n--------")
exit(0)
