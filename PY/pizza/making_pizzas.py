#8-16
import pizza
pizza.make_pizza2(16,'pepperoni')

#8-17
from pizza import make_pizza2
make_pizza2(16,'pepperoni')

from pizza import make_pizza2 as fn
fn(16,'pepperoni')

import pizza as mn
mn.make_pizza2(16,'pepperoni')

from pizza import *
make_pizza2(16,'pepperoni')