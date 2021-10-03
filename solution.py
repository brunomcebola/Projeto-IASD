from registration import registration
from get_pointcloud import point_cloud_data

import numpy as np
from typing import Tuple


class registration_iasd(registration):

    def __init__(self, scan_1: np.array((..., 3)), scan_2: np.array((..., 3))) -> None:

        # inherit all the methods and properties from registration
        super().__init__(scan_1, scan_2)

        return

    def compute_pose(self,correspondences: dict) -> Tuple[np.array, np.array]:
        """compute the transformation that aligns two
        scans given a set of correspondences

        :param correspondences: set of correspondences
        :type correspondences: dict
        :return: rotation and translation that align the correspondences
        :rtype: Tuple[np.array, np.array]
        """
        
        pass


    def find_closest_points(self) -> dict:
        """Computes the closest points in the two scans.
        There are many strategies. We are taking all the points in the first scan
        and search for the closes in the second. This means that we can have > than 1 points in scan
        1 corresponding to the same point in scan 2. All points in scan 1 will have correspondence.
        Points in scan 2 do not have necessarily a correspondence.

        :param search_alg: choose the searching option
        :type search_alg: str, optional
        :return: a dictionary with the correspondences. Keys are numbers identifying the id of the correspondence.
                Values are a dictionaries with 'point_in_pc_1', 'point_in_pc_2' identifying the pair of points in the correspondence.
        :rtype: dict
        """

        pass


class point_cloud_data_iasd(point_cloud_data):

    def __init__(
            self,
            fileName: str,
            ) -> None:
            
        super().__init__(fileName)

        return


    def load_point_cloud(
            self,
            file: str
            ) -> bool:
        """Loads a point cloud from a ply file

        :param file: source file
        :type file: str
        :return: returns true or false, depending on whether the method
        the ply was OK or not
        :rtype: bool
        """

        with open(file, "r") as fp:
            point_order = []
            while True:
                line = fp.readline().split()
            
                if line[0]=="element":
                    if line[1]=="vertex":
                        n_vertex = int(line[2])
                elif line[0] == "property" and line[1]=="float":
                    if line[2] == "x":
                        point_order.append("x")
                    if line[2] == "y":
                        point_order.append("y")
                    if line[2] == "z":
                        point_order.append("z")
                        
                if line[0] == "end_header":
                    break
            
            if len(point_order) != 3 :
                return False

            for i in range(n_vertex):
                line = fp.readline().split()
                
                # point_list = ["","",""]
                # #[x, z, y]
                # point_list[0] = line[ point_order.index("x") ]
                # point_list[1] = line[point_order.index("y")]
                # point_list[2] = line[point_order.index("z")]

                point_list = [ float(line[point_order.index(j)]) for j in ["x", "y", "z"] ]
                
                self.data[str(i)] = np.array(point_list)

        return True