num_str = "42"
print("Valor original %s %s" % (num_str, str(type(num_str))))
num_str = int(num_str)
print("Como int %d %s" % (num_str, str(type(num_str))))
num_str = float(num_str)
print("Como float %.1f %s" % (num_str, str(type(num_str))))
num_str = bool(num_str)
print("Como bool %s %s" % (num_str, str(type(num_str))))
