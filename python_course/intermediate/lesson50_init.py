# __init__ is used to make Python think the package is a module importing things
# inside the package.
# It's really useful.
import lesson50_package
print(lesson50_package.double(15))
print(lesson50_package.modules_sum(20, 30))