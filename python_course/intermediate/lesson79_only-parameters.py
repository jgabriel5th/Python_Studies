# Controlling the keyword arguments and positional arguments quantity in functions.
# *args (unlimited positional arguments)
# **kwargs (unlimited keyword arguments)
# 🟢 Positional-only Parameters (/) - Everything before the bar must
# be❗️ONLY❗️ positional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * alone ❗️DOESN'T ABSORB❗️ values.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
def sumNumber(x, y, /, *, z, **kwargs):
    print(kwargs)
    return x + y + z

print(sumNumber(3, 4, z=10, name='test'))