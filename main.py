"""
calculer la distance euclidienne entre deux points
"""
import math


def calc_dis(p_x_1:int, p_y_1:int, p_x_2:int, p_y_2:int):
    """
    calcule la distance entre deux point
    :param p_x_1: coordn x prem point
    :param p_y_1: coordn y prem point
    :param p_x_2: coordn x deuxi point
    :param p_y_2: coordn y deuxi point
    :return: distance euclidienne entre les deux point
    """
    return math.sqrt((p_x_1 - p_x_2) ^ 2 + (p_y_1 - p_y_2) ^ 2)


point1_x = 12
point1_y = 10
point2_x = 22
point2_y = 26
# appeler la fonction calculer distance
print("distance entre deux point est",
        calc_dis(point1_x, point1_y, point2_x, point2_y))
#afficher la disrtab ebtre aey piae
