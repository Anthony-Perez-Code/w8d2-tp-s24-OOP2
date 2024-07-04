## w8d2-tp-s24-OOP2

A Python script that exhibits class inheritance and polymorphism.

# Parent Class:

## Shape

The Shape class creates establishes the attributes that will be shared among all shapes.

### Attributes

The Shape class defines the self.\_\_color attribute, which is shared by all shapes.

### Methods

- \_\_init\_\_(): establishes the self.\_\_color attribute and keeps track of all created instances by appending each instance to a class-level attribute called "all", which is a list.
- \_\_repr\_\_(): establishes how instances are represented when printed. In this script, printing an instance results in a f-string that contains the instance's type, perimeter, and area.
- get_color(): returns an instance's color. Since self.\_\_color is private, it can only be accessed through methods.
- set_color(): changes an instance's color. Since self.\_\_color is private, it can only be accessed through methods.

# Child Classes:

## Circle

### Attributes

The Circle class defines the self.\_\_radius attribute.

### Methods

- \_\_init\_\_(): calls on parent \_\_init\_\_() method to establish self.\_\_color, then establishes the self.\_\_radius attribute.
- get_radius(): returns an instance's radius. Since self.\_\_radius is private, it can only be accessed through methods.
- set_radius(): changes an instance's radius. Since self.\_\_radius is private, it can only be accessed through methods.
- calculate_area(): returns the area of circle by calling math.pi and self.\_\_radius and evaluating math.pi\*self.\_\_radius\*\*2.
- calculate_perimeter(): returns the circumference of circle by calling math.pi and self.\_\_radius and evaluating 2\*math.pi\*self.\_\_radius.

## Rectangle

### Attributes

The Rectangle class defines the self.\_\_length and self.\_\_width attributes.

### Methods

- \_\_init\_\_(): calls on parent \_\_init\_\_() method to establish self.\_\_color, then establishes the self.\_\_length and self.\_\_width attributes.
- get_length(): returns an instance's length. Since self.\_\_length is private, it can only be accessed through methods.
- set_length(): changes an instance's length. Since self.\_\_length is private, it can only be accessed through methods.
- get_width(): returns an instance's width. Since self.\_\_width is private, it can only be accessed through methods.
- set_width(): changes an instance's width. Since self.\_\_width is private, it can only be accessed through methods.
- calculate_area(): returns the area of rectangle by calling on self.\_\_length and self.\_\_width and evaluating self.\_\_length\*self.\_\_width.
  -calculate_perimeter(): returns the perimeter of rectangle by calling on self.\_\_length and self.\_\_width and evaluating 2\*self.\_\_length + 2\*self.\_\_width.

## Triangle

### Attributes

The triangle class define self.\_\_side1, self.\_\_side2, and self.\_\_side3 attributes.

### Methods

- \_\_init\_\_(): calls on parent \_\_init\_\_() method to establish self.\_\_color, then establishes the self.\_\_side1, self.\_\_side2, and self.\_\_side3 attributes.
- get_length(): returns an instance's side lengths. Since self.\_\_side1, self.\_\_side2, and self.\_\_side3 are private, they can only be accessed through methods.
- set_length(): changes an instance's side lengths. Since self.\_\_side1, self.\_\_side2, and self.\_\_side3 are private, they can only be accessed through methods.
- calculate*area(): returns the area of triangle by call on self.\_\_side1, self.\_\_side2, self.\_\_side3, and self.calculate_perimeter() and evaluating math.sqrt(s * (s - self.\_\_side1) \_ (s - self.\_\_side2) \* (s - self.\_\_side3)), where s = .5\*self.calculate_perimeter().
- calculate_perimeter(): returns the perimeter of the triangle by calling on self.\_\_side1, self.\_\_side2, and self.\_\_side3 and evaluating self.\_\_side1 + self.\_\_side2 + self.\_\_side3.
