# print(__name__)

# from geometry import *
import test_geometry.planimetry as pl
import test_geometry.stereometry as st

if __name__ == '__main__':
    c1 = pl.Circle(1)
    c2 = st.Ball(1)

    print(c1.square())
    print(c2.V())

