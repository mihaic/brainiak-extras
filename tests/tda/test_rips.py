# Copyright 2016 Intel Corporation
#
# This file is part of brainiak-extras.
#
# brainiak-extras is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# brainiak-extras is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with brainiak-extras.  If not, see <http://www.gnu.org/licenses/>.


from brainiak_extras.tda.rips import rips_filtration, _lower_neighbors
import numpy as np

inf = float('inf')


def assert_barcodes(mat, dim, scale, barcodes):
    pairs_with_dim = rips_filtration(dim, scale, mat)

    print("\nThere are %d persistence pairs: " % len(pairs_with_dim))
    for triplet in pairs_with_dim:
        print("Birth: ", triplet[0], ", Death: ", triplet[1], type(triplet[1]), ", Dimension: ", triplet[2])
    print(pairs_with_dim)
    assert pairs_with_dim == barcodes


def reference_lower_neighbors(dist_Mat,max_Scale):
    LN=[]
    for i in range(np.shape(dist_Mat)[0]):
        LN_List=[]
        for j in range(i):
            if dist_Mat[i][j]<=max_Scale:
                LN_List.append(j)
        LN.append(LN_List)
    return LN

dist_mat_1 = [[0,   1,   1,   1.4],
              [1,   0,   1.4, 1],
              [1,   1.4, 0,   1],
              [1.4, 1,   1,   0]]

def test_lower_neighbors_inf():
    assert _lower_neighbors(dist_mat_1, inf) == reference_lower_neighbors(dist_mat_1, inf)

def test_lower_neighbors_partial():
    assert _lower_neighbors(dist_mat_1, 1) == reference_lower_neighbors(dist_mat_1, 1)

def test_lower_neighbors_zero():
    d = np.array(dist_mat_1)
    d[3][0] = 0
    d[0][3] = 0
    assert _lower_neighbors(d, inf) == reference_lower_neighbors(d, inf)

def test_dist_mat_1():
    assert_barcodes(dist_mat_1, 2, inf,
                    [(1, 1.4, 1),
                     (0, 1, 0),
                     (0, 1, 0),
                     (0, 1, 0),
                     (1.4, inf, 2),
                     (0, inf, 0)])


def test_dist_mat_3():
    dist_mat_3 = [
        [0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0],
        [2, 4, 0, 0, 0],
        [3, 10, 1, 0, 0],
        [16, 11, 9, 10, 0]]

    assert_barcodes(dist_mat_3, 2, inf, [(0, 9, 0),
                                         (0, 1, 0),
                                         (0, 2, 0),
                                         (0, 4, 0),
                                         (16, inf, 2),
                                         (16, inf, 2),
                                         (11, inf, 2),
                                         (10, inf, 2),
                                         (0, inf, 0)])


def test_dist_mat_2():
    dist_mat_2 = \
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [85, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [120, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [10, 73, 44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [37, 47, 76, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [14, 104, 116, 97, 58, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [57, 111, 78, 93, 22, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [91, 55, 45, 56, 107, 7, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [62, 105, 81, 72, 94, 34, 52, 30, 0, 0, 0, 0, 0, 0, 0, 0],
         [77, 117, 17, 103, 19, 28, 99, 29, 89, 0, 0, 0, 0, 0, 0, 0],
         [108, 101, 43, 25, 53, 65, 40, 98, 75, 13, 0, 0, 0, 0, 0, 0],
         [51, 92, 112, 36, 100, 115, 2, 82, 70, 32, 38, 0, 0, 0, 0, 0],
         [12, 90, 24, 68, 86, 64, 8, 59, 49, 69, 114, 3, 0, 0, 0, 0],
         [95, 35, 61, 15, 71, 31, 74, 41, 5, 4, 16, 84, 50, 0, 0, 0],
         [27, 102, 87, 39, 118, 109, 21, 11, 9, 83, 88, 80, 60, 66, 0, 0],
         [18, 54, 67, 79, 26, 96, 6, 20, 63, 1, 33, 110, 113, 106, 119, 0]
         ]
    result = [(49, 52, 1), (48, 55, 1), (47, 55, 1), (36, 38, 1), (32, 40, 1), (28, 29, 1), (27, 56, 1), (24, 59, 1),
              (22, 26, 1), (21, 23, 1), (20, 34, 1), (18, 53, 1), (15, 51, 1), (14, 57, 1), (0, 1, 0), (0, 9, 0),
              (0, 4, 0), (0, 3, 0), (0, 2, 0), (0, 13, 0), (0, 5, 0), (0, 6, 0), (0, 7, 0), (0, 11, 0), (0, 12, 0),
              (0, 19, 0), (0, 10, 0), (0, 17, 0), (0, 35, 0), (120, inf, 2), (120, inf, 2), (120, inf, 2),
              (120, inf, 2), (120, inf, 2), (120, inf, 2), (120, inf, 2), (120, inf, 2), (120, inf, 2), (120, inf, 2),
              (120, inf, 2), (120, inf, 2), (120, inf, 2), (119, inf, 2), (119, inf, 2), (119, inf, 2), (119, inf, 2),
              (119, inf, 2), (119, inf, 2), (119, inf, 2), (119, inf, 2), (119, inf, 2), (119, inf, 2), (119, inf, 2),
              (119, inf, 2), (119, inf, 2), (118, inf, 2), (118, inf, 2), (118, inf, 2), (118, inf, 2), (118, inf, 2),
              (118, inf, 2), (118, inf, 2), (118, inf, 2), (118, inf, 2), (118, inf, 2), (118, inf, 2), (118, inf, 2),
              (117, inf, 2), (117, inf, 2), (117, inf, 2), (117, inf, 2), (117, inf, 2), (117, inf, 2), (117, inf, 2),
              (117, inf, 2), (117, inf, 2), (117, inf, 2), (117, inf, 2), (117, inf, 2), (117, inf, 2), (116, inf, 2),
              (116, inf, 2), (116, inf, 2), (116, inf, 2), (116, inf, 2), (116, inf, 2), (116, inf, 2), (116, inf, 2),
              (116, inf, 2), (116, inf, 2), (116, inf, 2), (116, inf, 2), (115, inf, 2), (115, inf, 2), (115, inf, 2),
              (115, inf, 2), (115, inf, 2), (115, inf, 2), (115, inf, 2), (115, inf, 2), (115, inf, 2), (115, inf, 2),
              (115, inf, 2), (115, inf, 2), (114, inf, 2), (114, inf, 2), (114, inf, 2), (114, inf, 2), (114, inf, 2),
              (114, inf, 2), (114, inf, 2), (114, inf, 2), (114, inf, 2), (114, inf, 2), (114, inf, 2), (114, inf, 2),
              (114, inf, 2), (113, inf, 2), (113, inf, 2), (113, inf, 2), (113, inf, 2), (113, inf, 2), (113, inf, 2),
              (113, inf, 2), (113, inf, 2), (113, inf, 2), (113, inf, 2), (113, inf, 2), (112, inf, 2), (112, inf, 2),
              (112, inf, 2), (112, inf, 2), (112, inf, 2), (112, inf, 2), (112, inf, 2), (112, inf, 2), (112, inf, 2),
              (112, inf, 2), (112, inf, 2), (111, inf, 2), (111, inf, 2), (111, inf, 2), (111, inf, 2), (111, inf, 2),
              (111, inf, 2), (111, inf, 2), (111, inf, 2), (111, inf, 2), (111, inf, 2), (111, inf, 2), (111, inf, 2),
              (110, inf, 2), (110, inf, 2), (110, inf, 2), (110, inf, 2), (110, inf, 2), (110, inf, 2), (110, inf, 2),
              (110, inf, 2), (110, inf, 2), (109, inf, 2), (109, inf, 2), (109, inf, 2), (109, inf, 2), (109, inf, 2),
              (109, inf, 2), (109, inf, 2), (109, inf, 2), (109, inf, 2), (108, inf, 2), (108, inf, 2), (108, inf, 2),
              (108, inf, 2), (108, inf, 2), (108, inf, 2), (108, inf, 2), (108, inf, 2), (108, inf, 2), (108, inf, 2),
              (108, inf, 2), (107, inf, 2), (107, inf, 2), (107, inf, 2), (107, inf, 2), (107, inf, 2), (107, inf, 2),
              (107, inf, 2), (107, inf, 2), (107, inf, 2), (107, inf, 2), (107, inf, 2), (107, inf, 2), (106, inf, 2),
              (106, inf, 2), (106, inf, 2), (106, inf, 2), (106, inf, 2), (106, inf, 2), (106, inf, 2), (106, inf, 2),
              (106, inf, 2), (106, inf, 2), (105, inf, 2), (105, inf, 2), (105, inf, 2), (105, inf, 2), (105, inf, 2),
              (105, inf, 2), (105, inf, 2), (105, inf, 2), (105, inf, 2), (105, inf, 2), (105, inf, 2), (104, inf, 2),
              (104, inf, 2), (104, inf, 2), (104, inf, 2), (104, inf, 2), (104, inf, 2), (104, inf, 2), (103, inf, 2),
              (103, inf, 2), (103, inf, 2), (103, inf, 2), (103, inf, 2), (103, inf, 2), (103, inf, 2), (103, inf, 2),
              (103, inf, 2), (103, inf, 2), (103, inf, 2), (103, inf, 2), (102, inf, 2), (102, inf, 2), (102, inf, 2),
              (102, inf, 2), (102, inf, 2), (102, inf, 2), (102, inf, 2), (101, inf, 2), (101, inf, 2), (101, inf, 2),
              (101, inf, 2), (101, inf, 2), (101, inf, 2), (100, inf, 2), (100, inf, 2), (100, inf, 2), (100, inf, 2),
              (100, inf, 2), (100, inf, 2), (100, inf, 2), (100, inf, 2), (99, inf, 2), (99, inf, 2), (99, inf, 2),
              (99, inf, 2), (99, inf, 2), (99, inf, 2), (99, inf, 2), (99, inf, 2), (99, inf, 2), (99, inf, 2),
              (99, inf, 2), (98, inf, 2), (98, inf, 2), (98, inf, 2), (98, inf, 2), (98, inf, 2), (98, inf, 2),
              (98, inf, 2), (98, inf, 2), (98, inf, 2), (97, inf, 2), (97, inf, 2), (97, inf, 2), (97, inf, 2),
              (97, inf, 2), (97, inf, 2), (97, inf, 2), (97, inf, 2), (96, inf, 2), (96, inf, 2), (96, inf, 2),
              (96, inf, 2), (96, inf, 2), (96, inf, 2), (95, inf, 2), (95, inf, 2), (95, inf, 2), (95, inf, 2),
              (95, inf, 2), (95, inf, 2), (95, inf, 2), (95, inf, 2), (95, inf, 2), (95, inf, 2), (94, inf, 2),
              (94, inf, 2), (94, inf, 2), (94, inf, 2), (94, inf, 2), (94, inf, 2), (94, inf, 2), (94, inf, 2),
              (94, inf, 2), (93, inf, 2), (93, inf, 2), (93, inf, 2), (93, inf, 2), (93, inf, 2), (93, inf, 2),
              (93, inf, 2), (93, inf, 2), (93, inf, 2), (93, inf, 2), (92, inf, 2), (92, inf, 2), (92, inf, 2),
              (92, inf, 2), (91, inf, 2), (91, inf, 2), (91, inf, 2), (91, inf, 2), (91, inf, 2), (91, inf, 2),
              (91, inf, 2), (91, inf, 2), (91, inf, 2), (90, inf, 2), (90, inf, 2), (90, inf, 2), (90, inf, 2),
              (90, inf, 2), (89, inf, 2), (89, inf, 2), (89, inf, 2), (89, inf, 2), (89, inf, 2), (89, inf, 2),
              (89, inf, 2), (89, inf, 2), (89, inf, 2), (88, inf, 2), (88, inf, 2), (88, inf, 2), (88, inf, 2),
              (88, inf, 2), (88, inf, 2), (87, inf, 2), (87, inf, 2), (87, inf, 2), (87, inf, 2), (87, inf, 2),
              (87, inf, 2), (86, inf, 2), (86, inf, 2), (86, inf, 2), (86, inf, 2), (86, inf, 2), (86, inf, 2),
              (85, inf, 2), (85, inf, 2), (84, inf, 2), (84, inf, 2), (84, inf, 2), (84, inf, 2), (84, inf, 2),
              (84, inf, 2), (84, inf, 2), (83, inf, 2), (83, inf, 2), (83, inf, 2), (83, inf, 2), (82, inf, 2),
              (82, inf, 2), (82, inf, 2), (82, inf, 2), (82, inf, 2), (81, inf, 2), (81, inf, 2), (81, inf, 2),
              (81, inf, 2), (81, inf, 2), (81, inf, 2), (80, inf, 2), (80, inf, 2), (80, inf, 2), (80, inf, 2),
              (79, inf, 2), (79, inf, 2), (79, inf, 2), (79, inf, 2), (79, inf, 2), (79, inf, 2), (78, inf, 2),
              (78, inf, 2), (78, inf, 2), (78, inf, 2), (78, inf, 2), (77, inf, 2), (77, inf, 2), (77, inf, 2),
              (77, inf, 2), (76, inf, 2), (76, inf, 2), (76, inf, 2), (76, inf, 2), (76, inf, 2), (75, inf, 2),
              (75, inf, 2), (75, inf, 2), (75, inf, 2), (75, inf, 2), (74, inf, 2), (74, inf, 2), (74, inf, 2),
              (74, inf, 2), (74, inf, 2), (74, inf, 2), (73, inf, 2), (73, inf, 2), (73, inf, 2), (72, inf, 2),
              (72, inf, 2), (72, inf, 2), (72, inf, 2), (72, inf, 2), (71, inf, 2), (71, inf, 2), (71, inf, 2),
              (71, inf, 2), (70, inf, 2), (70, inf, 2), (69, inf, 2), (69, inf, 2), (69, inf, 2), (69, inf, 2),
              (68, inf, 2), (68, inf, 2), (68, inf, 2), (68, inf, 2), (68, inf, 2), (67, inf, 2), (67, inf, 2),
              (67, inf, 2), (66, inf, 2), (66, inf, 2), (66, inf, 2), (65, inf, 2), (65, inf, 2), (65, inf, 2),
              (64, inf, 2), (64, inf, 2), (64, inf, 2), (64, inf, 2), (63, inf, 2), (63, inf, 2), (62, inf, 2),
              (62, inf, 2), (62, inf, 2), (61, inf, 2), (61, inf, 2), (61, inf, 2), (61, inf, 2), (61, inf, 2),
              (60, inf, 2), (60, inf, 2), (60, inf, 2), (59, inf, 2), (59, inf, 2), (58, inf, 2), (58, inf, 2),
              (57, inf, 2), (57, inf, 2), (57, inf, 2), (57, inf, 2), (56, inf, 2), (53, inf, 2), (53, inf, 2),
              (52, inf, 2), (52, inf, 2), (41, inf, 2), (41, inf, 2), (0, inf, 0)]
    assert_barcodes(dist_mat_2, 2, inf, result)
