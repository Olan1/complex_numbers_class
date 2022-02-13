from numpy import sqrt

class Complex:
    
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

        Returns
        -------
        TYPE - Float/Int
            DESCRIPTION - Real component of complex number

        """
        # Return real component value
        return self.real
    
    def setImag(self, imag):
        """

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

        Returns
        -------
        TYPE - Float/Int
            DESCRIPTION - Imaginary component of complex number

        """
        # Return imaginary component value
        return self.imag
        
    def __add__(self, other):
        """

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
      
