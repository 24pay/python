from Signer24pay import Signer24pay

signer = Signer24pay("demoOMED", "1234567812345678123456781234567812345678123456781234567812345678")

print(signer.sign("Compute Test Sign").decode("utf8"))
# with default params will print out 0C4F8AAEE7729C869653CF3BB3F4A621
