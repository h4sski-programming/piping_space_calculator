from math import ceil

from .pipe_db import pipe_dimensions, flange_dimensions, flange_dimensions_pn16


def calculate_pipe_space(dn_1, dn_2, flange, min_gap):
    # od_1 = flange_dimensions_pn16[50]['OD']
    # od_2 = int(dn_2)
    # min_gap = int(min_gap)
    if flange == 'NONE':
        return ceil((pipe_dimensions[dn_1]['OD']/2 + pipe_dimensions[dn_2]['OD']/2 + min_gap)/10)*10
    else:
        return ceil((flange_dimensions[flange][dn_1]['OD']/2 + pipe_dimensions[dn_2]['OD']/2 + min_gap)/10)*10
    # return ceil((flange_dimensions_pn16[dn_1]['OD']/2 + pipe_dimensions[dn_2]['OD']/1 + min_gap)/10)*10
