# Import libraries/modules
from numpy import sqrt

class Complex:
     """
    A class used to represent a complex number. Each complex number instance
    will have a real and an imaginary component.

    ...

    Args
    ----------
    real : TYPE, optional - Int/Float
            DESCRIPTION. The default is 1. Real component of complex number
    imag : TYPE, optional - Int/Float
        DESCRIPTION. The default is 1. Imaginary component of complex number

    Attributes
    ----------
    real : TYPE, optional - Int/Float
            DESCRIPTION. The default is 1. Real component of complex number
    imag : TYPE, optional - Int/Float
        DESCRIPTION. The default is 1. Imaginary component of complex number

    Methods
    -------
    __str__()
        DESCRIPTION: Override the str magic method to return the real and imaginary parts
                     of the complex number as a string.
    setReal(real)
        DESCRIPTION: Set the value of the real component
    setImag(imag)
        DESCRIPTION: Set the value of the imaginary component
    getImag()
        DESCRIPTION: Get the value of the real component
    getImag()
        DESCRIPTION: Get the value of the imaginary component
    __add__(other)
        DESCRIPTION: Override the add magic method to add two complex numbers
    __sub__(other):
        DESCRIPTION: Override the sub magic method to subtract two complex numbers
    __mul__(other)
        DESCRIPTION: Override the mul magic method to multiply two complex numbers
    __truediv__(other)
        DESCRIPTION: Override the truediv magic method to divide two complex numbers
    __eq__(other)
        DESCRIPTION: Override the eq magic method to determine if two complex numbers are equal
    magnitude()
        DESCRIPTION: Calculate the magnitude or length of a complex number
    conj()
        DESCRIPTION: Calculate the complex conjugate of a complex number
    """
    def __init__(self, real=1, imag=1):
        """

        Parameters
        ----------
        real : TYPE, optional - Int/Float
            DESCRIPTION. The default is 1. Real component of complex number
        imag : TYPE, optional - Int/Float
            DESCRIPTION. The default is 1. Imaginary component of complex number

        Returns
        -------
        None.

        """
        # Initialise real and imaginary components
        self.real = real
        self.imag = imag
        # Initialise magnitude of complex number
        self.magnitude()
        
    def __str__(self):
        """
        Override the str magic method to return the real and imaginary parts
        of the complex number as a string.
        
        ...
        
        Returns
        -------
        str
            DESCRIPTION - Real and imaginary component values of instance 

        """
        # Return complex number as a string
        if self.imag < 0:
            imag = self.imag * -1
            return f'{self.real} - {imag}i'
        else:
            return f'{self.real} + {self.imag}i'
        
    def setReal(self, real):
        """
        Set the value of the real component
        
        ...

        Parameters
        ----------
        real : TYPE - Float/Int
            DESCRIPTION - Real component of complex number

        Returns
        -------
        None.

        """
        # Set real component value
        self.real = real
    
    def getReal(self):
        """
        Get the value of the real component
        
        ...
        
        Returns
        -------
        TYPE - Float/Int
            DESCRIPTION - Real component of complex number

        """
        # Return real component value
        return self.real
    
    def setImag(self, imag):
        """
        Set the value of the imaginary component
        
        ...

        Parameters
        ----------
        imag : TYPE - Float/Int
            DESCRIPTION - Imaginary component of complex number

        Returns
        -------
        None.

        """
        # Set imaginary component value
        self.imag = imag
    
    def getImag(self):
        """
        Get the value of the imaginary component
        
        ...

        Returns
        -------
        TYPE - Float/Int
            DESCRIPTION - Imaginary component of complex number

        """
        # Return imaginary component value
        return self.imag
        
    def __add__(self, other):
        """
        Override the add magic method to add two complex numbers
        
        ...

        Parameters
        ----------
        other : TYPE - Object
            DESCRIPTION - Complex number

        Returns
        -------
        TYPE - Object
            DESCRIPTION - Complex number

        """
        # Overload the add operator between instances of the Complex class
        # Add the real components
        real = self.real + other.real
        # Add the imaginary components
        imag = self.imag + other.imag
        # Return new instance of the Complex class
        return Complex(real,imag)
    
    def __sub__(self, other):
        """
        Override the sub magic method to subtract two complex numbers
        
        ...

        Parameters
        ----------
        other : TYPE - Object
            DESCRIPTION - Complex number

        Returns
        -------
        TYPE - Object
            DESCRIPTION - Complex number

        """
        # Overload the subtract operator between instances of the Complex class
        # Subtract the real components
        real = self.real - other.real
        # Subtract the imaginary components
        imag = self.imag - other.imag
        # Return new instance of the Complex class
        return Complex(real,imag)
    
    def __mul__(self, other):
        """
        Override the mul magic method to multiply two complex numbers
        
        ...

        Parameters
        ----------
        other : TYPE - Object
            DESCRIPTION - Complex number

        Returns
        -------
        TYPE - Object
            DESCRIPTION - Complex number

        """
        # Overload the multiply operator between instances of the Complex class
        # Calculate real component
        real = (self.real * other.real) - (self.imag * other.imag)
        # Calculate imaginary component
        imag = (self.real * other.imag) + (self.imag * other.real)
        # Return new instance of the Complex class
        return Complex(real, imag)
    
    def __truediv__(self, other):
        """
        Override the truediv magic method to divide two complex numbers
        
        ...

        Parameters
        ----------
        other : TYPE - Object
            DESCRIPTION - Complex number

        Returns
        -------
        TYPE - Object
            DESCRIPTION - Complex number

        """
        # Overload the divide operator between instances of the Complex class
        # Calculate real component
        real = (self.real * other.real + self.imag * other.imag)/(other.real**2 + other.imag**2)
        # Calculate imaginary component
        imag = (self.imag * other.real - self.real * other.imag)/(other.real**2 + other.imag**2)
        # Return new instance of the Complex class
        return Complex(real, imag)
    
    
    def __eq__(self, other):
        """
        Override the eq magic method to determine if two complex numbers are equal
        
        ...

        Parameters
        ----------
        other : TYPE - Object
            DESCRIPTION - Complex number

        Returns
        -------
        bool
            DESCRIPTION - True if real and imaginary components are equal, else false

        """
        # Overload the equality operator between instances of the Complex class
        # Return true if both the real and imaginary components are equal, else return false
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False
    
    def magnitude(self):
        """
        Calculate the magnitude or length of a complex number
        
        ...

        Returns
        -------
        TYPE - Float/Int
            DESCRIPTION - Magnitude/Length of complex number

        """
        # Calculate and return the magnitude of the complex number
        self.magnitude = sqrt(self.real**2 + self.imag**2)
        return self.magnitude
    
    def conj(self):
        """
        Calculate the complex conjugate of a complex number
        
        ...

        Returns
        -------
        TYPE - Object
            DESCRIPTION - Complex conjugate of complex number

        """
        # Calculate the complex conjugate of the complex number
        real = self.real
        imag = self.imag * -1
        # Return new instance of the Complex class
        return Complex(real,imag)
