input_str = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "

input_str = input_str.strip()

key_name = input_str.split('&')

key_name = [d for d in key_name if d != '']

out_str = dict(s.split('=', 1) for s in key_name)
print(out_str)
