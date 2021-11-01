###############################################################################
#    pyscript_icem_venturi_mesh_gen.py
#    author: Diogo Alexandre Santos
#    email: diogoalexsantos@hotmail.com
#    web: www.github.com/diogoalexsantos
#    version 1.0.0 30/10/2021
###############################################################################

import math

#CHANGE VARIABLES HERE:

# D1 FOR INTERNAL PIPE DIAMETER (mm)
d1 = 52.5
# BETA FOR DIAMETER RATIO
beta = 0.400
# LENGTH/DIAMETER RATIO FOR FLOW DEVELOPMENT
ratio_length_over_diameter = 10
# CONVERGENCE ANGLE (degrees)
angle_1 = 21
# DIVERGENCE ANGLE (degrees)
angle_2 = 10
# FIRST CELL HEIGHT (mm)
first_cell_height = 0.001
# OVERALL SCALE OF NODES (This number should be between 0.5 and 1)
overall_scale = 0.50

###############################################################################
# DO NOT CHANGE CODE BELOW
###############################################################################

# FILE NAME
file_name = f"diameter_{d1:.2f}_beta_{beta:.3f}_scale_{overall_scale:.2f}"

# OGRID ABSOLUTE DISTANCE
o_grid_abs_distance = int(d1/10)

# VARIABLES
c1 = math.tan(angle_1/2 * 3.14159 / 180)
c2 = math.tan(angle_2/2 * 3.14159 / 180)

r1 = (d1*beta)/2
r2 = (d1)/2
p1 = 0
p2 = r1*2
p3 = p2 + (r2-r1)/c2
p4 = (p3 + d1*ratio_length_over_diameter)
p5 = -((r2-r1)/c1)
p6 = (p5 - d1*ratio_length_over_diameter)

a3 = int((p2*2)*overall_scale)
a2 = int((abs(p5))*overall_scale)
a4 = int(((r2-r1)/c2)*overall_scale)
a1 = int((d1/2)*overall_scale*ratio_length_over_diameter)
a5 = int((d1/2)*overall_scale*ratio_length_over_diameter)

b1 = int((d1*0.58)*overall_scale)
b2 = int((d1*0.58)*overall_scale)
b3 = int((d1*0.58)*overall_scale)

my_file = open(f"{file_name}.rpl", "w")

list = [
    f'ic_set_global geo_cad 0 toptol_userset\n',
    f'ic_set_global geo_cad 0.0 toler\n',
    f'ic_undo_group_begin \n',
    f'ic_geo_new_family GEOM\n',
    f'ic_boco_set_part_color GEOM\n',
    f'ic_empty_tetin \n',
    f'ic_point {{}} GEOM pnt.00 {p1},0,0\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_point {{}} GEOM pnt.01 {p2},0,0\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_point {{}} GEOM pnt.02 {p3},0,0\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_point {{}} GEOM pnt.03 {p4},0,0\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_point {{}} GEOM pnt.04 {p5},0,0\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_point {[]} GEOM pnt.05 {p6},0,0\n',
    f'ic_undo_group_end \n',
    f'ic_set_global geo_cad 0 toptol_userset\n',
    f'ic_set_global geo_cad 0.2 toler\n',
    f'ic_set_global geo_cad 0.2 toler\n',
    f'ic_set_global geo_cad 0.2 toler\n',
    f'ic_undo_group_begin \n',
    f'ic_surface cyl GEOM srf.00 {{pnt.05 pnt.04 {r2} {r2} 1 1}}\n',
    f'ic_set_global geo_cad 0.2 toler\n',
    f'ic_set_dormant_pickable point 0 {{}}\n',
    f'ic_set_dormant_pickable curve 0 {{}}\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_surface cyl GEOM srf.01 {{pnt.04 pnt.00 {r2} {r1} 1 1}}\n',
    f'ic_set_global geo_cad 0.2 toler\n',
    f'ic_set_dormant_pickable point 0 {{}}\n',
    f'ic_set_dormant_pickable curve 0 {{}}\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_surface cyl GEOM srf.02 {{pnt.00 pnt.01 {r1} {r1} 1 1}}\n',
    f'ic_set_global geo_cad 0.2 toler\n',
    f'ic_set_dormant_pickable point 0 {{}}\n',
    f'ic_set_dormant_pickable curve 0 {{}}\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_surface cyl GEOM srf.03 {{pnt.01 pnt.02 {r1} {r2} 1 1}}\n',
    f'ic_set_global geo_cad 0.2 toler\n',
    f'ic_set_dormant_pickable point 0 {{}}\n',
    f'ic_set_dormant_pickable curve 0 {{}}\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_surface cyl GEOM srf.04 {{pnt.02 pnt.03 {r2} {r2} 1 1}}\n',
    f'ic_set_global geo_cad 0.2 toler\n',
    f'ic_set_dormant_pickable point 0 {{}}\n',
    f'ic_set_dormant_pickable curve 0 {{}}\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_geo_set_part surface srf.00.S1 INLET 0\n',
    f'ic_delete_empty_parts \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_geo_set_part surface srf.04.S2 OUTLET 0\n',
    f'ic_delete_empty_parts \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_geo_set_part surface {{srf.03 srf.04 srf.01 srf.02 srf.00}} WALL 0\n',
    f'ic_delete_empty_parts \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_geo_new_family FLUID\n',
    f'ic_boco_set_part_color FLUID\n',
    f'ic_geo_create_volume {{100 0 0}} {{}} FLUID\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_initialize_blocking {{surface srf.00.S1 surface srf.04.S2}} FLUID 0 101\n',
    f'ic_hex_unblank_blocks \n',
    f'ic_hex_multi_grid_level 0\n',
    f'ic_hex_projection_limit 0\n',
    f'ic_hex_default_bunching_law default 2.0\n',
    f'ic_hex_floating_grid off\n',
    f'ic_hex_transfinite_degree 1\n',
    f'ic_hex_unstruct_face_type one_tri\n',
    f'ic_hex_set_unstruct_face_method uniform_quad\n',
    f'ic_hex_set_n_tetra_smoothing_steps 20\n',
    f'ic_hex_error_messages off_minor\n',
    f'ic_hex_set_piercing 0\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_undo_major_start split_grid\n',
    f'ic_hex_split_grid 25 41 pnt.04 m GEOM INLET OUTLET WALL FLUID\n',
    f'ic_hex_undo_major_end split_grid\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_undo_major_start split_grid\n',
    f'ic_hex_split_grid 70 41 pnt.00 m GEOM INLET OUTLET WALL FLUID\n',
    f'ic_hex_undo_major_end split_grid\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_undo_major_start split_grid\n',
    f'ic_hex_split_grid 86 41 pnt.01 m GEOM INLET OUTLET WALL FLUID\n',
    f'ic_hex_undo_major_end split_grid\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_undo_major_start split_grid\n',
    f'ic_hex_split_grid 102 41 pnt.02 m GEOM INLET OUTLET WALL FLUID\n',
    f'ic_hex_undo_major_end split_grid\n',
    f'ic_undo_group_end \n',
    f'ic_hex_find_comp_curve srf.00.C0\n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_edge_projection 25 26 0 1 srf.00.C0\n',
    f'ic_hex_set_edge_projection 21 25 0 1 srf.00.C0\n',
    f'ic_hex_set_edge_projection 21 22 0 1 srf.00.C0\n',
    f'ic_hex_set_edge_projection 22 26 0 1 srf.00.C0\n',
    f'ic_undo_group_end \n',
    f'ic_hex_find_comp_curve srf.00.C1\n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_edge_projection 70 74 0 1 srf.00.C1\n',
    f'ic_hex_set_edge_projection 69 70 0 1 srf.00.C1\n',
    f'ic_hex_set_edge_projection 69 73 0 1 srf.00.C1\n',
    f'ic_hex_set_edge_projection 73 74 0 1 srf.00.C1\n',
    f'ic_undo_group_end \n',
    f'ic_hex_find_comp_curve srf.01.C1\n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_edge_projection 86 90 0 1 srf.01.C1\n',
    f'ic_hex_set_edge_projection 85 86 0 1 srf.01.C1\n',
    f'ic_hex_set_edge_projection 85 89 0 1 srf.01.C1\n',
    f'ic_hex_set_edge_projection 89 90 0 1 srf.01.C1\n',
    f'ic_undo_group_end \n',
    f'ic_hex_find_comp_curve srf.02.C1\n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_edge_projection 102 106 0 1 srf.02.C1\n',
    f'ic_hex_set_edge_projection 101 102 0 1 srf.02.C1\n',
    f'ic_hex_set_edge_projection 101 105 0 1 srf.02.C1\n',
    f'ic_hex_set_edge_projection 105 106 0 1 srf.02.C1\n',
    f'ic_undo_group_end \n',
    f'ic_hex_find_comp_curve srf.03.C1\n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_edge_projection 118 122 0 1 srf.03.C1\n',
    f'ic_hex_set_edge_projection 117 118 0 1 srf.03.C1\n',
    f'ic_hex_set_edge_projection 117 121 0 1 srf.03.C1\n',
    f'ic_hex_set_edge_projection 121 122 0 1 srf.03.C1\n',
    f'ic_undo_group_end \n',
    f'ic_hex_find_comp_curve srf.04.C1\n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_edge_projection 41 42 0 1 srf.04.C1\n',
    f'ic_hex_set_edge_projection 37 41 0 1 srf.04.C1\n',
    f'ic_hex_set_edge_projection 37 38 0 1 srf.04.C1\n',
    f'ic_hex_set_edge_projection 38 42 0 1 srf.04.C1\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_project_to_surface FLUID WALL INLET GEOM OUTLET\n',
    f'ic_undo_group_end \n',
    f'ic_hex_mark_blocks unmark\n',
    f'ic_undo_group_begin \n',
    f'ic_hex_mark_blocks face_neighbors corners {{ 21 25 22 26 }} {{ 69 70 73 74 }} {{ 85 86 89 90 }} {{ 101 102 105 106 }} {{ 117 118 121 122 }} {{ 37 41 38 42 }}\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_ogrid distance {o_grid_abs_distance} fix_dist m GEOM INLET OUTLET WALL FLUID -version 50\n',
    f'ic_hex_mark_blocks unmark\n',
    f'ic_undo_group_end \n',
    f'ic_hex_mark_blocks unmark\n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 86 102 n {a3} h1rel 1 h2rel 1 r1 2 r2 2 lmax 1 default copy_to_parallel unlocked\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 86 102 n {a3} h1rel 1 h2rel 1 r1 2 r2 2 lmax 1 default copy_to_parallel unlocked\n',
    f'ic_undo_group_begin \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_match_edges 86 102 102 118\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 102 118 n {a4} h1rel 1 h2rel 1 r1 2 r2 2 lmax 1 default copy_to_parallel unlocked\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 102 118 n {a4} h1rel 1 h2rel 1 r1 2 r2 2 lmax 1 geo1 copy_to_parallel unlocked\n',
    f'ic_undo_group_begin \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_match_edges 86 102 70 86\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 70 86 n {a2} h1rel 115704315.308 h2rel 1 r1 2 r2 2 lmax 1 default copy_to_parallel unlocked\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 70 86 n {a2} h1rel 115704315.308 h2rel 1 r1 2 r2 2 lmax 1 geo2 copy_to_parallel unlocked\n',
    f'ic_undo_group_begin \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 25 70 n {a5} h1rel 190476190.476 h2rel 1 r1 2 r2 2 lmax 1 default copy_to_parallel unlocked\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 25 70 n {a5} h1rel 190476190.476 h2rel 1 r1 2 r2 2 lmax 1 default copy_to_parallel unlocked\n',
    f'ic_undo_group_begin \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 118 41 n {a1} h1rel 190476190.476 h2rel 1 r1 2 r2 2 lmax 1 default copy_to_parallel unlocked\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 118 41 n {a1} h1rel 190476190.476 h2rel 1 r1 2 r2 2 lmax 1 default copy_to_parallel unlocked\n',
    f'ic_undo_group_begin \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 134 135 n {b1} h1rel 0.0 h2rel 0.0 r1 2 r2 2 lmax 0 default copy_to_parallel unlocked\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 134 135 n {b1} h1rel 0.0 h2rel 0.0 r1 2 r2 2 lmax 0 default copy_to_parallel unlocked\n',
    f'ic_undo_group_begin \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin\n',
    f'ic_hex_set_mesh 132 134 n {b2} h1rel 0.0 h2rel 0.0 r1 2 r2 2 lmax 0 default copy_to_parallel unlocked\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 132 134 n {b2} h1rel 0.0 h2rel 0.0 r1 2 r2 2 lmax 0 default copy_to_parallel unlocked\n',
    f'ic_undo_group_begin\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 25 134 n 3 h1rel 0.0 h2rel 0.0 r1 2 r2 2 lmax 0 default copy_to_parallel unlocked\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 25 134 n {b3} h1rel 0.0 h2rel 0.0 r1 2 r2 2 lmax 0 default copy_to_parallel unlocked\n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_begin \n',
    f'ic_hex_set_mesh 25 134 n {b3} h1rel {first_cell_height/o_grid_abs_distance} h2rel 0.0 r1 1.2 r2 2 lmax 0 geo1 copy_to_parallel unlocked\n',
    f'ic_undo_group_begin \n',
    f'ic_undo_group_end \n',
    f'ic_undo_group_end \n',
    f'ic_hex_create_mesh GEOM INLET OUTLET WALL FLUID proj 2 dim_to_mesh 3\n',
    f'ic_undo_group_begin \n',
    f'ic_uns_diag_reset_degen_min_max \n',
    f'ic_hex_ratio_histogram 20 GEOM INLET OUTLET WALL FLUID proj 2 minval 0 -type determinant maxval 1 new_format\n',
    f'ic_undo_group_end'
    ]

print(my_file)
my_file.writelines(list)
my_file.close()

