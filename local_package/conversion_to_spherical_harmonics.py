

from typing import Literal
# from pydantic import validate_call; val_call=validate_call(config=dict(arbitrary_types_allowed=True))
import numpy as np

from enum import Enum

class recognized_prop_tags(Enum):
    dipole='D'
    quadrupole='Q'
    ddpol='DDP'
    qqpol='QQP'

# @val_call
def traceless_cartesian_to_spherical(prop, prop_type:recognized_prop_tags):
    prop=np.array(prop)
    assert len(prop.shape)==1, f"Expected one dimensional arrays as input, got: {prop}"
    if prop_type in [recognized_prop_tags.dipole.value, recognized_prop_tags.ddpol.value ]:
        assert len(prop)==3
        ar=[ prop[-1], prop[0], prop[1]]
    elif prop_type==recognized_prop_tags.quadrupole.value:
        assert len(prop)==6
        xx,xy,xz,yy,yz,zz=prop
        sqr3=np.sqrt(3)
        ar= [
            3/2  * zz, 
            sqr3*xz,  # 3/2 * 2/sqr3*xz, 
            sqr3*yz, 
            sqr3/2*(xx-yy), 
            sqr3*xy, # is sqr(3)
        ]
    elif prop_type==recognized_prop_tags.qqpol.value:
        assert len(prop)==6
        xx,xy,xz,yy,yz,zz=prop
        ar = [
            9/4* zz,
            3 * xz,
            3 * yz,
            np.nan, # undetermined due to lack of xx,yy cross-term
            3 * xy,
        ]
    else: raise ValueError(f"unkown property type: {prop_type}")
    return np.array(ar)

