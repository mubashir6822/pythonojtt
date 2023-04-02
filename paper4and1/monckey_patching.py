class main_func:
	def og_func():
		print ("og_func() is being called")

def monkey_f():
	print ("monkey_f() is being called")

# replacing address of "og_func" with "monkey_f"
main_func.og_func = monkey_f

# calling og_function "og_func" whose address got replaced with function "monkey_f()"

main_func.og_func()
