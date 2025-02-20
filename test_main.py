from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    #additional quadratic_multiply tests
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(8)) == 7*8
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(10)) == 5*10
    assert quadratic_multiply(BinaryNumber(11), BinaryNumber(12)) == 11*12

    #additional test_quadratic_multiply tests
    print(test_quadratic_multiply(BinaryNumber(6), BinaryNumber(7), quadratic_multiply))
    print(test_quadratic_multiply(BinaryNumber(1), BinaryNumber(8), quadratic_multiply))
    print(test_quadratic_multiply(BinaryNumber(65), BinaryNumber(9), quadratic_multiply))
