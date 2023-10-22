'''In object=oriented programming encapsulation refers to the bunding of data with the methods that operate on
that data, or the restrictiong of direct access to some of an objects components. Encapsulation is used to hide to the
values or state of stuctured data object inside a class, preventing direct access to them by clients in a way that could
expose hidden implementation details or violate state invariance maintained by the methods .
this mechanism is not unique to oop. Implementaions of abstract data types,e.g modules offer a similar form of
encapsulation. The similarityl has been explained by programming language theorists in terms of existential types.

'''
'''
This is one of the main features of object-oriented programming. Encapsulation is very useful when writing large scripts. 
You can encapsulate one part of the script in such a way that it is not affected by any other part, even if the parts have properties of the same name or Use the method.
More simply, encapsulation is a method by which the scope of properties, methods, etc. in a script can be fixed (again, don't think that encapsulation is just encapsulation
of methods/properties with access modifiers. Rather, it's because the data is wrapped in objects that are protected in different ways). , that's encapsulation).access
'''


@property
# Property Decortor = Read-Only Attribute
def name(self):
    return self._name


@name.setter
def name(self, value):
    if len(value) > 10:
        raise Exception("The name is too long")